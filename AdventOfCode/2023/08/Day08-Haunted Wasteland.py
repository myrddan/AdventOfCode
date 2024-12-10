
import re

# Initialisation avec mes données test
if False:
    # lignes = []
    # lignes.append("RL")
    # lignes.append("")
    # lignes.append("AAA = (BBB, CCC)")
    # lignes.append("BBB = (DDD, EEE)")
    # lignes.append("CCC = (ZZZ, GGG)")
    # lignes.append("DDD = (DDD, DDD)")
    # lignes.append("EEE = (EEE, EEE)")
    # lignes.append("GGG = (GGG, GGG)")
    # lignes.append("ZZZ = (ZZZ, ZZZ)")


    lignes = []
    lignes.append("LLR")
    lignes.append("")
    lignes.append("AAA = (BBB, BBB)")
    lignes.append("BBB = (AAA, ZZZ)")
    lignes.append("ZZZ = (ZZZ, ZZZ)")

else:
    fichier = open("input", "r")
    lignes = fichier.readlines()

path = lignes[0]

cpt = 2
data = {}


start = []

while True:
    data[lignes[cpt][0:3]] = lignes[cpt][7:10] + lignes[cpt][12:15]
    if re.match( r"..A", lignes[cpt][0:3] ):
        start.append(lignes[cpt][0:3])
    cpt+=1
    if cpt == len(lignes):
        break

print(start)
step = 0
pos = "AAA"
directionpossible = data.get(pos)
reboucle = True
while reboucle:


    for c in path:
        if c != "\n":
            if c == "L":
                pos = directionpossible[0:3]
            else:
                pos = directionpossible[3:6]

            directionpossible = data.get(pos)
            step  += 1
            print("Move",step," ",c," direction",pos)

            if pos == "ZZZ":
                reboucle = False
                break






# while True:



# hands = re.findall(regex, puzzle_input)

