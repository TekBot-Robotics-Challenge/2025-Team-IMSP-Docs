# Utilité de la photorésistance dans le projet

La mesure de la **lumière ambiante** avec une **LDR** (photorésistance) exige la transformation de cette lumière en une **tension électrique comprise entre 0 et 5V** pour pouvoir la lire avec une entrée analogique (`analogRead`) de l’Arduino ou de l’ATMega.

**🎛️ Problème : la LDR seule ne génère pas une tension exploitable**

Une LDR change de résistance selon la lumière :

- Plus de lumière → résistance faible
- Moins de lumière → résistance élevée

Mais seule, la LDR ne fournit pas une tension, juste une résistance variable. Il faut donc un montage électrique qui transforme cette variation de résistance en une variation de tension. C’est là qu’intervient.

**⚙️ Le diviseur de tension**

On utilise un diviseur de tension, composé de :

- Une LDR (résistance variable)
- Une résistance fixe de 10 kΩ

Formule de la tension mesurée par l’Arduino :

$$
V_{A1} = \frac{R_{\text{fixe}}}{R_{\text{LDR}} + R_{\text{fixe}}} \times 5V
$$

**🔍 Pourquoi une résistance de 10 kΩ ?**

1. Elle forme avec la LDR un diviseur de tension efficace.
2. Elle est assez grande pour ne pas consommer trop de courant.
3. Elle est assez petite pour créer une variation de tension perceptible quand la lumière change.
4. C’est une valeur standard bien adaptée à la plage de résistance typique des LDR (de quelques centaines d’ohms à plusieurs dizaines de kΩ).

**🧲 Pourquoi on l’appelle parfois "pull-down" ?**

Le terme pull-down vient de l’électronique numérique, où une résistance ramène un signal vers 0V (GND) lorsqu’aucune autre source ne force l’état.

Dans notre cas :

- Le signal (point entre la LDR et la résistance) est tiré vers le bas (GND) par la résistance de 10 kΩ.
- Donc elle "pull down" la tension quand la LDR est très résistante (obscurité).

Mais ici, ce n’est pas exactement un pull-down au sens strict numérique — on parle plutôt d’un diviseur de tension, dont la résistance du bas joue ce rôle de tirer le signal vers 0V quand la LDR ne conduit presque plus. 

[Photorésistance : fonctionnement, choix, montages arduino, …](https://passionelectronique.fr/photoresistance/)