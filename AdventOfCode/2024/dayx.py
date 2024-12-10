
# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = True

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True

if useDataTest :
    # Utilisation des données test
    lignes = []
    if isLvlOne:
        lignes.append("")
        lignes.append("")
        lignes.append("")
        lignes.append("")
        lignes.append("")
        lignes.append("")
        lignes.append("")
        lignes.append("")
        lignes.append("")
        lignes.append("")
    else:
        lignes.append("")
else:
    # Utilisation des données du challlenge
    fichier = open("input.txt", "r")
    lignes = fichier.readlines()

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

##################################################################"
##   Etape 1 Préparer mes données
##################################################################



##################################################################
##   Etape 2 exploiter les données
##################################################################

if isLvlOne:
    print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
else:
    print(f"\nRésultat du challenge partie 2 : {resultatChallenge}")



