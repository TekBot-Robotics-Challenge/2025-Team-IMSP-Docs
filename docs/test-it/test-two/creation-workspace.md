# Création d’un workspace

Dans le cadre de ce **test**, un workspace a été mis en place pour centraliser les fichiers nécessaires à la compilation et à l'exécution des différents packages. Ici, ce workspace a été nommé **`test-02`**.

### Structure d’un workspace ROS2

Un workspace ROS2 est un environnement organisé selon la structure suivante :

- `src/` : répertoire contenant les sources des packages.
- `build/` : contient les fichiers de construction intermédiaires.
- `install/` : regroupe les exécutables et fichiers prêts à l’emploi.
- `log/` : conserve les journaux de compilation.

### Création de la structure de travail

Le dossier principal a été nommé **`test-02`**, puis initialisé comme suit :

```bash

mkdir -p ~/test-02/src
cd ~/test-02
```

Le sous-dossier `src` est essentiel : il accueille les packages ROS2 à compiler.

### Initialisation du workspace avec colcon

Après création de la structure, l’outil `colcon` a été utilisé pour initialiser et compiler l’environnement :

```bash

colcon build
```

Une fois cette commande exécutée, ROS2 génère automatiquement les dossiers `build`, `install` et `log`.

### 4. Configuration de l’environnement

Afin de pouvoir utiliser les éléments du workspace, il est nécessaire de "sourcer" le fichier d’environnement après chaque compilation :

```bash
source install/setup.bash
```

Il est également possible d’automatiser cela à chaque démarrage de terminal :

```bash

echo "source ~/test-02/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

Ce workspace **test-02** a servi de base pour organiser et tester le fonctionnement des nœuds `publisher` et `subscriber` ROS2 implémentés durant le test.