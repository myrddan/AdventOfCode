import itertools

# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True


# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0
resultatChallenge2 = 0



##################################################################"
##   Etape 1
##################################################################
print("\nEtape 1 \n")

# J'ai trouvé une bibliothèque qui calculs les diviseurs
from sympy import divisors

cpt = 0
while True:
    cpt += 1

    # j'ai enlevé un zero par rapport à l'input du challenge
    if sum(divisors(cpt)) > 3600000:
        resultatChallenge = cpt
        break




print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



