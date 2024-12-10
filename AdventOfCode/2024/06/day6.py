import copy

# Les challenges contiennent des données pour comprendre et tester notre algo.
# Ce boolean sert à faciliter le passage de l'un à l'autre
useDataTest = True

# Il y a deux niveaux pour les challenges
# Ce boolean permet d'avoir les deux versions dans le même fichier
isLvlOne = True

# Affichage de log supplémentaire pour faciliter le debugage
verbose = True


if useDataTest :
    # Utilisation des données test
    lignes = []
    if isLvlOne:
        lignes.append("....#.....")
        lignes.append(".........#")
        lignes.append("..........")
        lignes.append("..#.......")
        lignes.append(".......#..")
        lignes.append("..........")
        lignes.append(".#..^.....")
        lignes.append("........#.")
        lignes.append("#.........")
        lignes.append("......#...")
    else:
        lignes.append("")
else:
    # Utilisation des données du challlenge
    fichier = open("input.txt", "r")
    lignes = fichier.readlines()


from enum import Enum

class GuardDep(Enum):
    GONORD = "^"
    GOEST = ">"
    GOSUD = "v"
    GOOUEST = "<"

    @staticmethod
    def tournerDroite(cls):
        match cls:
            case GuardDep.GONORD:
                return GuardDep.GOEST
            case GuardDep.GOEST:
                return GuardDep.GOSUD
            case GuardDep.GOSUD:
                return GuardDep.GOOUEST
            case GuardDep.GOOUEST:
                return GuardDep.GONORD


def getNextCase(posX,posY,dep):
    match dep:
        case GuardDep.GONORD:
            posX = posX
            posY = posY - 1

        case GuardDep.GOEST:
            posX = posX + 1
            posY = posY

        case GuardDep.GOSUD:
            posX = posX
            posY = posY + 1

        case GuardDep.GOOUEST:
            posX = posX - 1
            posY = posY

    if posX < 0 or posY < 0 or posX == len(data) or posY == len(data[0]):
        raise Exception("Le guard est sortie de la zone")

    return posX,posY


# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

##################################################################"
##   Etape 1 Préparer mes données
##################################################################

data = []

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


# Recherche du point de départ
# La position est symbolisé par deux variables posX et posY
posX = -1
posY = -1
dep = GuardDep.GOSUD


print("\n Recherche de la position initiale : \n")

for x in range(len(data[1])):
    for y in range(len(data)):
        if data[x][y] in ["<",">","v","^"]:
            posX = x
            posY = y
            dep = GuardDep(data[x][y])
            print(f"   Le garde est en position {posX+1}:{posY+1} et se déplace vers : {dep}")



def parcoursGuard(posXStart,posYStart,depStart,dataParcours,isRechercheBoucle):
    if isRechercheBoucle:
        dep = GuardDep.tournerDroite(depStart)
    else:
        dep = depStart
    posX = posXStart
    posY = posYStart

    cptBoucle = 0

    cptTours = 0
    cptX = 0

    while True:
        cptTours +=1
        if not isRechercheBoucle:
            print(f"etape {cptTours}/4602")
        try:
            testPosX, testPosY = getNextCase(posX, posY, dep)

            while dataParcours[testPosX][testPosY] in ["#","O"]:
                dep = GuardDep.tournerDroite(dep)
                if verbose:
                    print("Rencontre d'un obstacle")
                    print("Changement de direction vers :", dep)
                testPosX, testPosY = getNextCase(posX, posY, dep)

            if dataParcours[testPosX][testPosY] == "H":
                cptX += 1
            else:
                cptX = 0


            if isRechercheBoucle:
                if cptX == 10000 or (dataParcours[testPosX][testPosY] == "O" and dep == depStart and posX == posXStart and posY == posYStart):
                    for j in range(len(dataParcours[1])):
                        afficheLigne = ""
                        for i in range(len(dataParcours)):
                            afficheLigne = afficheLigne + dataParcours[i][j]
                        print(afficheLigne)
                    raise Exception("Boucle")
            else:
                dataTest = copy.deepcopy(dataParcours)
                dataTest[testPosX][testPosY] = "O"
                try:
                    parcoursGuard(posX, posY, dep, dataTest, True)
                except Exception :
                    print(f"Boucle avec O à la pos {testPosX+1}:{testPosY+1}")
                    cptBoucle += 1


            if dataParcours[testPosX][testPosY]  in ["X","H"]:
                dataParcours[posX][posY]  = "H"
            else:
                dataParcours[posX][posY] = "X"

            dataParcours[testPosX][testPosY] = dep.value
            posX = testPosX
            posY = testPosY

            if verbose:
                print("\n Affichage des données : \n")
                for j in range(len(dataParcours[1])):
                    afficheLigne = ""
                    for i in range(len(dataParcours)):
                        afficheLigne = afficheLigne + dataParcours[i][j]
                    print(afficheLigne)

                input("Continuer...")

        except Exception as ex:
            if "Boucle" in ex.args[0]:
                raise
            else:
                break

    if isRechercheBoucle:
        return 0
    else:
        return dataParcours,cptBoucle

data,resultatChallenge2 = parcoursGuard(posX,posY,dep,data,False)

print("\n Affichage des données : \n")
for j in range(len(data[1])):
    afficheLigne = ""
    for i in range(len(data)):
        afficheLigne = afficheLigne + data[i][j]
    print(afficheLigne)



# On compte les cases parcourus
for x in range(len(data[1])):
    for y in range(len(data)):
        if data[x][y] in ["<",">","v","^","X"]:
            resultatChallenge += 1




print(f"\nRésultat du challenge partie 1 : {resultatChallenge}")

print(f"\nRésultat du challenge partie 2 : {resultatChallenge2}")



