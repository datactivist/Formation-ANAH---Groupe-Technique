# Atelier revue de code - Gestion des arrêtés de péril

Script CLI qui charge le CSV des arrêtés de péril (Marseille, jeu de données
fictif) dans une base SQLite locale, et permet de le consulter.

## Prérequis

- Python 3.8 ou supérieur
- Aucune dépendance externe : le script n'utilise que la bibliothèque
  standard (`sqlite3`, `csv`)

Vérifier votre version de Python :

```bash
python3 --version
```

## Fichiers

```py
config.py               # configuration
db_utils.py              # chargement CSV + accès base de données
gestion_arretes.py        # script principal (à lancer)
arretes_peril_marseille_ATTENDU.csv   # données à placer dans le même dossier
```

Les 4 fichiers (dont le CSV) doivent être **dans le même dossier**.

## Lancer le script

Depuis un terminal, dans le dossier où se trouvent les fichiers :

```bash
python3 gestion_arretes.py
```

Un menu s'affiche :

```txt
1. Charger les données
2. Rechercher par propriétaire
3. Rechercher par adresse
4. Détecter les doublons d'adresse
5. Statistiques
6. Mode admin
7. Filtre personnalisé (avancé)
0. Quitter
```

Commencez toujours par l'option **1** (chargement du CSV en base), avant
d'utiliser les autres options.

## Objectif de l'atelier

Ce script contient des défauts volontaires à identifier et corriger, répartis
sur 5 thématiques : erreurs, failles de sécurité, performance, factorisation,
documentation. Il ne fonctionne pas correctement tel quel, c'est normal,
c'est le point de départ de l'exercice.

## Réinitialiser

Le script crée un fichier `arretes.db` à côté des sources lors du premier
chargement. Pour repartir d'un état propre :

```bash
rm arretes.db
```
