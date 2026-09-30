# Formation ANAH - Groupe Technique

Formation à l'utilisation d'assistants IA (Mistral / GitHub Copilot) pour
l'aide au développement, à travers deux ateliers pratiques.

## Objectif des ateliers

### Atelier 1 - Extraction de données depuis un PDF

Utiliser un assistant IA pour **écrire du code** capable d'extraire des
données structurées (arrêtés de péril) depuis un document PDF, en combinant
règles (regex) et reconnaissance d'entités nommées (NER).

### Atelier 2 - Revue de code assistée par IA

Utiliser un assistant IA pour **déboguer, optimiser et améliorer** un code
existant (script de gestion des arrêtés de péril) contenant des défauts
volontaires : erreurs, failles de sécurité, problèmes de performance,
manque de factorisation et de documentation.

➡️ Voir [atelier_2/README.md](atelier_2/README.md)

## Prise en main de VS Code avec Mistral et GitHub Copilot

1. Installer [Visual Studio Code](https://code.visualstudio.com/).
2. Installer les extensions nécessaires depuis l'onglet Extensions
   (`Ctrl+Shift+X`) :
   - **Mistral Vibe** (ou **Continue**, l'extension équivalente permettant
     d'utiliser l'API Mistral / Le Chat) : configurer une clé API Mistral
     (obtenue sur [console.mistral.ai](https://console.mistral.ai/)) dans
     les paramètres de l'extension.
   - **GitHub Copilot** (et **GitHub Copilot Chat**) : créer un compte
     GitHub si besoin, puis se connecter depuis VS Code
     (`Ctrl+Shift+P` → `GitHub Copilot: Sign in`). La version gratuite
     (Copilot Free) suffit pour cette formation.
3. Ouvrir le dossier du projet dans VS Code (`Fichier > Ouvrir le dossier...`).
4. Installer l'extension **Python** (Microsoft) pour l'exécution et le
   débogage des scripts.
5. Ouvrir la palette de commandes assistant (Mistral Vibe / Continue ou
   Copilot Chat) via l'icône dédiée dans la barre latérale, ou `Ctrl+Alt+I`.

## Démarrer un projet Python

Depuis un terminal, à la racine du dépôt :

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

Une fois l'environnement activé, les scripts de chaque atelier peuvent être
lancés normalement (voir le `README.md` de chaque atelier pour le détail).
