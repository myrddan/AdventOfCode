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

instruction = {}

##################################################################"
##   Etape 1
##################################################################
"""
The Operators:

x << y
    Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y. 
x >> y
    Returns x with the bits shifted to the right by y places. This is the same as floor division of x by 2**y. 
x & y
    Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 
x | y
    Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 
~ x
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1. 
"""
import re

for ligne in lignes:
    calc,var = ligne.strip().split(" -> ")
    instruction[var] = calc

calcul = "a"
while re.search(r"[a-z]+",calcul):
    for var in re.findall("[a-z]+",calcul):
        print(f" {var} >> {instruction[var]}")
        calcul = re.sub(var, instruction[var], calcul)

    print(calcul)

calcul = re.sub("AND","&",calcul)
calcul = re.sub("OR", "|", calcul)
calcul = re.sub("LSHIFT", "<<", calcul)
calcul = re.sub("RSHIFT", ">>", calcul)
calcul = re.sub("NOT", "~", calcul)

print()
print(calcul)

print()
print(eval(calcul))
##################################################################
##   Etape 2
##################################################################

print("\nEtape 2 \n")


print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



