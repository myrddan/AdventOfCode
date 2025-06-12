import itertools

# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True

if useDataTest :
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
##   Etape 1
##################################################################

import re

data = [ [False for i in range(1000)] for i in range(1000)]

for ligne in lignes:
    startX, startY, endX, endY = re.findall(r"\d+",ligne)

    isTurnOn = ligne.startswith("turn on")
    isTurnOff = ligne.startswith("turn off")
    isToggle = ligne.startswith("toggle")

    for i in range(int(startX),int(endX)+1):
        for j in range(int(startY),int(endY)+1):
            if isTurnOn:
                data[i][j] = True
            elif isTurnOff:
                data[i][j] = False
            elif isToggle:
                data[i][j] = not data[i][j]

for i in range(1000):
    for j in range(1000):
        if data[i][j] == True:
            resultatChallenge += 1

##################################################################
##   Etape 2
##################################################################

print("\nEtape 2 \n")

data = [ [0 for i in range(1000)] for i in range(1000)]

for ligne in lignes:
    startX, startY, endX, endY = re.findall(r"\d+",ligne)

    isTurnOn = ligne.startswith("turn on")
    isTurnOff = ligne.startswith("turn off")
    isToggle = ligne.startswith("toggle")

    for i in range(int(startX),int(endX)+1):
        for j in range(int(startY),int(endY)+1):
            if isTurnOn:
                data[i][j] += 1
            elif isTurnOff and  data[i][j] > 0:
                data[i][j] -= 1
            elif isToggle:
                data[i][j] += 2

for i in range(1000):
    for j in range(1000):
        resultatChallenge2 +=  data[i][j]


print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



