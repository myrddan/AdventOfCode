
# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True

if useDataTest :
    # Utilisation des données pour tester
    fichier = open("input.txt", "r")
    lignes = fichier.readlines()
else:
    # Utilisation des données du challlenge
    fichier = open("input2.txt", "r")
    lignes = fichier.readlines()

import re

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge  = 0
resultatChallenge2 = 0
##################################################################
##   Etape 2 exploiter les données
##################################################################
def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

for ligne in lignes:
    ligne = ligne.strip()
    print("\n",ligne)
    total = ligne.split(":")[0]
    number = ligne.split(":")[1].strip().split(" ")

    isPossible = False

    if isLvlOne:
        for i in range((2 ** (len(number) - 1))):
            txt = bin(i)[2:]
            txt = txt.zfill(len(number) - 1)

            chaineEval = ""

            totalEval = int(number[0])

            for i in range(len(txt)):
                if txt[i] == "0":
                    chaineEval += number[i] + "+"
                    totalEval = totalEval + int(number[i + 1])
                else:
                    chaineEval += number[i] + "*"
                    totalEval = totalEval * int(number[i + 1])

            chaineEval += number[-1]

            if totalEval == int(total):
                if verbose:
                    print(total, " == ", chaineEval, ">", totalEval, "  OUI")
                isPossible = True
            else:
                if verbose:
                    print(total, " == ", chaineEval, ">", totalEval, "  NON")

        if isPossible:
            print("POSSIBLE")
            resultatChallenge += int(total)
            resultatChallenge2 += int(total)
        else:
            print("TEST CONCAT")

            for i in range((3 ** (len(number)-1))):
                txt = ternary(i)
                txt = txt.zfill(len(number)-1)

                chaineEval = [number[0]]

                for i in range(len(txt)):
                    if txt[i] == "0":
                        chaineEval.append("+")
                        chaineEval.append(number[i+1])
                    elif txt[i] == "1":
                        chaineEval.append("*")
                        chaineEval.append(number[i+1])
                    else:
                        chaineEval.append("|")
                        chaineEval.append(number[i+1])

                totalEval = 0

                totalEval = int(chaineEval[0])
                pos = 1

                try:
                    while True:
                        if chaineEval[pos] == "+":
                            totalEval = totalEval + int(chaineEval[pos + 1])
                        elif chaineEval[pos] == "*":
                            totalEval = totalEval * int(chaineEval[pos + 1])
                        else:
                            totalEval = int(str(totalEval) + chaineEval[pos + 1])
                        pos += 2
                        if pos > len(chaineEval):
                            break
                except:
                    print("")

                if totalEval == int(total):
                    if verbose:
                        print(total, " == ", chaineEval, ">",totalEval,"  OUI")
                    isPossible = True
                else:
                    if verbose:
                        print(total, " == ", chaineEval, ">",totalEval,"  NON")

            if isPossible:
                print("POSSIBLE")
                resultatChallenge2 += int(total)
            else:
                print("IMPOSSIBLE")




if isLvlOne:
    print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
    print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



