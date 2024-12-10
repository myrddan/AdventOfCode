
import re

# Initialisation avec mes données test
if False:
    lignes = []
    lignes.append("LR")
    lignes.append("")
    lignes.append("11A = (11B, XXX)")
    lignes.append("11B = (XXX, 11Z)")
    lignes.append("11Z = (11B, XXX)")
    lignes.append("22A = (22B, XXX)")
    lignes.append("22B = (22C, 22C)")
    lignes.append("22C = (22Z, 22Z)")
    lignes.append("22Z = (22B, 22B)")
    lignes.append("XXX = (XXX, XXX)")

else:
    fichier = open("input", "r")
    lignes = fichier.readlines()


class navigation ():
    start = ""
    pos = ""
    directionpossible = ""

path = lignes[0].strip()
cpt = 2
data = {}
start = []

while True:
    data[lignes[cpt][0:3]] = lignes[cpt][7:10] + lignes[cpt][12:15]
    if re.match( r"..A", lignes[cpt][0:3] ):
        n = navigation()
        n.pos = lignes[cpt][0:3]
        n.start = n.pos
        start.append(n)

    cpt+=1
    if cpt == len(lignes):
        break

print(start)
step = 1

for n in start:
    n.directionpossible = data.get(n.pos)

reboucle = True
while reboucle:
    for c in path:
        for n in start:
            if c == "L":
                n.pos = n.directionpossible[0:3]
            else:
                n.pos = n.directionpossible[3:6]

            n.directionpossible = data.get(n.pos)

            print("Move",step," ",c,"start",n.start,"direction",n.pos)

        step += 1
        end = True
        for n in start:
            if not n.pos.endswith("Z"):
                end = False

        if end :
            reboucle = False
            break


