
# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = False

if useDataTest :
    # Utilisation des données test
    lignes = []
    lignes.append("2333133121414131402")

else:
    # Utilisation des données du challlenge
    fichier = open("input_challenge.txt", "r")
    lignes = fichier.readlines()

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

##################################################################"
##   Etape 1
##################################################################


###################
# Fonctionne avec les données test mais pas avec celels du challenges !!!




data = []
isblank = False
counter = 0

print(lignes[0])

for c in lignes[0]:
    if isblank:
        for i in range(int(c)):
            data.append(".")
        isblank = False
    else:
        for i in range(int(c)):
            data.append(str(counter))
        isblank = True
        counter = (counter + 1) % 10

if verbose:
    print(data)

total = sum(int(lignes[0][i]) for i in range(len(lignes[0])))
nbblank = sum(int(lignes[0][i]) for i in range(len(lignes[0]))if i % 2 == 1)
nbid = sum(int(lignes[0][i]) for i in range(len(lignes[0]))if i % 2 == 0)

print("Total : ", total)
print("nbid : ",nbid)
print("nbblank :",nbblank)

print("len tableau : ", len(data))
##################################################################
##   Etape 2
##################################################################

if isLvlOne:
    isInstructionPack = False

    while not isInstructionPack:
        firstP = -1
        lastD = -1

        for i in range(len(data)):
            if data[i] == ".":
                firstP = i
                break

        for i in range(len(data)):
            if data[-1-i] != ".":
                lastD = len(data)-i -1
                break

        if firstP < lastD:
            temp = data[firstP]
            data[firstP] = data[lastD]
            data[lastD] = temp
            data.pop()
            if verbose:
                print(data)
        else:
            break

    while data[-1] == ".":
        data.pop()

    if verbose:
        print()
        print(data)

    print("Len tableau 2 :",len(data))
    for i in range(len(data)):
        if data[i].isdigit():
            resultatChallenge += i * int(data[i])


if isLvlOne:
    print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
else:
    print(f"\nRésultat du challenge partie 2 : {resultatChallenge}")



