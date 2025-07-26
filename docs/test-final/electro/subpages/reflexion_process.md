# Processus de réflexion et difficultés

**1.Comprendre ce que le capteur mesure**

Quand on mesures une couleur avec le capteur :

- Tu obtiens trois valeurs : `redFreq`, `greenFreq`, `blueFreq`.
- **Plus la fréquence est basse**, **plus la couleur correspondante est présente** (car la fréquence est inversement proportionnelle à l’intensité).
- Donc pour chaque couleur, on peut dire :
    
    ```
    Couleur claire → fréquence basse
    Couleur foncée ou absente → fréquence élevée
    ```
    
**2.Réflexion**

- Il est assez clair que pour détecter les couleurs primaires Rouge, Vert et Bleu, il suffirait de chercher la fréquence mesurée la plus basse. Si on obtenait par exemple :

-redFreq=30, greenFreq=70, blueFreq=80, alors on dira que l’objet est de couleur rouge. 

- Mais ici, notre objectif est de détecter le Rouge, le Vert, le Bleu et le Jaune. Alors comment prendre le jaune en compte ?
- La **première idée** fut de considérer **des plages de valeurs de fréquences fixes** pour chaque couleur à reconnaitre. Et on comprend que si les valeurs de fréquences mesurées ne se retrouvent pas dans une  des plages définies , alors la couleur ne correspond à rien .

Il est important de préciser que ces plages de valeurs doivent être déterminées en mesurant chaque couleur à détecter et en analysant la variation des valeurs. 

Le **problème** avec cette méthode est qu’elle est peu flexible et dépend des paramètres extérieurs comme:

-la stabilité des valeurs

-la distance,

-l’éclairage , l’angle d’éclairage 

-les teintes de couleurs

-etc.

La remarque s’est faite surtout au niveau de la distance parce que plus on s’éloignait de l’objet, plus les valeurs de fréquences augmentaient (ce qui est assez logique puisque l’intensité lumineuse de la lumière reflétée par l’objet diminue au fur et à mesure que la distance augmente conduisant ainsi à une augmentation de la fréquence) et dépassaient les plages de valeurs définies . Je précise qu’il ne fallait qu’une légère variation (1cm ) pour que la détection ne marche plus . Donc on s'est dit qu'en mesurant à plusieurs distances, les valeurs des fréquences de rouge, de vert, de bleu, dans une couleur, et en prenant pour minimum, le minimum des fréquences obtenues pour la distance la plus petite et pour maximum, le maximum des valeurs de fréquences pour la distance la plus grande, alors on aurait notre plage de valeurs. Mais un problème assez évident s'est posé : les plages se mélangeaient. Par exemple, le rouge et le jaune se confondaient de même que le bleu et le vert. 

Aussi, on s’est dit qu’en fixant la distance , qu’on aurait un meilleur résultat mais les mesures du capteur n’étaient pas assez stables et dépassaient parfois les plages de valeurs. De plus, la teinte de vert dont nous disposions n’était pas pur c’est à dire que son code décimal n’était pas (0,255,0) ce qui rendait la création des plages de valeurs encore plus compliquée. 

C’est comme ca que nous avons eu l’idée finale actuelle.