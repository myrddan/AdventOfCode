
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

goUp = False
goDown = False
goLeft = False
goRight = False

donneeeTest = False

if donneeeTest:
    dataImport = []
    dataImport.append(".-.F..")
    dataImport.append("..S-7.")
    dataImport.append(".F|||.")
    dataImport.append(".JL-J.")
    dataImport.append("......")

    # dataImport = []
    # dataImport.append("FF7FSF7F7F7F7F7F---7")
    # dataImport.append("L|LJ||||||||||||F--J")
    # dataImport.append("FL-7LJLJ||||||LJL-77")
    # dataImport.append("F--JF--7||LJLJIF7FJ-")
    # dataImport.append("L---JF-JLJIIIIFJLJJ7")
    # dataImport.append("|F|F-JF---7IIIL7L|7|")
    # dataImport.append("|FFJF7L7F-JF7IIL---7")
    # dataImport.append("7-L-JL7||F7|L7F-7F7|")
    # dataImport.append("L.L7LFJ|||||FJL7||LJ")
    # dataImport.append("L7JLJL-JLJLJL--JLJ.L")

    # dataImport = []
    # dataImport.append("..........")
    # dataImport.append(".S------7.")
    # dataImport.append(".|F----7|.")
    # dataImport.append(".||OOOO||.")
    # dataImport.append(".||OOOO||.")
    # dataImport.append(".|L-7F-J|.")
    # dataImport.append(".|II||II|.")
    # dataImport.append(".L--JL--J.")
    # dataImport.append("..........")

else:
    fichier = open("input", "r")
    dataImport = fichier.readlines()
    # On pars vers la droite

def propage(data, posX , posY):

    data[posX][posY] = "0"

    try:
        if data[posX - 1][posY] == ".":
            propage(data, posX - 1, posY)
    except:
        posX = posX

    try:
        if data[posX + 1][posY] == ".":
            propage(data, posX + 1, posY)
    except:
        posX = posX

    try:
        if data[posX][posY + 1] == ".":
            propage(data, posX, posY + 1 )
    except:
        posX = posX

    try:
        if data[posX][posY - 1] == ".":
            propage(data, posX, posY - 1)
    except:
        posX = posX

lignes = []
data = []
for ligne in dataImport:
    tab = []
    lignes.append(tab)
    tab2 = []
    data.append(tab2)
    tab3 = []
    data.append(tab3)
    for c in ligne:
        tab.append(c)
        tab2.append(".")
        tab2.append(".")
        tab3.append(".")
        tab3.append(".")

# findS
posX = -1
posY = -1

for i in range(len(lignes)):
    for j in range(len(lignes[0])):
        if lignes[i][j]=="S":
            posX = j
            posY = i
            data[posY * 2][posX * 2 ] = lignes[posY][posX]

nbMove = 1
# On pars vers la droite*

if donneeeTest:
    goRight = True
    posX += 1
    data[posY * 2][posX * 2 - 1] = "-"
else:
    goLeft = True
    posX += -1
    data[posY * 2][posX * 2 + 1] = "-"


print("Move",nbMove," ", lignes[posY][posX])

data[posY * 2 ][posX * 2 ] = lignes[posY][posX]

while lignes[posY][posX] != "S":

    if lignes[posY][posX] == "|":
        if goUp:
            posY += - 1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2 + 1][posX * 2] = "|"
        else:
            posY +=  1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2 -1][posX * 2] = "|"
    elif lignes[posY][posX] == "-":
        if goRight:
            posX += 1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2][posX * 2 -1] = "-"
        else:
            posX += -1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2][posX * 2 +1] = "-"
    elif lignes[posY][posX] == "L":
        if goLeft:
            goLeft = False
            goUp = True
            posY += - 1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2 +1][posX * 2] = "|"
        else:
            goDown = False
            goRight = True
            posX += 1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2][posX * 2 -1] = "-"
    elif lignes[posY][posX] == "J":
        if goRight:
            goRight = False
            goUp = True
            posY += - 1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2 +1][posX * 2] = "|"
        else:
            goDown = False
            goLeft = True
            posX += - 1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2][posX * 2 +1] = "-"
    elif lignes[posY][posX] == "7":
        if goRight:
            goRight = False
            goDown = True
            posY += 1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2 -1][posX * 2] = "|"
        else:
            goUp = False
            goLeft = True
            posX += -1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2][posX * 2 +1] = "-"
    elif lignes[posY][posX] == "F":
        if goLeft:
            goLeft = False
            goDown = True
            posY += 1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2 - 1][posX * 2] = "|"
        else:
            goUp = False
            goRight = True
            posX += 1
            data[posY * 2][posX * 2] = lignes[posY][posX]
            data[posY * 2][posX * 2 -1] = "-"

    nbMove += 1
    print("Move", nbMove, " ", lignes[posY][posX])

result = 0
for i in range(len(data)):

    passageTop = True
    passageBot = True

    for j in range(len(data[0])):
        if data[i][j] == "0":
            result = result  # ne fait rien
        elif data[i][j] == ".":
            propage(data,i,j)
        elif data[i][j] == "|":
            passageTop = False
            passageBot = False
        elif data[i][j] == "F":
            passageBot = False
        elif data[i][j] == "L":
            passageTop = False
        elif data[i][j] == "7":
            passageBot = False
        elif data[i][j] == "J":
            passageTop = False

        if not passageTop and not passageBot:
            break


    passageTop = True
    passageBot = True

    for j in range(len(data[0])-1,-1,-1):
        if data[i][j]=="0":
            result = result# ne fait rien
        elif data[i][j]==".":
            propage(data, i, j)
        elif data[i][j] == "|":
            passageTop = False
            passageBot = False
        elif data[i][j] == "F":
            passageBot = False
        elif data[i][j] == "L":
            passageTop = False
        elif data[i][j] == "7":
            passageBot = False
        elif data[i][j] == "J":
            passageTop = False

        if not passageTop and not passageBot:
            break


for j in range(len(data[0])):
    passageLeft = True
    passageRight = True

    for i in range(len(data)):
        if data[i][j] == "0":
            result = result  # ne fait rien
        elif data[i][j] == ".":
            propage(data, i, j)
        elif data[i][j] == "-":
            passageLeft = False
            passageRight = False
        elif data[i][j] == "F":
            passageRight = False
        elif data[i][j] == "L":
            passageRight = False
        elif data[i][j] == "7":
            passageLeft = False
        elif data[i][j] == "J":
            passageLeft = False

        if not passageRight and not passageLeft:
            break

    passageLeft = True
    passageRight = True

    for i in range(len(data) - 1, -1, -1):
        if data[i][j] == "0":
            result = result  # ne fait rien
        elif data[i][j] == ".":
            propage(data, i, j)
        elif data[i][j] == "-":
            passageLeft = False
            passageRight = False
        elif data[i][j] == "F":
            passageRight = False
        elif data[i][j] == "L":
            passageRight = False
        elif data[i][j] == "7":
            passageLeft = False
        elif data[i][j] == "J":
            passageLeft = False

        if not passageRight and not passageLeft:
            break

for i in range(0,len(data),2):
    for j in range(0,len(data[0]),2):
        if data[i][j] == ".":
            result += 1

with open("export", "w", encoding ="utf8") as f :
    for i in range(len(data)):
        for j in range(len(data[0])):
            f.write(data[i][j])
        f.write("\n")





print(data)
print("enclosed", result)
