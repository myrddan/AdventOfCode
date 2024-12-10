
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 9 0 -degree bend connecting north and east.
# J is a 9 0 -degree bend connecting north and west.
# 7 is a 9 0 -degree bend connecting south and west.
# F is a 9 0 -degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch does
# n't show what shape the pipe has.
#

if False:
    # lignes = []
    # lignes.append(".....")
    # lignes.append("..S-7.")
    # lignes.append("..|.|.")
    # lignes.append("..L-J.")
    # lignes.append(".....")


    lignes = []
    lignes.append("..F7.")
    lignes.append(".FJ|.")
    lignes.append("SJ.L7")
    lignes.append("|F--J")
    lignes.append("LJ...")


else:
    fichier = open("input", "r")
    lignes = fichier.readlines()


# findS
posX = -1
posY = -1

for i in range(len(lignes)):
    for j in range(len(lignes[0])):
        if lignes[i][j]=="S":
            posX = j
            posY = i

goUp = False
goDown = False
goLeft = False
goRight = False

nbMove = 1
# On pars vers la droite
goLeft = True
posX += -1

print("Move",nbMove," ", lignes[posY][posX])

while lignes[posY][posX]!="S":

    if lignes[posY][posX] == "|":
        if goUp:
            posY += - 1
        else:
            posY +=  1

    elif lignes[posY][posX] == "-":
        if goRight:
            posX += 1
        else:
            posX += -1
    elif lignes[posY][posX] == "L":
        if goLeft:
            goLeft = False
            goUp = True
            posY += - 1
        else:
            goDown = False
            goRight = True
            posX += 1
    elif lignes[posY][posX] == "J":
        if goRight:
            goRight = False
            goUp = True
            posY += - 1
        else:
            goDown = False
            goLeft = True
            posX += - 1

    elif lignes[posY][posX] == "7":
        if goRight:
            goRight = False
            goDown = True
            posY += 1
        else:
            goUp = False
            goLeft = True
            posX += -1
    elif lignes[posY][posX] == "F":
        if goLeft:
            goLeft = False
            goDown = True
            posY += 1
        else:
            goUp = False
            goRight = True
            posX += 1

    nbMove += 1
    print("Move", nbMove, " ", lignes[posY][posX])

print("Moitier", nbMove/2)
