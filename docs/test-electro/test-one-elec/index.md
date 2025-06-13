# Détermination de l'orientation d'un objet à l'aide d'un capteur gyroscope et accéléromètre

## Description sommaire du projet

<p style="display: flex; align-items: center;">
  <span> Les capteurs, composants électroniques permettant de mesurer des grandeurs physiques jouent un rôle prépondérant dans la robotique moderne. Ils permettent aux systèmes robotiques de recueillir des données du monde extérieur leur permettant ainsi de s’adapter à différents types de situations. S’inscrivant dans un contexte de conception d’un bras robotique mobile capable de ramasser puis de trier les déchets, le présent projet vise à permettre l’acquisition des notions d’orientation dans l’espace et de vitesse de rotation angulaire par le futur système robotique. Ce projet a donc pour objectif principal de récupérer puis d’interpréter les valeurs envoyées par un capteur combinant les fonctionnalités de gyroscope et d’accéléromètre : Le MPU 6050. Découvrons - le ensemble !</span>
  
  <img src="./assets/034837.png" style="margin-left:10px; width: 200px">
</p>

## Explication du fonctionnement du Capteur MPU 6050

<p style="display: flex; align-items: center;">
  <span>Le capteur que nous utilisons : Le MPU9250 est en réalité un module de suivi de mouvement à neuf axes dont trois permettent de mesurer l’accélération linéaire sur chacun des axes x,y et z , trois la mesure de la vitesse de rotation angulaire autour de ces axes et trois l’orientation de l’objet dans l’espace (Nord, Sud, etc…). La mesure des accélérations linéaires renseigne sur la direction du mouvement, celle de la vitesse angulaire permet de déduire les angles de rotation respectives par rapport à  deux axes( roulis et tangage) puis le magnétomètre permet de déterminer l’angle de lacet.
  Son fonctionnement se base sur le concept du MEMS (Micro- Electro-Mecanical-System): Il s'agit en réalité de dispositifs miniaturisés qui combinent des composants électriques, mécaniques et parfois optiques sur une seule puce. 
  </span>
    <img src="./assets/065522.png" 
  style="margin-left:10px; width: 200px"/>
</p>

### L'accéléromètre

Afin de mesurer l’accélération linéaire sur un axe, le capteur se sert d’un système électromécanique constitué d’une très fine tige de silicium qui sert de masse sismique en forme de H avec des doigts sensoriels s’étendant à partir d’elle. Cette masse est attaché à un substrat aux deux extrémités et peut se déplacer d’avant en arrière entre les deux extrémités attachées lorsque le capteur est en déplacement. Ce substrat contient également des électrodes fixes qui forment avec les doits sensoriels de la masse sismique une structure en forme de peigne. Ainsi, chaque doigt de la masse sismique forme avec les deux électrodes qui l’entourent deux condensateurs dont la capacité varie lors du mouvement (Etant donné que le mouvement modifie la distance entre les armatures).

<p align="center">
  <img src="./assets/image.jpg" width="400" alt="Image décrivant le fonctionnement interne d'un accélérometre"/>
</p>

Cette différence de capacité est mesurée pour chaque branche de la masse, amplifié, conditionné et filtré avant d’être convertit en donnée numérique grâce à un convertisseur analogique numérique.
Le même procédé est répété pour chaque axe permettant ainsi au capteur de renvoyer les valeurs des accélérations linéaires sur chacun des trois axes.

### Le gyroscope

La mesure de la vitesse de rotation angulaire par le capteur gyroscope quant à elle se base sur l’effet Coriolis qui stipule que tout corps en rotation autour d’un axe avec une certaine vitesse est soumis à une force de direction perpendiculaire à l’axe et à la vitesse. Le déplacement provoqué par cette force permet de déduire la vitesse angulaire appliquée au corps. Afin de reproduire cet effet et déduire la vitesse angulaire à laquelle il tourne, le capteur utilise une structure en forme de fourche combiné à des électrodes, qui en l’absence de rotation effectue un mouvement constant d’avant en arrière maintenue par des cristaux piézoélectriques. Mais dès que la structure est soumise à une rotation, ce mouvement est modifié en raison de force de Coriolis, modification se manifestant par des variations de capacités des condensateurs formés. Ces variations permettent de déduire la vitesse de rotation du capteur. Cette architecture est répétée sur chacun des axes ce qui permet de déduire la vitesse de rotation angulaire suivant chaque axe.

<p align="center">
  <img src="./assets/image1.png" width="700" alt="Image décrivant le fonctionnement interne du gyroscope du MPU 9250">
</p>

Les informations du gyroscope et de l'accéléromètre permettent ainsi d'avoir la direction de déplacement de l'objet dans l'espace mais permettent également d'estimer les angles que font le capteur avec les axes X et Y.

## Architecture du Hardware

### Le système de mesure

- #### Le matériel

- Capteur MPU 9250 (Gyroscope + accéléromètre+ magnétomètre) : Ce capteur a été choisi pour son architecture simple et compréhensible et sa simplicité d’utilisation. De plus, il combine un gyroscope, un accéléromètre et un magnétomètre, une combinaison qui permet de déterminer avec précision l’orientation d’un objet dans l’espace ainsi que sa direction de déplacement.
- Carte Arduino uno : Cette carte a la particularité d’être à la fois facile d’utilisation et assez performant pour notre projet.

- Ecran LCD 20x4 : Ce type d’écran a été choisi car elle est assez grande pour afficher la direction de l’objet et les angles suivant chaque axe.

- Alimentation : 2 piles plates de 9v chacun montés en série pour offrir l’autonomie nécessaire au système.

- Régulateur buck : Afin de maintenir une alimentation stable pour les composants.

NB : Nous reviendrons un peu plus en détail sur l'alimentation.

- #### La logique globale

L’accéléromètre du capteur mesure les accélérations linéaires suivant chaque axe, le gyroscope mesure les vitesses de rotation angulaire suivant chaque axe afin de suivre l’évolution du mouvement puis le magnétomètre permet de connaître les composantes du champ magnétique terrestre.

Ces informations sont ensuite envoyés au microcontrôleur qui les converti en données concrètes puis les envoie sur l’écran LCD pour l’affichage via le bus I2C .

- ### L'Alimentation

Dans le cadre de la réalisation des projets électroniques faisant intervenir des capteurs, nous avons l’habitude d’utiliser notre ordinateur (ports USB) pour l’alimentation. Pour donc se passer d’un PC nous allons concevoir une source d’énergie semblable à celle du port de notre PC (en raison de sa stabilité).
On peut très facilement se demander, si on veut une source d’alimentation de 5V pour notre circuit, pourquoi n’utiliserait-on donc pas une pile simple de 5V ?
Euh, je dirais que oui c’est possible. Mais qu’il vous souvienne, l’une des raisons principales qui justifiait le choix de l’alimentation via le port USB d’un ordinateur est la stabilité de la tension fournie.
Et puisque vous convenez avec moi qu’en pleine utilisation une pile se décharge, la stabilité de la tension fournie n’est donc pas maintenue, ce qui pourrait biaisée les informations renvoyées.
Pour résoudre ce problème d’alimentation on va utiliser certes une source comme par exemple une batterie, mais à cela on va ajouter un régulateur de tension pour maintenir la sortie constante.
Sans plus tarder faisons l’inventaire des composants qui interviendrons dans la réalisation de notre alimentation.

1. Une source de tension : Comme point de départ nous allons utiliser 02 batteries au mercure d’environ 8 V chacune que nous allons assembler avec un coupleur, soit un total de 16V environ. (
   Après réalisation de cette solution, nous avons remarquer que l'arduino décharge rapidement nos batteries. Donc la solution a été de rajouter des batteries monter en parallèle pour l'alimentation.)

<p align="center">
  <img src="./assets/SC20.jpg" alt="Description" width="200">
</p>

1. Un régulateur non linéaire de type abaisseur (buck) pour la conversion de la tension fournie en entrée par la source (les piles), en une tension plus stable, constante de 7V pour alimenter par exemple un Arduino. Plus précisément nous allons faire usage d’un XL4015 qui est model très particulier capable de prendre entre 3 et 32 volts et de restituer entre 1.5 et 35 volts(ajustable) de tension en sortie.

<p align="center">
  <img src="./assets/SC5.jpg" alt="Description" width="500">
</p>

3. Une diode zener et une résistance :
   La diode zener et la résistance sont là comme protection. Au cas où, suite à une mauvaise manipulation, la tension va au-delà de 7V, l'alimentation du circuit est coupée. Donc, une diode zener de 7V qui a été dimensionné et une résistance de 1K.

Voici une complète de notre alimentation.

 <p align="center">
  <img src="./assets/SC9.jpg" width="700" alt="Image de l'alimentation sur KICAD">
</p>

<p align="center">
  <img src="./assets/SC14.jpg" width="500" alt="Image physique de l'alimentation">
</p>

Dans le cadre du concours, cette source d’alimentation aura deux sorties. L'un réglé sur du 7V permettant ainsi d’alimenter efficacement notre carte arduino, et l'autre sur du 5V pour des utilisations futures.

### - Les schémas électroniques

Pour le câblage, le microprocesseur arduino sera utilisé comme source d’alimentation de l’écran LCD et du capteur MPU-6050z.
Etant donné que dans Kicad l'écran lcd ne dispose pas directement du module de communication I2C, on lui associera un module de communication I2C appelé le PCF8574. C’est une petite puce qui te permet d’ajouter des broches numériques supplémentaires à ton microcontrôleur (Arduino, ESP32...) en utilisant juste 2 fils : SDA et SCL. Il possède 15 broches dont la liaison avec l’écran LCD est la suivante :

| Broche du PCF8574 | Broche du LCD | Nom             | Fonction                            |
| ----------------- | ------------- | --------------- | ----------------------------------- |
| P0                | D4            | Data 4          | Données (bit 4) envoyé vers l’écran |
| P1                | D5            | Data 5          | Données (bit 5) envoyé vers l’écran |
| P2                | D6            | Data 6          | Données (bit 6) envoyé vers l’écran |
| P3                | D7            | Data 7          | Données (bit 7) envoyé vers l’écran |
| P4                | E             | Enable          | Validation de l’envoi des données   |
| P5                | RW            | Read/Write      | Lecture/Ecriture                    |
| P6                | RS            | Register select | Sélection du registre               |

P7 |LED +Blacklight | Control Rétroéclairage Contrôle du rétroéclairage
GND |K, VSS Masse | Fermeture du circuit

Les broches restantes n’étant connectées à rien, on utilisera des marqueurs indicateurs de la non-connexion pour faire comprendre au logiciel Kicad que ces broches sont non-utilisées sinon on risque d’avoir une dizaine d’erreurs lors du contrôle des règles électriques (ERC).
Il est important de noter que l’écran LCD que nous utiliserons dispose du module PCF 8574 directement soudé à l’arrière et laissant uniquement 4 broches visibles, les autres étant directement connectées à l’écran.
Il s’agit des broches :
• VCC pour permettre l’alimentation de l’écran,
• GND qui désigne la masse ou borne négative de l’écran,
• SDA désignant la ligne de données de la communication I2C,
• SCL désignant la ligne d’horloge qui synchronise l’envoi des données I2C.

Ces 4 broches seront directement connectées à leurs équivalents respectifs du même nom sur le microprocesseur Arduino.

 <p align="center">
  <img src="./assets/SC7.jpg" width="700" alt="Image de l'écran lcd sur KICAD">
</p>

<p align="center">
  <img src="./assets/SC8.jpg" width="400" alt="Image du PCF sur KICAD">
</p>

Le capteur MPU-6050 quant à lui a 8 broches ayant des fonctions précises qui sont recensées dans le tableau ci-dessous :
Nom de la broche | Fonction
---------------- | ---------
VCC | Alimentation
GND | Masse commune
SCL | Horloge de communication I2C
SDA | Données de communication I2C
INT | Sortie interruption
AD0 | Sélection de l’adresse I2C
XCL | Horloge externe
XDA | Données externes

Ce capteur, tout comme l’écran LCD sera câblé en mode I2C, c’est-à-dire avec les broches VCC, GND, SDA et SCL directement avec l’arduino. Les 4 autres restantes n’étant connectées à rien, on y disposera des marqueurs de non connexion .Pour notre schéma, nous utiliserons directement un connecteur 01x08 pin que nous avons renommé avec le nom des broches d’un MPU 6050 étant donné que sa représentation dans Kicad ne dispose pas directement des broches pour la communication par I2C. L’utilisation d’un tel connecteur pour également aider si on a éventuellement besoin de designer le PCB à partir du schéma du circuit.

<p align="center">
  <img src="./assets/SC17.jpg" width="500" alt="Image du capteur MPU 6050 sur KICAD">
</p>

<p align="center">
  <img src="./assets/SC19.jpg" width="500" alt="Schema complete du circuit du capteur sur KICAD">
</p>

## Processus des differents montages

### Le capteur

1. Connection du capteur à l'arduino suivant le protocole de communication I2C.

<p align="center">
  <img src="./assets/SC2.jpg" alt="Description" width="500">
</p>

2. Ajout de l'écran Lcd

<p align="center">
  <img src="./assets/SC4.jpg" alt="Description" width="500">
</p>

3. Montage final

<p align="center">
  <img src="./assets/SC3.jpg" alt="Description" width="500">
</p>

### L'alimentation

1. Disposition des régulateurs , des diodes et des résistances

<p align="center">
  <img src="./assets/SC11.jpg" alt="Description" width="500">
</p>

2. Le soudage

<p align="center">
  <img src="./assets/SC12.jpg" alt="Description" width="500">
</p>

<p align="center">
  <img src="./assets/SC13.jpg" alt="Description" width="500">
</p>

3. Le montage final

<p align="center">
  <img src="./assets/SC14.jpg" alt="Description" width="500">
</p>

## Le code

```C++
//Code capteur MPU_filtre
#include <Wire.h>
#include <MPU6050.h>
#include <LiquidCrystal_I2C.h>

/* on crée l’objet LCD et on définit les Pins utilisés */
LiquidCrystal_I2C lcd(39,16,2);

/* creation d'un objet de la classe MPU6050 */
MPU6050 mpu;

const float SEUIL = 0.1;
int16_t accelerationX, accelerationY, accelerationZ;
int16_t vitesseRotationX, vitesseRotationY, vitesseRotationZ;

void setup() {
  /* Initialisation de la communication série */
  Serial.begin(115200);

  /* Initialisation de la communication par le bus I2C */
  Wire.begin();

/* initialisation de l'ecran LCD */
  lcd.init();

/* Allumage du retroeclairage de l'ecran */
  lcd.backlight();


  mpu.initialize();

/*verifie si la liaison I2C est bien etablie */
lcd.setCursor(0,0);
  while(!mpu.testConnection())
    lcd.print("MPU6050connectionfailed");


}

void loop() {
  /* 1. Lire les données du capteur (acceleration et vitesse angulaire suivant chaque axe) */
  mpu.getMotion6(&accelerationX, &accelerationY, &accelerationZ, &vitesseRotationX, &vitesseRotationY, &vitesseRotationZ);

float sensibilteAccel=16384.0;
float sensibilteGyro=131.0;

  /* 2. Convertir les valeurs (valeurs brutes de sorties en valeurs physiques reelles) */
  float accelX = accelerationX / sensibilteAccel;
  float accelY = accelerationY / sensibilteAccel;
  float accelZ = accelerationZ / sensibilteAccel;
  float gyroX = vitesseRotationX / sensibilteGyro * DEG_TO_RAD;
  float gyroY = vitesseRotationY / sensibilteGyro * DEG_TO_RAD;
  float gyroZ = vitesseRotationZ / sensibilteGyro * DEG_TO_RAD;


  /* 3. Retirer la gravité pour obtenir acc. réelle */
  float realAccX = accelX ;
  float realAccY = accelY ;
  float realAccZ = accelZ - 1.0;

/* 4. Precision sur le sens de deplacement */
String sens= directionFromGreaterAxis(realAccX,realAccY,realAccZ);

  /* 5. Calcul de l'accélération */
  float accNorm=sqrt(pow(realAccX,2)+pow(realAccY,2)+pow(realAccZ,2));


  /* 6. Affichage du sens et de l'acceleration */

/*on place le curseur de l'écran LCD au début de la 1ère ligne  */
  lcd.setCursor(0,0);

  lcd.print("Sens: ");lcd.print(sens);

/*on place le curseur de l'écran LCD au début de la 2ème ligne  */
  lcd.setCursor(0,1);

  lcd.print("Acceleration:"); lcd.print(accNorm,1);
   delay(1000);
lcd.clear();


}
/* Fonction disant si la valeur suivant un axe est negligeable */
bool estNegligeable(float valeur) {
  return abs(valeur) < SEUIL;
}

/* Fonction precisant l'axe dont l'acceleration est la plus élévée */
String axePlusDominant(float x, float y, float z) {
  float absX = abs(x);
  float absY = abs(y);
  float absZ = abs(z);

  if (absX >= absY && absX >= absZ)
    return "X";
  else if (absY >= absX && absY >= absZ)
    return "Y";
  else
    return "Z";
}

/* Fonction donnant le sens dans lequel il se deplace suivant l'axe dominant */
String directionSelonAxe(String axe, float x, float y, float z)
{
  if (axe == "X") return x > 0 ? "avant" : "arriere";
  if (axe == "Y") return y > 0 ? "gauche" : "droite";
  if (axe == "Z") return z > 0 ? "haut" : "bas";
  return "inconnue";
}

/* Fonction donnant les directions simples */
String directionSimple(float x, float y, float z)
{
  if (estNegligeable(x) && estNegligeable(y) && estNegligeable(z))
    return "Immobile";

  if (!estNegligeable(x) && estNegligeable(y) && estNegligeable(z))
    return x > 0 ? "avant" : "arriere";

  if (estNegligeable(x) && !estNegligeable(y) && estNegligeable(z))
    return y > 0 ? "gauche" : "droite";

  if (estNegligeable(x) && estNegligeable(y) && !estNegligeable(z))
    return z > 0 ? "haut" : "bas";

  return ""; // Cas complexe à traiter dans la fonction principale
}

String directionFromGreaterAxis(float x, float y, float z)
{
  String dir = directionSimple(x, y, z);
  if (dir != "")
  {
    return dir;
  }

  // Cas combinés : on choisit l'axe le plus dominant
  String axe = axePlusDominant(x, y, z);
  return directionSelonAxe(axe, x, y, z);
}


```

Le code Arduino permet, comme il a été demandée, de préciser le sens (gauche/droite, haut/bas, avant/arrière ) dans lequel le capteur se déplace et son accélération durant le déplacement avec affichage sur un écran LCD. Voici les principales etapes du code:

- La récupération des données provenant du capteur(les valeurs brutes d’accélération et de vitesse angulaire suivant chaque axe) ;

- La conversion des valeurs brutes en valeurs physiques réelles(en m/s² pour les accélérations suivant chaque axe et en rad/s pour les vitesses angulaires);

- Le retrait de la gravité (G(0,0,1) dans le repère terrestre(repère fixe)) pour obtenir le vecteur-accélération réelle ;

- La détermination du sens de déplacement du capteur en se basant sur les valeurs d’accélération suivant chaque axe ;

- Et enfin l’affichage du sens et de l’acceleration (norme) sur l’ecran LCD.

## Difficultés rencontrées et amélioration apportées.

Notre objectif global était de détecter la direction de déplacement du capteur(Avant, arriere, gauche et droite) avec précision afin de déduire celle du robot, puis de déterminer également les angles de rotation du capteur suivant chaque axe.

### Obtention de données inprécis liéés à l'intervention de la gravité terrestre

En fait, étant donné qu'on se basait sur les valeurs d'accélération suivant chaque axe, on les obtenait grâce au capteur. Le problème c'est que les accélérations obtenues étaient la somme de 2 accélérations ( celle due au mouvement et celle due à la gravité) . Donc il fallait enlever la gravité sur chaque axe . Maintenant puisque durant le déplacement le capteur ne sera pas parfaitement plat, c'est-à-dire qu'il est possible qu'on fasse une rotation quelconque ce qui entraînerait une différence entre le repère fixe( répère terrestre) et celui du capteur( le repère dans lequel sont mesurées les valeurs d'accélération)puisque lorsque le capteur plat et qu'on tourne par rapport à Z, son repère est confondu à celui de la terre et donc il nous suffit de retirer les composantes de la gravité sur chaque axe qui sont ( 0,0,1). Donc on comprend que le problème ici c'est de retrouver le vecteur accélération dans le repère terrestre s'il y a une rotation du capteur .

Pour ce faire il vous faudrait la matrice de rotation du capteur qui est le produit matriciel non commutatif des matrices de rotation du capteur autour de X , de Y et de Z (s'il y en a eu). La rotation autour Z est moins possible ( c'est à dire que il faut être conscient d'après moi pour pouvoir tourner autour de Z) durant le déplacement du capteur la main. Donc on la laisse néglige. Les rotations suivant X et Y sont plus inattendues dans le déplacement avec la main. Le sens du produit matriciel dépend de si on fait une rotation autour de X puis autour de Y ( le produit matriciel donnera Ry.Rx) ou si on fait Y puis X (Rx.Ry).

Maintenant la solution à ce problème aurait été d'utiliser le quaternion qui permet de définir une rotation autour d'un axe dirigé par un vecteur unitaire et d'angle @. Donc on définirait le quaternion globale de la rotation totale(X puis Y ou Y puis X ) qui serait le produit non commutatif de q1(quaternion définissant une rotation autour X) et q2( quaternion pour Z). On se dit que le problème de produit non commutatif est de retour ! Eh ben non!! Car la bibliothèque madgwickAHRS nous permet d'obtenir directement le quaternion global de la rotation complète. Mais pour cela il faudrait qu'on ait accès aux différentes composantes du quaternion global (q0,q1,q2,q3). Ce qui n'est pas possible puisqu'ils ont été définis comme attribut privé de la classe Madgwick. Donc on ne peut pas y avoir accès .

Donc finalement, on s'est dit que les mouvements de rotation inattendus de notre main auraient un impact pas trop significatif sur le sens du déplacement (à priori et à fortiori).

### Difficultés à obtenir l'angle de lacet ( Yaw)

Le capteur MPU 6050 en combinant un gyroscope et un accéléromètre permet de mesurer avec un précision moyenne la direction de déplacement du capteur et aussi les angles de tangage et de roulis . Par contre, le calcul de l'angle de lacet ( Le plus important des angles) est impossible sans intégration de la vitesse angulaire car il n'existe pas de référence absolue horizontale à l'image de la gravitépour la verticale .L'integration étant faussé au fil du temps, il est donc impossible d'afficher ce angle avec notre capteur.
L'affichge des angles a donc été abandonné.

## Instabilité de l'alimentation

La cause de ce problème était assez bizarre et bête à la fois mais il fallait qu'on le notifie parcequ'on a vraiment déché dessus 😆. Le problème c'est quoi :lorsqu'on essai d'alimenter la carte arduino avec notre alimentation, les lumières qui montrent que la carte est bien alimenté s'allument très faiblement comme si le courant ou la tension était insuffisant et que l'arduino en demandais plus. La tension de sortie de l'alimentation a été mesuréé à plusieurs reprises, les câbles et tout le matériel testé séparemment mais rien d'anormal, tout semblais aller bien. Après de longues heures de réflexion et de dépression, on a commencer par effectuer des test de continuité avec notre multimètre histoire de vérifier si nos soudures avaient été bien faites. Et il s'avérais qu'on avait raison. La soudure au niveau de la résistance qui accompagnais le régulateur qu'on utilisais étais mal soudé et le test de continuité a révélé que le courant ne passais pas. Et le problème fut réglé. Ce problème nous a particulièrement appris que la pratique peut parfois diverger avec la théorie et drastiquement d'ailleurs 🤣.

## Résultat final:

Finalement nous n'avons pu déterminé que la direction de déplacement du capteur pour ce projet. Ici se présente la vidéo de fonctionnement du système:

<!-- <video controls="" autoplay="" loop="" muted="" width="100%" height="auto">
   <source src="https://fabacademy.org/2024/labs/energylab/students/mohamed-salifou/images/week13/I2C_2.mp4" type="video/mp4">
</video> -->
<iframe title="vimeo-player" src="https://player.vimeo.com/video/1092985856?h=e86efbfe9d" width="640" height="360" frameborder="0"    allowfullscreen>
</iframe>

## Limites et amélioration à long terme

1. Données faussées en cas de rotation du Capteur

Comme nous l'avons mentionné un peu plus haut, les données concernant la direction sont faussées en cas de rotation du capteur ce qui limite la précision de notre système.

2. Impossibilité d'estimer l'angle de rotation suivant l'axe Z

Ce problème étant lié au capteur qu'on utilise, Une solution assez évidente serait de changer de capteur et d'en utiliser un qui dispose d'un magnétomètre.

## Bilan Global et conclusion

Ce projet malgré ses limites peut être utilisé pour déterminer avec une certaine précision la direction de déplacement d'un objet dans l'espace et pourrait donc être utilisé en robotique, les drones , les stabilisateurs de mouvement et pleins d'autres systèmes.En outre, ce projet nous a énormément appris. De la compréhension du fonctionnement interne des capteurs gyroscope et accéléromètre au montage d'un régulateur en passant par l'utilisation du logiciel KICAD,
toutes les conditions étaient réunis pour nous plonger un peu plus dans le monde fascinant de l'électronique. Nous espérons à l'avenir améliorer la précision de notre système afin qu'il soit utilisable dans des systèmes un peu plus complexes.

## Annexe

- https://docs.sunfounder.com/projects/davinci-kit/fr/latest/2.2.6_mpu6050_module.html
- https://www.youtube.com/watch?v=REVp33SwwHE&t=7s
- https://www.youtube.com/watch?v=KuekQ-m9xpw

### La team ✌️

<p align="center">
  <img src="./assets/SC15.jpg" width="400" alt="Alex le soudeur😆👌">
</p>

<p align="center">
  <img src="./assets/SC16.jpg" width="400" alt="Donald Le codeur expérimenté👌✌️">
</p>

<p align="center">
  <img src="./assets/SC21.jpg" width="400" alt="Le schématiseur ✌️">
</p>

<p align="center">
  <img src="./assets/SC22.jpg" width="400" alt="Le réparateur d'imprimante 😆">
</p>
