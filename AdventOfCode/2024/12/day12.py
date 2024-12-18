
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

    fichier = open("input_test2", "r")
    # fichier = open("input_test.txt", "r")
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

# Création d'une variable qui va stocker le résultat du challenge
resultatChallenge = 0

##################################################################"
##   Etape 1 Préparer mes données
##################################################################

regions = []
dejaVu = set()

nbLignes = len(data)
nbCols = len(data[0])

def rechercheRegion(region,start):

    seed = region[0]
    area = region[1]

    area.append(start)
    dejaVu.add(start)
    ligne = start[0]
    col = start[1]

    fence = 4

    if verbose:
        print(f"Rechercher REGION {seed} start {ligne + 1}:{col + 1}")

    for ligneTest,colTest in [(ligne - 1,col),(ligne + 1,col),(ligne,col -1),(ligne,col+1)]:
        if verbose:
            print(f"    Rechercher {seed} in {ligneTest}:{colTest}")
        if not (-1 < ligneTest < nbLignes and -1 < colTest < nbCols):
            if verbose:
                print(f"    Hors zone")
            continue
        if data[ligneTest][colTest] != seed:
            if verbose:
                print(f"    Seed différente : {data[ligneTest][colTest]}")
            continue

        fence = fence - 1

        if (ligneTest,colTest) in dejaVu :
            if verbose:
                print(f"    seed déja vu")
            continue

        if verbose:
            print(f"    Trouvé")

        rechercheRegion(region,(ligneTest, colTest))

    region[2][0] += fence

from enum import Enum

class fencerec(Enum):
    GONORD = [(0, -1), (-1, -1)]
    GOEST = [(+1, 0), (+1, -1)]
    GOSUD = [(0, +1), (+1, +1)]
    GOOUEST = [(-1, 0), (-1, +1)]

    @staticmethod
    def tournerDroite(cls):
        match cls:
            case fencerec.GONORD:
                return fencerec.GOEST
            case fencerec.GOEST:
                return fencerec.GOSUD
            case fencerec.GOSUD:
                return fencerec.GOOUEST
            case fencerec.GOOUEST:
                return fencerec.GONORD

    @staticmethod
    def tourneGauche(cls):
        match cls:
            case fencerec.GONORD:
                return fencerec.GOOUEST
            case fencerec.GOEST:
                return fencerec.GONORD
            case fencerec.GOSUD:
                return fencerec.GOEST
            case fencerec.GOOUEST:
                return fencerec.GOSUD


for l in range(nbLignes):
    for c in range(nbLignes):
        if (l, c) in dejaVu: continue
        region = (data[l][c],[],[0,0])
        rechercheRegion(region,(l, c))
        regions.append(region)


if verbose: print(regions)


for region in regions:
    seed = region[0]
    area = region[1]
    sides = 0

    start = area[0]
    ligne = start[0]
    col = start[1]
    dep = fencerec.GOEST

    firstTime = True
    if verbose:
        print(f"\nRechercher FENCE {seed} start {ligne + 1}:{col + 1}")

    while True:

        # Retour au pt de départ
        if not firstTime:
            if ligne == start[0] and col == start[1] and dep == fencerec.GOEST: break
        else:
            firstTime = False

        if not (-1 < ligne + dep.value[0][0] < nbLignes and -1 < col + dep.value[0][1] < nbCols):
            sides += 1
            dep = dep.tournerDroite(dep)
            if verbose:
                print(f"   Hors limite > tourner a droite")
            continue

        if verbose:
            print(f"   Is next same ? {data[ligne + dep.value[0][0]][col + dep.value[0][1]] == seed}")
        if data[ligne + dep.value[0][0]][col + dep.value[0][1]] == seed:
            if (-1 < ligne + dep.value[1][0] < nbLignes and -1 < col + dep.value[1][1] < nbCols) and verbose:
                print(f"   Is adjacent same ? {data[ligne + dep.value[1][0]][col + dep.value[1][1]] == seed:}")
            if (-1 < ligne + dep.value[1][0] < nbLignes and -1 < col + dep.value[1][1] < nbCols) and \
                    data[ligne + dep.value[1][0]][col + dep.value[1][1]] == seed:
                sides += 1
                ligne = ligne + dep.value[1][0]
                col = col + dep.value[1][1]
                dep = dep.tourneGauche(dep)
                if verbose:
                    print(f"   Tourner a gauche {dep}")
                    print(f"   Avancer {ligne + 1}:{col + 1}")
                continue
            else:
                ligne = ligne + dep.value[0][0]
                col = col + dep.value[0][1]
                if verbose:
                    print(f"   Avancer {ligne+1}:{col+1} {dep}")
        else:

            sides += 1
            dep = dep.tournerDroite(dep)
            if verbose:
                print(f"   Tourner a droite {dep}")
            continue




    region[2][1] = sides

    print(f"\nFENCE : {sides}  {seed} start {ligne + 1}:{col + 1}")

if verbose:
    print(f"\n\n recherche regions enclavé")
# recherche si une region est dans une autre
for region in regions:
    seed = region[0]
    area = region[1]

    isregionenclave = True
    regiontest = None

    if verbose:
        print(f"\n   Rechercher {seed} start {area[0][0] + 1}:{area[0][1] + 1}")

    for pos in area:
        ligne = pos[0]
        col = pos[1]

        if ligne == 0 or ligne == nbLignes - 1 \
                or col == 0 or col == nbCols - 1:
            if verbose:
                print(f"   bord de map {ligne + 1}:{col + 1}")
            isregionenclave = False
            break

        for ligneTest, colTest in [(ligne - 1, col), (ligne + 1, col), (ligne, col - 1), (ligne, col + 1),(ligne - 1, col - 1 ), (ligne + 1, col + 1 ), (ligne + 1, col - 1), (ligne - 1, col + 1)]:
            if data[ligneTest][colTest] != seed:
                if regiontest == None:
                    testseed = data[ligneTest][colTest]
                    for regionrec in regions:
                        if (ligneTest, colTest) in regionrec[1]:
                            regiontest = regionrec
                elif data[ligneTest][colTest] != testseed or data[ligneTest][colTest] == testseed and not (ligneTest, colTest) in regiontest[1]:
                    isregionenclave = False
                    break
            elif not (ligneTest, colTest) in area:
                isregionenclave = False
                break

    if verbose:
        print(f"   Enclave {isregionenclave}")

    if isregionenclave:
        print(f"\n Rechercher {seed} start {area[0][0] + 1}:{area[0][1] + 1} fences : {region[2][1]}")
        for regionrec in regions:
            if (ligneTest, colTest) in regionrec[1]:
                regionrec[2][1] = regionrec[2][1] + region[2][1]
                print(f"   Trouvé {regionrec[0]} old : {regionrec[2][1]-region[2][1]} newfence : {regionrec[2][1]}")

print(f"\nRésultat du challenge partie 1 : {sum(region[2][0] * len(region[1]) for region in regions)}")
print(f"\nRésultat du challenge partie 2 : {sum(region[2][1] * len(region[1]) for region in regions)}")



