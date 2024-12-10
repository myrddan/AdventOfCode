import re

with open("input2", "r") as fichier:
    lignes = fichier.readlines()

sum = 0
cpt = 0

for ligne in lignes:
    for c in ligne:
        cpt += 1
        if c == "(":
            sum += 1

        if c == ")":
            sum -=1

        if sum == -1:
            print("cpt :",cpt)

print(" diff = ",sum)
