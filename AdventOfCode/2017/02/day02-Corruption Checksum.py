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

if useDataTest :
    # Utilisation des données test
    data = np.loadtxt('input_test.txt')
else:
    # Utilisation des données du challlenge
    data = np.loadtxt('input_challenge.txt')
import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

##################################################################"
##   Etape 1 Préparer mes données
##################################################################

print(data)

print(f"\nRésultat du challenge partie 1 : { sum(data.max(axis=1) - data.min(axis=1))}")


##################################################################
##   Etape 2 exploiter les données
##################################################################

if isLvlOne:
    print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
else:
    print(f"\nRésultat du challenge partie 2 : {resultatChallenge}")



# from fileinput import input
#
# sheet = [sorted(int(x) for x in l.split()) for l in input()]
#
# # Part 1
# print(sum(x[-1] - x[0] for x in sheet))
#
# # Part 2
# print(sum(y // x for row in sheet for i, x in enumerate(row) for y in row[i+1:] if y % x == 0))


