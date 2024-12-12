
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

# resultattrailheads = 0
##################################################################"
##   Etape 1 Préparer mes données
##################################################################

data = []

trailhead = []

# On charge les données dans une liste à deux dimensions
print("\nChargement des données dans une liste à deux dimension")
for c in lignes[0]:
    if not c == '\n':
        data.append([])

for ligne in lignes:
    for i in range(len(ligne)):
        if not ligne[i] == '\n':
            data[i].append(ligne[i])

# Affiche le tableau
print("\n Affichage des données : \n")
for j in range(len(data[1])):
    afficheLigne = ""
    for i in range(len(data)):
        afficheLigne = afficheLigne + data[i][j]
    print(afficheLigne)


##################################################################
##   Etape 2 exploiter les données
##################################################################

def testSuite(posx,posy,start):
    global trailhead
    # Test nord
    posxTest = posx
    posyTest = posy - 1
    if -1 < posxTest < len(data) and -1 < posyTest  < len(data[0]) and data[posxTest][posyTest] == str(int(data[posx][posy])+1):
        if verbose:
            print(f"     Trouvé  {data[posxTest][posyTest]} NORD en {posxTest}:{posyTest}")
        if data[posxTest][posyTest] == "9":
            trailhead.append(start + "-" + str(posxTest) + str(posyTest))
        else:
            testSuite(posxTest, posyTest,start)
    # Test Est
    posxTest = posx + 1
    posyTest = posy
    if -1 < posxTest < len(data) and -1 < posyTest  < len(data[0]) and data[posxTest][posyTest] == str(int(data[posx][posy])+1):
        if verbose:
            print(f"     Trouvé  {data[posxTest][posyTest]} EST en {posxTest}:{posyTest}")
        if data[posxTest][posyTest] == "9":
            trailhead.append(start + "-" + str(posxTest) + str(posyTest))
        else:
            testSuite(posxTest, posyTest,start)
    # Test Sud
    posxTest = posx
    posyTest = posy + 1
    if -1 < posxTest < len(data) and -1 < posyTest  < len(data[0]) and data[posxTest][posyTest] == str(int(data[posx][posy])+1):
        if verbose:
            print(f"     Trouvé  {data[posxTest][posyTest]} SUD en {posxTest}:{posyTest}")
        if data[posxTest][posyTest] == "9":
            trailhead.append(start + "-" + str(posxTest) + str(posyTest))
        else:
            testSuite(posxTest, posyTest,start)
    # Test Ouest
    posxTest = posx - 1
    posyTest = posy
    if -1 < posxTest < len(data) and -1 < posyTest  < len(data[0]) and data[posxTest][posyTest] == str(int(data[posx][posy])+1):
        if verbose:
            print(f"     Trouvé  {data[posxTest][posyTest]} OUEST en {posxTest}:{posyTest}")
        if data[posxTest][posyTest] == "9":
            trailhead.append(start + "-" + str(posxTest) + str(posyTest))
        else:
            testSuite(posxTest, posyTest,start)


print("\n Affichage des données : \n")
for j in range(len(data[1])):
    for i in range(len(data)):
        if data[i][j] == "0":
            start = str(i)+str(j)
            if verbose:
                print(f"\nTrouvé  0 en {str(i)+str(j)} ({start})")
            testSuite(i,j,start)

            if verbose:
                print(f"  Nombre trailheads : {len(trailhead)}")

            uniqueTrail = set(trailhead)
            if verbose:
                print(f"  Nombre unique trailheads : {len(uniqueTrail)}")
            resultatChallenge = len(uniqueTrail)

            global trailheads
            trailheads = []


if isLvlOne:
    print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
else:
    print(f"\nRésultat du challenge partie 2 : {resultatChallenge}")



