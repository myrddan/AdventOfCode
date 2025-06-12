
# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True

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

##################################################################"
##   Etape 1 Préparer mes données
##################################################################

import numpy as np
data = np.loadtxt('input_challenge.txt').T
print(data)
data.sort(axis=0)

print(f"\nRésultat du challenge partie 1 : {np.sum(sum(data[:2]) > data[2])}")
##################################################################
##   Etape 2 exploiter les données
##################################################################


import sys

data = np.loadtxt('input_challenge.txt').T.reshape(-1, 3).T
data.sort(axis=0)

print(f"\nRésultat du challenge partie 2 : {np.sum(sum(data[:2]) > data[2])}")





