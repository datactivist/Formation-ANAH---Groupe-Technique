import db_utils
import config


def afficher_menu():
    print("1. Charger les données")
    print("2. Rechercher par propriétaire")
    print("3. Rechercher par adresse")
    print("4. Détecter les doublons d'adresse")
    print("5. Statistiques")
    print("6. Mode admin")
    print("7. Filtre personnalisé (avancé)")
    print("0. Quitter")


def charger(chemin=None):
    if chemin is None:
        chemin = config.CSV_PATH
    conn = db_utils.init_db()
    rows = db_utils.load_csv(chemin)
    db_utils.insert_rows(conn, rows)
    print("Données chargées.")


def rapport(resultats):
    texte = ""
    for r in resultats:
        texte += str(r) + "\n"
    return texte


def ajouter_historique(entree, historique=[]):
    historique.append(entree)
    return historique


def mode_admin():
    mdp = input("Mot de passe admin : ")
    if mdp == config.ADMIN_PASSWORD:
        print("Accès admin OK. Clé API :", config.API_KEY)
    else:
        print("Mot de passe incorrect")


def filtre_personnalise():
    expr = input("Entrez une condition Python (ex: 2 + 2) : ")
    resultat = eval(expr)
    print(resultat)


def main():
    while True:
        afficher_menu()
        choix = input("Choix : ")

        if choix == "1":
            chemin = input("Chemin du fichier CSV (laisser vide pour le défaut) : ")
            if chemin.strip() == "":
                charger()
            else:
                charger(chemin)

        elif choix == "2":
            terme = input("Nom du propriétaire : ")
            res = db_utils.search_by_owner(terme)
            ajouter_historique(terme)
            print(rapport(res))

        elif choix == "3":
            terme = input("Adresse : ")
            res = db_utils.search_by_address(terme)
            ajouter_historique(terme)
            print(rapport(res))

        elif choix == "4":
            print(db_utils.find_duplicates())

        elif choix == "5":
            print("Taux de péril imminent :", db_utils.statistiques(), "%")

        elif choix == "6":
            mode_admin()

        elif choix == "7":
            filtre_personnalise()

        elif choix == "0":
            break


if __name__ == "__main__":
    main()
