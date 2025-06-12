from builtins import print

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

##################################################################"
##   Etape 1
##################################################################

taillesquare = 3
puzzleInput = 277678

posx = 0
posy = 0

startx = 1
starty = 0

while puzzleInput >= taillesquare * taillesquare:
    taillesquare += 2
    startx += 1
    starty += 1

posx = startx
posy = starty

print(f"taillesquare = {taillesquare}")
print(f"startx = {startx}")
print(f"starty = {starty}")

testNumber = (taillesquare-2) * (taillesquare-2) + 1

trouve = False

for i in range(taillesquare -2):
    # print(f"testNumber > {testNumber} {posx}:{posy}")
    if testNumber == puzzleInput:
        trouve = True
        break
    else:
        testNumber +=1
        posy -= 1

if not  trouve:
    for i in range(taillesquare - 1):
        # print(f"testNumber > {testNumber} {posx}:{posy}")
        if testNumber == puzzleInput:
            trouve = True
            break
        else:
            testNumber += 1
            posx -= 1

if not  trouve:
    for i in range(taillesquare - 1):
        # print(f"testNumber > {testNumber} {posx}:{posy}")
        if testNumber == puzzleInput:
            trouve = True
            break
        else:
            testNumber += 1
            posy += 1

if not  trouve:
    for i in range(taillesquare - 1):
        # print(f"testNumber > {testNumber} {posx}:{posy}")
        if testNumber == puzzleInput:
            trouve = True
            break
        else:
            testNumber += 1
            posx += 1


print(f"posx = {posx}")
print(f"posy = {posy}")

resultatChallenge = abs(posy) + abs(posx)
##################################################################
##   Etape 2
##################################################################

def rechercher():
    result = 0

    if (posx + 1,posy) in cases:
        result += cases[(posx + 1,posy)]
    if (posx + 1,posy + 1) in cases:
        result += cases[(posx + 1 ,posy + 1 )]
    if (posx + 1, posy -1) in cases:
        result += cases[(posx +1, posy-1)]
    if (posx, posy + 1 ) in cases:
        result += cases[(posx, posy +1)]
    if (posx, posy - 1) in cases:
        result += cases[(posx, posy -1 )]
    if (posx - 1, posy) in cases:
        result += cases[(posx - 1, posy)]
    if (posx - 1, posy + 1) in cases:
        result += cases[(posx - 1 , posy + 1 )]
    if (posx - 1, posy - 1) in cases:
        result += cases[(posx - 1, posy - 1)]

    return result

taillesquare = 1
puzzleInput = 277678

posx = 0
posy = 0

cases = {}

testNumber = 1
cases[(posx,posy)] = testNumber

print(f" ajout {posx}:{posy} > {testNumber}")

posx += 1

while True:

    taillesquare += 2

    trouve = False
    for i in range(taillesquare - 2):
        testNumber = rechercher()

        # print(f"testNumber > {testNumber} {posx}:{posy}")
        if testNumber >= puzzleInput:
            trouve = True
            break
        else:
            print(f" ajout {posx}:{posy} > {testNumber}")
            cases[(posx, posy)] = testNumber
            posy -= 1


    if not trouve:
        for i in range(taillesquare - 1):
            testNumber = rechercher()

            # print(f"testNumber > {testNumber} {posx}:{posy}")
            if testNumber >= puzzleInput:
                trouve = True
                break
            else:
                print(f" ajout {posx}:{posy} > {testNumber}")
                cases[(posx, posy)] = testNumber
                posx -= 1

    if not trouve:
        for i in range(taillesquare - 1):
            testNumber = rechercher()

            # print(f"testNumber > {testNumber} {posx}:{posy}")
            if testNumber >= puzzleInput:
                trouve = True
                break
            else:
                print(f" ajout {posx}:{posy} > {testNumber}")
                cases[(posx, posy)] = testNumber
                posy += 1

    if not trouve:
        for i in range(taillesquare ):
            testNumber = rechercher()

            # print(f"testNumber > {testNumber} {posx}:{posy}")
            if testNumber >= puzzleInput:
                trouve = True
                break
            else:
                print(f" ajout {posx}:{posy} > {testNumber}")
                cases[(posx, posy)] = testNumber
                posx += 1

    if trouve:
        print(f"\n Trouve {posx}:{posy} > {testNumber}")
        cases[(posx, posy)] = testNumber
        break


print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")
print(f"\nRésultat du challenge partie 2 : {testNumber}")


# from fileinput import input
#
# sheet = [sorted(int(x) for x in l.split()) for l in input()]
#
# # Part 1
# print(sum(x[-1] - x[0] for x in sheet))
#
# # Part 2
# print(sum(y // x for row in sheet for i, x in enumerate(row) for y in row[i+1:] if y % x == 0))


