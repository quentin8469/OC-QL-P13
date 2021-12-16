## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

Fonctionnement resumé:

Lors de l'envoi d'un commit sur la branch "master" du projet present sur Github, circleCI (lui meme lié au repository) va declancher plusieurs processus automatiquement :
1. Réalisatations des tests pour verifier le fonctionnement du code.
2. Si la premiere étape est un succes, alors l'etape de conteneurisation de l'application demarre et sera envoyer sur DockerHub.
3. Si la premiere étape est un succes, l'application sera envoyée sur Heroku pour effectuer son deploiement.
  


Pré-requis :

- Un compte/acces Github
- Un compte/acces CircleCi
- Un Compte/acces DockerHub
- Un Compte/Acces Heroku
- Un Compte/Acces Sentry


### Github:

Un compte est necéssaire pour y cloner le projet et lier le repository à CircleCi

### CircleCi:

Une fois connecté à votre compte CircleCI, dans le menu "projets" connectez vous sur votre repository à l'aide de "Set Up Project".
Le projet possedant déja un fichier de configuration dans ".circleci/config.yml" il vous sera alors demandé si vous souhaitez l'utiliser.
Confirmez son utilisation.

Une fois sur la page de gestion de votre projet sur CircleCI, utilisez le bouton "Project Settings" à droite, puis "Environment Variables" à gauche. 

Entrez les variables suivantes :

- DOCKER_LOGIN (correspond à votre username sur DockerHub)
- DOCKER_PASSWORD (correspond à votre Token acces sur DockerHub)
- HEROKU_API_KEY (API Key récupérée sur votre compte Heroku)
- SENTRY_DSN (DSN de votre projet Sentry)


### DockerHub:
Création d'un dépot dans Docker Hub
### Heroku:
Création d'une application dans Heroku nomée:
- oc ...
Configuration des variable d'environnements ( settings/conf Vars):
- ENV PRODUCTION (correspond au changement de parametre de l'environnement local vers environnement de production)
- SECRET_KEY (Clé secret de l'application Django lors du passage en production)
- SENTRY_DSN (DSN de votre projet Sentry)
### Sentry:
La surveillance de l'application se fera via sentry.
Une fois le compte crée, vous générez alors une "Issues" ZeroDivisionError dans sentry.


Une fois les differents comptes crées et parametrés,
Realiser une modification sur un fichier de l'application de la branche master et poussez cette modification sur le github.

Les test de verification se declencherons.
Si les tests passe , la contenerisation et le deploiement s'effectuerons.










