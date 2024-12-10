


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
cpt = 0
affiche = -1
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

    result = 0
    for tab in data:
        if cpt == affiche:
            print(tab)
        result += tab[len(tab)-1]
    total += result
    print(result)

    if cpt == affiche:
        break
    cpt += 1

print("Total :",total)