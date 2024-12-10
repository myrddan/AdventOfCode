# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = False
# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = False

if useDataTest :
    # Utilisation des données test
    lignes = []
    lignes.append("7 6 4 2 1")
    lignes.append("1 2 7 8 9")
    lignes.append("9 7 6 2 1")
    lignes.append("1 3 2 4 5")
    lignes.append("8 6 4 4 1")
    lignes.append("1 3 6 7 9")
else:
    # Utilisation des données du challlenge
    fichier = open("input.txt", "r")
    lignes = fichier.readlines()

# Création d'une variable qui va stocker la somme des différences entre les nombres des deux jeux de test.
sum = 0


##################################################################"
##   Etape 1 Exploiter les données
##################################################################
# Je vais ici parcourir mes données ligne par ligne

def testNombres (nombreUn, nombreDeux, isSuiteIncrement):
    difference = nombreUn - nombreDeux

    if (difference > 0) != isSuiteIncrement or abs(difference) < 1 or abs(difference) > 3:
        print("test : ", nombreDeux, " ", nombreUn, " : ", difference, " NOT SAFE")
        return False
    else:
        print("test : ", nombreDeux, " ", nombreUn, " : ", difference, " SAFE")
        return True


def testSiLigneSafe(datas):

    # On détermine si c'est une suite qui s'incrémente ou se décrémente
    # Si le second est plus grand alors on a un début de suite croissante
    if (datas[1] - datas[0]) > 0:
        isSuiteIncrement = True
    else:
        isSuiteIncrement = False

    print(datas)
    print("isSuiteIncrement=", isSuiteIncrement)

    for i in range(1, len(datas)):
        isSafe = testNombres(datas[i], datas[i - 1], isSuiteIncrement)

        if not isSafe:
            return False

    return True



for ligne in lignes:
    # Pour chaque ligne je vais récuperer les nombre de gauche et celui de droite et les stocker dans deux listes

    if isLvlOne:
        print("\n", ligne)
        split = ligne.split(" ")
        datas = []
        for e in split:
            datas.append(int(e))

        isSafe = testSiLigneSafe(datas)

        if isSafe:
            print(ligne, " is safe")
            sum += 1
        else:
            print(ligne, " is not safe !!!")
    else:
        print("\n", ligne)
        split = ligne.split(" ")
        datas = []
        for e in split:
            datas.append(int(e))


        # On test la chaine complete
        isSafe = testSiLigneSafe(datas)

        if not isSafe:
            for i in range(len(datas)):
                datasTest = datas.copy()
                del datasTest[i]

                isSafe = testSiLigneSafe(datasTest)

                if isSafe:
                    break

        if isSafe:
            print(ligne, " is safe")
            sum += 1
        else:
            print(ligne, " is not safe !!!")

# On affiche la somme
print("\n\nResult : ", sum)