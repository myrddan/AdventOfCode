# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False
# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

if useDataTest :
    # Utilisation des données test
    lignes = []
    if isLvlOne:
        lignes.append("47|53")
        lignes.append("97|13")
        lignes.append("97|61")
        lignes.append("97|47")
        lignes.append("75|29")
        lignes.append("61|13")
        lignes.append("75|53")
        lignes.append("29|13")
        lignes.append("97|29")
        lignes.append("53|29")
        lignes.append("61|53")
        lignes.append("97|53")
        lignes.append("61|29")
        lignes.append("47|13")
        lignes.append("75|47")
        lignes.append("97|75")
        lignes.append("47|61")
        lignes.append("75|61")
        lignes.append("47|29")
        lignes.append("75|13")
        lignes.append("53|13")
        lignes.append("")
        lignes.append("75,47,61,53,29")
        lignes.append("97,61,53,29,13")
        lignes.append("75,29,13")
        lignes.append("75,97,47,61,53")
        lignes.append("61,13,29")
        lignes.append("97,13,75,29,47")
    else:
        lignes.append("")
else:
    # Utilisation des données du challlenge
    fichier = open("input.txt", "r")
    lignes = fichier.readlines()

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

# Créaction d'un dico pour stoker les instructions
pageOrdering = {}

# Création
updates = []

# Création
updatesSafes = []

# Création
updatesUnsafes = []

isUpdate = False

#########################################################"""
# Traitement des données d'entrées
for ligne in lignes:
    ligne = ligne.strip()
    if "|" in ligne:
        first,second = ligne.split("|")
        if not first in pageOrdering.keys():
            pageOrdering[first] = ([],[])
        pageOrdering[first][1].append(second)

        if not second in pageOrdering.keys():
            pageOrdering[second] = ([],[])
        pageOrdering[second][0].append(first)
    elif "," in ligne:
        updates.append(ligne)

# Validation des updates
print("\npageOrdering\n")
print(pageOrdering)
print("\nUpdates:\n")
print(updates)


def testUpdate(update):
    print(f"\nTest : {update}")
    firstUnsafe = -1
    lastUnsafe = -1
    updateSafe = True
    for i in range(len(update)):
        for j in range(len(update)):
            if j < i:
                if not update[j] in pageOrdering[update[i]][0]:
                    updateSafe = False
                    if firstUnsafe == -1:
                        firstUnsafe = i
                    lastUnsafe = j
                    print(f"   is {update[j]} BEFORE {update[i]} : {update[j] in pageOrdering[update[i]][0]}")
                    break

            if j > i:
                if not update[j] in pageOrdering[update[i]][1]:
                    updateSafe = False
                    if firstUnsafe == -1:
                        firstUnsafe = i
                    lastUnsafe = j
                    print(f"   is {update[j]} AFTER  {update[i]} : {update[j] in pageOrdering[update[i]][1]}")
                    break

        if not updateSafe:
            break

    return updateSafe,firstUnsafe,lastUnsafe

for ligneUpdate in updates:


    update = ligneUpdate.split(",")

    updateSafe,firstUnsafe,lastUnsafe = testUpdate(update)

    if not updateSafe:
        print(f"{ligneUpdate} is not SAFE")
        print(f"First Unsafe {firstUnsafe}")
        print(f"LastUnsafe {lastUnsafe}")
        updatesUnsafes.append(update)
    else:
        print(f"{ligneUpdate} is SAFE")
        updatesSafes.append(update)


print("\n Récuperation des middle page number pour les pages safes")
for update in updatesSafes:
    number = int(update[(len(update)//2)])
    print(update)
    print(number)
    resultatChallenge += number

print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

resultatChallenge = 0


print("\n")

print(updatesUnsafes)
print(len(updatesUnsafes))
print()

import  random
for update in updatesUnsafes:

    print("\nRecherche : ",update)

    updateTest = update.copy()

    safe = False
    while not safe:

        safe, firstUnsafe, lastUnsafe = testUpdate(updateTest)
        if safe:
            number = int(updateTest[(len(updateTest) // 2)])
            print(f"Safe")
            print("Number : ",number)
            resultatChallenge += number
            break
        else:
            print(f"Unsafe ")
            print(f"First Unsafe {firstUnsafe}")
            print(f"LastUnsafe {lastUnsafe}")

            numberTemp = updateTest[firstUnsafe]
            updateTest[firstUnsafe] = updateTest[lastUnsafe]
            updateTest[lastUnsafe] = numberTemp

from os import system, name


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

# Then, whenever you want to clear the screen, just use this clear function as:
clear()

print(f"\nRésultat du challenge partie 2 : {resultatChallenge}")



