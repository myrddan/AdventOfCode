


if False:
    lignes = []
    lignes.append("0 3 6 9 12 15")
    lignes.append("1 3 6 10 15 21")
    lignes.append("10 13 16 21 30 45")

else:
    fichier = open("input", "r")
    lignes = fichier.readlines()

def newTab(lenght):
    tab = []
    for i in range(lenght):
        tab.append(0)
    return  tab


total = 0
for ligne in lignes:
    index = 1
    data = []
    data.append([])

    for c in ligne.strip().split(" "):
        data[0].append(int(c))

    continu = True
    while continu:
        data.append(newTab(len(data[0])))

        for i in range(index,len(data[0])):
            data[index][i] = data[index-1][i] - data[index-1][i-1]

        if sum(data[index]) == 0 :
            continu = False
        else:
            index+=1

    valeurCalc = 0
    for i in range(len(data)-2,-1,-1):
        valeurCalc = data[i][i]-valeurCalc

    total += valeurCalc


print("Total :",total)