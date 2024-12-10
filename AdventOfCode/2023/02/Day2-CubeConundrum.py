
fichier = open("input", "r")
lignes = fichier.readlines()

nbMaxRed = 12
nbMaxGreen = 13
nbMaxBlue = 14

cptPossible = 0
cptPower = 0

for ligne in lignes:
    gameGood = True
    index = ligne.find(":")
    id = int(ligne[5:index])
    data = ligne[index+2:]

    maxRed=0
    maxGreen=0
    maxBlue=0

    for pickup in data.split(";"):
        for couleur in pickup.split(","):

            decoup = couleur.strip().split(" ")
            if id < 6:
                print(couleur)
            match decoup[1]:
                case "blue":
                    if int(decoup[0])>nbMaxBlue:
                        gameGood = False
                    if int(decoup[0]) > maxBlue:
                        maxBlue = int(decoup[0])
                        if id < 6:
                            print("maxBlue <<", int(decoup[0]))
                case "green":
                    if int(decoup[0]) > nbMaxGreen:
                        gameGood = False
                    if int(decoup[0]) > maxGreen:
                        maxGreen = int(decoup[0])
                        if id < 6:
                            print("maxGreen <<", int(decoup[0]))
                case "red":
                    if int(decoup[0]) > nbMaxRed:
                        gameGood = False
                    if int(decoup[0]) > maxRed:
                        maxRed = int(decoup[0])
                        if id < 6:
                            print("maxRed <<", int(decoup[0]))


    if gameGood:
        print(id,"POSSIBLE")
        cptPossible +=id
    else:
        print(id, "NON ")

    cptPower += maxGreen*maxRed*maxBlue
    print(id,maxGreen*maxRed*maxBlue)


print("totalPossible",cptPossible)
print("totalPower",cptPower)