# 🔌Test 2 Electronique : Boite Noire

## 🎯 Objectifs du projet

**Objectifs généraux:** 

- Concevoir une boite capable de collecter et de transmettre les données de vitesse et de position du capteur MPU6050 ;

- Créer une station de contrôle qui reçoit et affiche les données provenant de la boite  

**Objectifs spécifiques:**

- Réaliser des schémas électronique avec KICAD utilisant directement des ATMega328p;
- Designer les PCB pour ensuite les produire.
- Fabriquer votre propre alimentation électrique pour alimenter le circuit qui ne devra pas être incluse dans la boîte.
- Fabriquer un cube de 7 cm d'arrêt pour représenter la boîte noire. La face supérieure du cube devra être ouverte si elle est faite dans un matériau opaque afin de permettre de voir le circuit à l'intérieur.
- Créer un bus I2C dont le seul maître sera le microcontrôleur à l'intérieur du cube. Le capteur (dans le cube) et le microcontrôleur (au niveau de la station de contrôle) devront être les esclaves sur le bus. L'écran LCD doit être branché en mode 4 bits.
- Produire une vidéo dans laquelle on verra bouger le cube dans toutes les directions et les informations sur l'écran LCD.

# **1. Introduction**

Lors du premier test, nous avons découvert un capteur particulier alliant les fonctionnalités d’un gyroscope et d’un accéléromètre, dont l’usage nous a permis de déterminer le sens de déplacement et l’accélération de notre robot collecteur de déchets en mouvement. Cette fois-ci (pour le test 2), nous nous sommes proposés de déterminer des informations plus pertinentes et significatives que les précédentes. Il s’agit de la vitesse de déplacement et de la position spatiale. Ces valeurs, en raison de leur importance, seront collectées et enregistrées dans une boîte noire, puis affichées sur une station de contrôle, le tout alimenté par l’alimentation.

# **2. Architecture du système**

Notre système qui se forme de trois sous-systèmes principaux qui:

- la Boite Noire
- la Station de contrôle
- l’Alimentation

Il est important de préciser que le composant qui est le cœur même du système est le **microcontrôleur  ATEMega328p**.

### **Présentation de l’ATMega 328p**

L’ATMega 328p est un microcontrôleur 8 bits de la famille AVR(Advanced Virtual RISC) développé par Microship qui est beaucoup utilisé dans la réalisation de projets embarqués ou juste dans l’apprentissage. Il intègre la technologie picoPower qui offre une consommation ultra faible et des modes de veille à faible consommation idéal pour les applications alimentées par batterie . C’est la version standard mais il en existe une version plus puissante ,le Atmega328 PB et qui est moins compatible avec Arduino mais qui dispose aussi d’un cœur AVR 8 bits .

![atmega_328p.png](./assets/test-two/atmega_328p.png)

**Schéma d’un** ATMega **328p**

Ici pour notre projet , nous utiliserons un ATMega 328p-PU(voir image ci-dessus ). C’est le même microcontrôleur , mais dans un boîtier DIP-28 traversant , idéal pour les breadboards et cartes Arduino .Ce boitier dispose de 28 broches traversantes qui assurent sa connexion aux éléments du circuit. Il peut être programmé en C ou via l’environnement Arduino. Ce composant sera donc le cœur de notre circuit et va permettre la liaison entre les différents éléments du circuit .

Son architecture est la suivante :

![atmega_328p-UP.png](./assets/test-two/atmega_328p-UP.png)

**Schéma de l’architecture d’un ATMega328p**

**Résumé des broches de l’ATMega 328p et leurs fonctions**

| Broches | Fonction |
| --- | --- |
| GND | Masse |
| VCC | Alimentation de tous l’ATMega en dehors des broches d’entrées analogiques |
| AVCC | Alimentation des broches analogiques |
| AREF | Reference de tensions pour les conversions analogiques |
| XTAL1,XTAL2 | Horloge externe |
| RESET | Réinitialisation |
| PD0(RX),PD1(TX) | UART (série) |
| PB3,PB4,PB5,PB2 | SPI |
| PC4(SDA),PC5(SCL) | I2C |
| PC0 à PC5 | ADC(entrée analogique) |
| PD3,PD5,PD6,PB1,PB2,PB3 | PWM |

Pour l’utiliser directement(sans carte Arduino) dans notre circuit , on utilisera les composants suivants:

- un **quartz de 16MHz** entre les broches **XTAL1** et **XTAL2m** qui nous servira d’oscillateur externe;

![quartz.png](./assets/test-two/quartz.png)

**📌** Utilité : fournit un signal d’horloge **très stable** et **précis** grâce à la vibration de son cristal à une fréquence spécifique (par exemple, 16 MHz).

| **Utilité du quartz** | **Détail** |
| --- | --- |
| **Cadencer les instructions** | Le quartz fixe la vitesse à laquelle les instructions sont exécutées. |
| **Précision temporelle** | Pour que les temporisations (ex : delay(), millis()) soient exactes.
 |
| **Communication fiable** | Pour que les protocoles comme UART, SPI, I2C fonctionnent correctement. |
| **Stabilité du système** | Un quartz est bien plus stable que les oscillateurs internes. |

- deux **condensateurs de 22pF**, un entre chaque broche du quartz et la masse GND ;
    
    ![condensateur_22pF.png](./assets/test-two/condensateur_22pF.png)
    

**📌** Utilité: stabilise le quartz.

- **Résistance de 10 kΩ** sur la broche **RESET**;

 

![resistance_10k.png](./assets/test-two/resistance_10k.png)

**📌** Utilité : Maintient la broche **RESET** à l'état **haut** (HIGH) pour éviter les redémarrages intempestifs.

- **Condensateur de 100 nF (0.1 µF) entre VCC et GND (découplage)**

![condensateur_100nF.png](./assets/test-two/condensateur_100nF.png)

**📌** Utilité: Supprime les **bruits** et **pics de tension** sur l’alimentation du microcontrôleur.

Plus clairement, sans lui dans le circuit, il peut y avoir des comportements aléatoires (bugs, plantages) lors d’une charge soudaine (ex: allumage LED, envoi UART).

- **Bouton poussoir**

![bouton_poussoir.png](./assets/test-two/bouton_poussoir.png)

**📌** Utilité: réinitialiser l’ATMega lorsqu’un problème lié au code survient

## 📦Présentation de la Boite Noire

La Boite Noire est le sous système chargée de collecter, d’enregistrer, et d’envoyer les données provenant du capteur MPU 6050 à la station de contrôle.

### *🛠️**Matériel***

- ATMega328p
- MPU6050

![MPU6050.png](./assets/test-two/MPU6050.png)

**📌** Utilité:  permet de déterminer la vitesse de déplacement et la position suivant chaque axe(X,Y,Z)

- LEDs

![LEDs.png](./assets/test-two/LEDs.png)

**📌** Utilité:  Pour signifier que la boite est effectivement alimentée.

- **Resistance de 220Ω**

![resistance_220.png](./assets/test-two/resistance_220.png)

**📌** Utilité: protéger la LED 

### 🔧🔋📟 ***Montage***

**Présentation du schéma du circuit Kicad du 1er PCB**
Pour notre  1er circuit, le microprocesseur ATMega en sera le cœur.  C’est à lui que seront reliés les différents composants du circuit et il va servir de maître.
Notre microprocesseur ne disposant pas directement d’un oscillateur interne, il a fallu faire un circuit d’oscillation externe composé de quartz et deux condensateurs de 22pF. Les broches de notre quartz sont également reliées aux broches XTAL1 et XTAL2 de notre microprocesseur. Afin de simplifier au maximum la compréhension de notre schéma, des labels XTAL1 et XTAL 2 ont été créés et utilisés.
Les **labels** sont des **connexions sans fils** qui relient un composant à un autre composant sur le schéma du circuit. L’onglet de création de label est disponible sur la bande verticale droite de notre environnement Kicad. C’est d’ailleurs ce qui est va être privilégié dans  tout notre schéma par rapport aux fils de connexion classiques.

![kicad_1er_PCB.png](./assets/test-two/kicad_1er_PCB.png)

**Schéma du circuit d’oscillation**

**-**Après il a fallu câbler le circuit de reset qui va nous permettre de réinitialiser notre ATMega en cas de problème avec notre code. Pour le faire, on a utilisé un bouton poussoir qui va nous servir de bouton « reset » qui sera connecté à une résistance de 10k et un condensateur de 100nF, tout ça pour veiller à la sécurité de notre circuit et à la dissipation de la chaleur. Cet ensemble est connecté au label Reset qui est quant à lui connecté à la broche RESET de notre ATMega , toujours dans la perspective d’éviter au maximum les fils de connexion classiques dans notre schéma.

![circuit_d'oscillation.png](./assets/test-two/circuit_d_oscillation.png)

**Schéma du circuit de Reset**

**-**Une LED d’Etat associée à une résistance sera également utilisée pour permettre en quelque sorte de notifier si notre circuit est parcouru par un courant comme avec l’arduino. Elle a été mise sur la broche D7 de notre microprocesseur.

![circuit_reset.png](./assets/test-two/circuit_reset.png)

**Schéma du câblage de la LED d’état**

-En ce qui concerne la broche d’alimentation de l’ATMega, le bus I2C ainsi que le capteur MPU-6050, le choix a été porté sur l’utilisation respective d’un connecteur 2 pin, d’un connecteur 4 pin ainsi que d’un connecteur 8 pin que nous avons  renommé avec les noms de broches correspondants avec l’éditeur de symbole disponible dans la section outils du menu Kicad. Ces différents circuits ont été réalisés avec l’ajout de résistances de 4.7 kΩ sur les broches SDA et SCL. Des labels  SDA et SCL ont été créés, toujours dans l’optique d’une compréhension facile de notre circuit.

![LED_d'etat.png](./assets/test-two/LED_d_etat.png)

**Schéma du circuit du 1er PCB**

-Il est important de noter que les broches VCC et GND de nos différents circuits sont connectés à toutes  les autres broches du même nom sur le schéma.
C’est une caractéristique intrinsèque au logiciel Kicad.
🧐L’exécution du contrôle des règles électriques affiche le message suivant :

![circuit_1er_PCB.png](./assets/test-two/circuit_1er_PCB.png)

En voyant l’inscription 0 erreurs , l’équipe s’était dit que le travail était fait (😏)et qu’elle  pouvait déjà passer au PCB en ignorant les avertissements du logiciel mais ce fut une grossière erreur de notre part.

Après les empreintes  des différents composants ont été assignées dont le récapitulatif se trouve sur l’image suivante :

![differents_composants.png](./assets/test-two/differents_composants.png)

😮Mais lors du passage au PCB, on a obtenu le message suivant :

![passage_PCB.png](./assets/test-two/passage_PCB.png)

On a obtenu **12 erreurs** lors de la **génération de notre PCB** et c’est après une lecture profonde qu’on s’est rendus compte que quand on renommait les connecteurs, ils n’étaient pas directement inclus dans la bibliothèque de composants de Kicad. C’était comme si on créait un élément et qu’on l’incluait dans la bibliothèque de Kicad, ce que l’on ne pouvait pas faire. En gros, les connecteurs n’étaient pas reconnus par le logiciel, ce qui entraînait leur non connexion aux différents éléments sur le PCB. Trois options s’offraient donc à nous :

- Soit on créait nos propres connecteurs que l’on allait inclure dans une bibliothèque que l’on aurait nous-même crée ;
- Soit on cherchait si ces connecteurs étaient disponibles dans des bibliothèques en ligne ;
- Ou soit on utilisait simplement les symboles d’origine non renommés disponibles dans le logiciel Kicad.

Notre choix s’est donc porté sur la 3ème option et après reprise du schéma on a obtenu le schéma final suivant :

![schema_final_circuit_1er_PCB.png](./assets/test-two/schema_final_circuit_1er_PCB.png)

**Schéma final du circuit du 1er PCB**
::: warning
Il est important de notifier que les broches non utilisées de l’ATMega ont été notifiées au logiciel grâce à des **marqueurs de non connexion** sinon on aurait eu des erreurs inutiles par rapport à ces broches. Par ailleurs les différents circuits ont été mis dans des cadres précis et nommés, toujours pour permettre aux lecteurs une compréhension totale de notre circuit.
:::

L’exécution du contrôle des règles électriques sur ce schéma a permis l’obtention de 0 erreurs ainsi que 0 avertissements comme souhaité(😏). Le même résultat a été observé lors de ma mise à jour du PCB  depuis notre schéma.

![actualisation_PCB.png](./assets/test-two/actualisation_PCB.png)

Après actualisation du PCB à partir de notre schéma, on obtenait un 1er PCB  où tous les éléments étaient collés l’un à l’autre et les fils se chevauchaient.

![1er_PCB_obtenu.png](./assets/test-two/1er_PCB_obtenu.png)

On voit clairement sur cette image comment les différents composants étaient mélangés et comment les fils s’entrecoupaient. 

Ce n’est qu’après **des heures de réorganisation** de tout ce schéma, de reprise et des tonnes d’erreurs qu’on a  obtenu notre PCB final :
![PCB_final.png](./assets/test-two/PCB_final.png)

**Schéma du PCB final de la Boite Noire**

**Vue 3D du PCB final de la Boite Noire**:

<iframe src="https://player.vimeo.com/video/1094747497" width="640" height="360" frameborder="0" allowfullscreen></iframe>

**Dimensions**  :

- 6cmx 6,5cm (taille)
- 0.5mm (0001969 in)
- Grille : 2. 5 mm
- 0.05 mm : épaisseur de la ligne de contour
- 1.6 mm : épaisseur de tout le PCB

### ***Résultat final***

**Image physique de la Boite Noire**

## **🖥️Présentation de la station de contrôle**

La station de contrôle est un système qui permettra de suivre en temps réel notre robot à travers la connaissance de sa vitesse et de sa position.

### *🛠️**Matériel***

- ATMega328p
- Ecran LCD

![ecran_LCD.png](./assets/test-two/ecran_LCD.png)

**📌** Utilité:  Afficher les valeurs de position et de vitesses du provenant du capteur 

### 🔧🔋📟 ***Montage***

**Présentation du circuit KiCad du PCB de la station contrôle**

En ce qui concerne le schéma du circuit de la station de contrôle, on a également utilisé un ATMega 328p auquel on a associé le circuit de Reset, le circuit d’oscillation, le circuit de la LED d’alimentation. 

Pour notre écran LCD I2C, on a choisi d’utiliser un connecteur 16 pin qu’on a câblé selon le modèle suivant :

| **LCD Pin** | **Fonction** | **Broche Arduino (Digital)** | **Port ATmega328P** | **Broche physique ATmega328P** |
| --- | --- | --- | --- | --- |
| 1 | GND | - | - | -GND |
| 2 | VCC (5V) | - | - | -VCC |
| 3 | Vo (contraste) | - | - | -Potentiomètre |
| 4 | RS | D12 | PB4 | 18 |
| 5 | RW | GND | -GND | -GND |
| 6 | E | D11 | PB3 | 17 |
| 11 | D4 | D5 | PD5 | 11 |
| 12 | D5 | D4 | PD4 | 6 |
| 13 | D6 | D3 | PD3 | 5 |
| 14 | D7 | D2 | PD2 | 4 |
| 15 | A (LED+) | VCC (via résistance 220Ω) | - | -GND |
| 16 | K (LED-) | GND | - | -GND |

<aside>
💡

Utiliser le lien suivant pour pouvoir accéder au schéma du mappage des PINS  e l’Arduino et ceux de l’ATMega328p:

[ATmega168/328P-Arduino Pin Mapping | Arduino Documentation](https://docs.arduino.cc/retired/hacking/hardware/PinMapping168/?_gl=1*g2i1pw*_up*MQ..*_ga*ODEwNDU0ODE4LjE3NTAzMjM1OTg.*_ga_NEXN8H46L5*czE3NTAzMjM1OTYkbzEkZzEkdDE3NTAzMjM2MDYkajUwJGwwJGgxNjQ3NjY2NjEw)

</aside>

![mappage_PINS.png](./assets/test-two/mappage_PINS.png)

**Schéma du montage de la station de contrôle**

Ayant retenu la leçon du montage précédent, on a compris qu’il serait inutile de renommer les broches de notre écran dans notre schéma donc on l’a laissé sous la forme disponible dans le logiciel Kicad. Ce qui nous a conduits à **0 erreurs et 0 avertissements (😏)** lors de l’exécution du contrôle des règles électriques.

Cela nous a permis de générer le PCB et c’est aussi après un travail fastidieux qu’on a pû réorganiser les fils pour obtenir le résultat suivant :

![station_controle.png](./assets/test-two/station_controle.png)

**Vue 3D du PCB final:**

<iframe src="https://player.vimeo.com/video/1094748623" width="640" height="360" frameborder="0" allowfullscreen></iframe>

Les dimensions de ce PCB sont les mêmes que pour le PCB précédent.

### ***Résultat final***

## **🔌Présentation de l’alimentation**

### *🛠️**Matériel***

- **Batterie au mercure de 8V**

![batterie_mercure_8V.jpeg](./assets/test-two/batterie_mercure_8V.jpeg)

**📌** Utilité: source de tension

- **Coupleur**

**📌** Utilité: associer les batteries en série pour avoir en sortie une tension qui est la somme des tensions

- Régulateur non linéaire de type abaisseur (Buck)(**XL4015**)

![regulateur_XL4015.jpeg](./assets/test-two/regulateur_XL4015.png)

**📌** Utilité: conversion de la tension fournie par la source en une tension plus stable(5V adaptée pour l’ATMega328p

- **Diode Zener de 5V**

**📌** Utilité: protéger au cas où il y a surtension 

- **Résistance de 1K**

**📌** Utilité: protéger au cas où il y a surtension

### 🔧🔋📟 ***Montage***

Notre alimentation est une source comme par exemple une batterie à laquelle on a ajouté un régulateur de tension pour maintenir la sortie constante.

**Connexions à l’intérieur du système** 

Comme point de départ ,nous allons utiliser comme source de tension, 02 batteries au mercure d’environ 8 V chacune que nous allons assembler avec un coupleur, soit un total de 16V environ.

Par rapport au **régulateur non linéaire**, il est connecté directement à la source pour effectuer la conversion de la tension fournie en entrée par cette dernière en une tension plus stable, constante de 5V pour alimenter les ATMega des autres sous systèmes. Plus précisément nous faisons usage d’un **XL4015** qui est un modèle très particulier capable de prendre entre 3 et 32 volts et de restituer entre 1.5 et 35 volts(ajustable) de tension en sortie.

 La **diode Zener** et la **résistance,** quant à elles,  sont câblées entre la **sortie** et le **régulateur,** de sorte que l'alimentation du circuit soit coupée dès que la tension va au-delà de 5V. 

Voici une complète de notre alimentation.

**Schéma KiCad de l'alimentation sur KICAD**

![alimentation_kicad.png](./assets/test-two/alimentation_kicad.png)

### ***Résultat final***

**Image physique de l’alimentation**

![alimentation_physique.jpeg](./assets/test-two/alimentation_physique.jpeg)

## ⚒️Montage final

- **Connexions entre les sous systèmes**
    
    De tout ce qui précède, on comprend que le système entier est l’ensemble formé de la boite noire (Premier PCB) , de la station de contrôle (second PCB)  et de l’alimentation. 
    
    - La Boite Noire et la station de contrôle communiquent via un bus I2C qui est représenté physiquement par un connecteur 4pin avec des résistances  4.7kOhm sur les SDA et SCL.
    - L’alimentation sert de source directe (sans intermédiaire) à la Boite Noire et la station de Contrôle via un connecteur 2pin placé sur la source.

- **Rendu final physique du système complet**

- **Difficultés rencontrées et solutions apportées**

# 3. Code

<aside>
💡

Pour le code, nous avons eu, dans un premier temps, à créer un bus I2C pour la communication entre l’ATMega de la boite Noire et l’ATMega de la station de contrôle et dans un second temps, à câbler l’écran LCD en mode 4 bits avec l’ATMega secondaire.

</aside>

## 🚌Création du bus I2C

## **🧐C’est quoi l’I2C?**

L’I2C (prononcé **"I deux C"** ou **"I-squared-C"**) signifie **Inter-Integrated Circuit**. C’est un **protocole de communication série** inventé par Philips (aujourd’hui NXP) pour permettre à plusieurs circuits intégrés (CI) de communiquer entre eux avec **seulement deux fils**.

---

### 🔧 **Principes de base de l’I2C**

- **Nombre de fils :** 2
    - **SDA (Serial Data Line)** : ligne de données
    - **SCL (Serial Clock Line)** : ligne d’horloge
- **Architecture :**
    - Un **maître (master)** contrôle la communication.
    - Un ou plusieurs **esclaves (slaves)** répondent.
    - **Un seul maître**, **plusieurs esclaves** possibles sur le même bus.

---

### 🧠 **Fonctionnement général**

1. Le **maître envoie un signal d’horloge (SCL)** et contrôle le moment où les données (SDA) sont envoyées ou lues.
2. Chaque esclave a une **adresse unique** (ex : 0x68 pour un MPU6050).
3. Le maître commence par envoyer une **adresse d’esclave**, puis des **ordres** ou des **demandes de lecture**.
4. L’esclave répond si l’adresse reçue correspond à la sienne.

---

<aside>
💡

**A partir de cette explication suffisamment claire de l’I2C et de la compréhension du contexte du test 2, le bus I2C  qu’on doit créer à pour maître: l’ATMega de la boite Noire et pour esclaves: le capteur MPU6050 et l’ATMega de la station de contrôle.**

</aside>

**Explication du code du maître** 

### ⚙️ **1. ATMega maître (le principal)**

📌 **Fonction :**

- Lit les données du **capteur MPU6050** (avec DMP) via I2C.
    
    📌 A noter :
    
    Le DMP (Digital Motion Processor) est un **processeur embarqué** à l’intérieur de certains capteurs comme le **MPU6050** (gyroscope + accéléromètre). Il est intégré pour **traiter les données brutes directement dans le capteur**, **sans trop solliciter le microcontrôleur (Arduino, etc.)**.
    
    ---
    
    ### Ce que le DMP fait :
    
    ✅ **Filtrage des données**
    
    ✅ **Fusion des capteurs** (accéléromètre + gyroscope)
    
    ✅ **Calcul d’orientation (quaternions, angles d’Euler)**
    
    ✅ **Réduction du bruit et des erreurs dues à la dérive**
    
    ✅ **Calcul automatique de la gravité et orientation**
    
- Calcule : **accélération réelle**, **vitesse**, **position**
- Transmet ces données (6 `float`, soit 24 octets) via **I2C** à l’esclave

### Code

```cpp
/*Inclusion des bibliothèques nécéssaires*/
#include <Wire.h>
#include "I2Cdev.h"
#include "MPU6050_6Axis_MotionApps20.h"

/*Adresse de l'esclave*/
#define SLAVE_ADDR 0x08

/* Création d’un objet de la classe MPU6050 */
MPU6050 mpu;

/* Variables liées au DMP (Digital Motion Processor) */
bool dmpReady = false;            // Drapeau indiquant si le DMP est initialisé 
uint8_t devStatus;                // Code de retour de l'initialisation du DMP
uint16_t packetSize;              // Taille attendue des paquets FIFO DMP 
uint16_t fifoCount;               // Nombre de bytes actuellement dans le FIFO 
uint8_t fifoBuffer[64];           // Tampon de lecture des données DMP 

/* Accélérations et gravité */
VectorInt16 accelerationBrut;     // Accélération brute (avec gravité)
VectorInt16 accelerationReel;     // Accélération réelle (sans gravité)
VectorInt16 accelerationMonde;     //Accélération dans le repere terrestre
VectorFloat gravity;              // Vecteur gravité calculé à partir du quaternion

Quaternion q;                     // Quaternion représentant l’orientation absolue

float accelerationX, accelerationY, accelerationZ; // acceleration sans gravite (dans le repere monde)
float vitesseX = 0, vitesseY = 0, vitesseZ = 0; // vitesse en m/s
float positionX = 0, positionY = 0, positionZ = 0; // position en m

const float constAccelGravit = 9.81;
const float sensibiliteAccel = 16384.0;

unsigned long lastTime = 0;

void setup() {
  /*Initialisation de la communication serie */
  Serial.begin(9600);

  /*Initialisation du bus I2C en mode maitre */
  Wire.begin();

  /*Pause pour stabiliser le bus et les periphériques */
  delay(1000);

  /*Initialisation du MPU6050 */
  mpu.initialize();

  /* Verification de la connexion I2C avec le capteur MPU */
  while(!mpu.testConnection()) 
  {
  Wire.beginTransmission(SLAVE_ADDR);
  Wire.write("ERRMPU");  // 6 caractères = 6 octets
  Wire.endTransmission();
  }

  
  devStatus = mpu.dmpInitialize();//Initialisation du DMP

  /* Verification de l'initialisation du DMP */
  while(devstatus!=0) 
  {
  Wire.beginTransmission(SLAVE_ADDR);
  Wire.write("ERRDMP");  // 6 caractères = 6 octets
  Wire.endTransmission();
  }
  
  /*Activation du DMP */
  mpu.setDMPEnabled(true);

  /* DMP est prêt */ 
  dmpReady = true;

  /*Récuperation de la taille des paquets de données générés par le DMP */
  packetSize = mpu.dmpGetFIFOPacketSize();

  lastTime = millis();
}

void loop() {
  if (!dmpReady) return; //arrêt de la boucle si le DMP n'est pas prêt 

  fifoCount = mpu.getFIFOCount();//taille actuelle des données dans la FIFO
  
  /*Arrêt de la boucle si le FIFO ne contient pas de packets complets */
  if (fifoCount < packetSize) return;

  mpu.getFIFOBytes(fifoBuffer, packetSize);//Lecture d'un paquet complet

   /*Calcul de la gravite */
  mpu.dmpGetGravity(&gravity, &q);

  /*Determination du vecteur accélération brute dans le repere du capteur  */
  mpu.dmpGetAccel(&accelerationBrut, fifoBuffer);
  
  /*Obtention de l'acceleration sans la gravité dans le repere du capteur */
  mpu.dmpGetLinearAccel(&accelerationReel, &accelerationBrut, &gravity);

  /*Determination du vecteur acceleration dans le monde reelle(repere fixe)  */
  mpu.dmpGetLinearAccelInWorld(&accelerationMonde, &accelerationReel, &q);

  /*Conversion des donnees brutes d'acceleration en valeurs physiques reelles */
  accelerationX = accelerationMonde.x / sensibiliteAccel * constAccelGravit;
  accelerationY = accelerationMonde.y / sensibiliteAccel * constAccelGravit;
  accelerationZ = accelerationMonde.z / sensibiliteAccel * constAccelGravit;

  unsigned long now = millis();
  float dt = (now - lastTime) / 1000.0;
  lastTime = now;

  /*Integration de l'accélération pour obtention de la vitesse */
  vitesseX += accelerationX * dt;
  vitesseY += accelerationY * dt;
  vitesseZ += accelerationZ * dt;

  /*Integration de la vitesse pour obtention de la position */
  positionX += vitesseX * dt;
  positionY += vitesseY * dt;
  positionZ += vitesseZ * dt;

/*Envoie des donnees de position et de vitesses (dans cet ordre) à l'esclave à travers son adresse */
  Wire.beginTransmission(SLAVE_ADDR);
  Wire.write((byte *)&positionX, 4);
  Wire.write((byte *)&positionY, 4);
  Wire.write((byte *)&positionZ, 4);

  Wire.write((byte *)&vitesseX, 4);
  Wire.write((byte *)&vitesseY, 4);
  Wire.write((byte *)&vitesseZ, 4);
  Wire.endTransmission();

  delay(50);
}

```

### ⚙️ **2. ATMega esclave (le secondaire)**

📌 **Fonction :**

- Reçoit les données envoyées par le maître
- Affiche **position (X, Y)** et **vitesse (X, Y)** sur un **écran LCD 16x2 en mode 4 bits**

**Code**

```cpp
#include <Wire.h> //communication I2C
#include <LiquidCrystal.h> //pour contrôler un écran LCD en mode parallèle 4 bits

// LCD en mode 4 bits : RS, E, D4, D5, D6, D7
LiquidCrystal lcd(12,11, 5, 4, 3, 2);

// Données reçues
float px = 0, py = 0, pz = 0;
float vx = 0, vy = 0, vz = 0;

void setup() {

  /*Configure l’écran comme LCD 16 colonnes × 2 lignes */
  lcd.begin(16, 2);

  lcd.print("Esclave pret");

  /*Initialistion de la communication en mode esclave avec l'adresse 0x08*/
  Wire.begin(0x08);

  /*Définition de la fonction recevoir() comme handler à appeler quand le maître envoie des données I2C */
  Wire.onReceive(recevoir);
}

void loop() {

  /*Affichage de la position sur la premiere ligne de l'ecran LCD */
  lcd.setCursor(0, 0);

  lcd.print("Pos:");
  lcd.print(px, 1);
  lcd.print(":");
  lcd.print(py, 1);
  lcd.print(":");
  lcd.print(pz,1);

  /*Affichage de la vitesse sur la 2e ligne de l'ecran */
  lcd.setCursor(0, 1);
  lcd.print("Vit:");
  lcd.print(vx, 1);
  lcd.print(":");
  lcd.print(vy, 1);
  lcd.print(":");
  lcd.print(vz, 1);
  delay(500);

   /*Nettoyage de l'ecran */
  lcd.clear();
}

/*Fonction de reception des donnees provenant du maître */
void recevoir(int n) 
{
  if (n == 6) 
  { // Un message d'erreur de 6 caractères
    char msg[7] = {0}; // +1 pour null-terminator
    for (int i = 0; i < 6; i++) {
      msg[i] = Wire.read();
    }

    if (strcmp(msg, "ERRMPU") == 0) {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Erreur capteur:");
      lcd.setCursor(0, 1);
      lcd.print("MPU non detecte");
    }
    else if(strcmp(msg, "ERRDMP") == 0)
    {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Erreur capteur:");
      lcd.setCursor(0, 1);
      lcd.print("DMP INACTIF");
    }
  }

  else if (n >= 24) //Si la taille des données reçues est au moins 24 octets
  {
    /*Lecture des 24e premiers octets reçues dans un tableau */
    byte buffer[24];
    for (int i = 0; i < 24; i++) 
    {
      buffer[i] = Wire.read();
    }

    /*Recuperation de chaque float dans les bonnes variables */
    memcpy(&px, &buffer[0], 4);
    memcpy(&py, &buffer[4], 4);
    memcpy(&pz, &buffer[8], 4);
    memcpy(&vx, &buffer[12], 4);
    memcpy(&vy, &buffer[16], 4);
    memcpy(&vz, &buffer[20], 4);
  }
}

```

# 4. Difficultés

- Difficultés à redisposer les éléments lors de  la génération du PCB
- Conflits avec la bibliothèque Kicad en raison de la modification des noms des connecteurs, ce qui a conduit à une reprise du schéma
- Impossibilité d’impression de notre PCB en raison de la couche manquante, ce qui a conduit à l’utilisation d’un veroboard
- Manque de matériel  lors du montage de notre circuit sur le veroboard
Problèmes de tension avec l’alimentation en raison de l’utilisation de piles qui se déchargent

# 5. Compétences tirées de ce test

- Creation d’un bus I2C
- Design d’un PCB
- Câblage d’un LCD en parallèle (mode 4bits)
- Comprehension de l’utilisation directe d’un ATMega328p avec d’autres sans arduino.

# 6. Annexe
Retrouvez ici les fichiers sources:
- [Lien de téléchargement](https://www.dropbox.com/scl/fi/z5cdrzrg7udv5ojdjnx21/test-02-electro.zip?rlkey=96njyhwtru3y9y58j83gv41en&st=9wv4r3ff&dl=0)
<aside>
💡

### Peace  ✌️

</aside>