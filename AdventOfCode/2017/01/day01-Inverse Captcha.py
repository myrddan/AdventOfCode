from builtins import print

# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True


import numpy as np

if useDataTest:
    # Utilisation des données test

    fichier = open("input_test.txt", "r")
    lignes = fichier.readlines()

    # lignes = []
    # if isLvlOne:
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    #     lignes.append("")
    # else:
    #     lignes.append("")
else:
    # Utilisation des données du challlenge
    fichier = open("input_challenge.txt", "r")
    lignes = fichier.readlines()

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0
resultatChallenge2 = 0

##################################################################"
##   Etape 1 Préparer mes données
##################################################################

import itertools as it

ligne = lignes[0]

for a, b in zip(it.chain(ligne[::1],ligne[-1:-1]), it.chain(ligne[1::1],ligne[0])):
    if a == b:
        resultatChallenge += int(a)


mid = int(len(ligne)/2)
for a, b in zip(ligne[:mid], ligne[mid:]):
    if a == b:
        resultatChallenge2 += int(a) * 2


##################################################################
##   Etape 2 exploiter les données
##################################################################

print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")





