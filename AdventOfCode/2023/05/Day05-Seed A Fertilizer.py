

class DataAlmanac():
    destinationRangeStart = 0
    sourceRangeStart = 0
    sourceRangeLength = 0

def createData(ligne):
    data = DataAlmanac()
    decoup = ligne.split(" ")
    data.destinationRangeStart = int(decoup[0])
    data.sourceRangeStart = int(decoup[1])
    data.sourceRangeLength = int(decoup[2])
    return data

def getNext(index, datas):
    for data in datas:
        if index >= data.sourceRangeStart and index < (data.sourceRangeStart + data.sourceRangeLength):
            diff = index - data.sourceRangeStart
            return data.destinationRangeStart + diff

    return  index

def getLocation(index):
    seed = index
    soil = getNext(seed,seedToSoilData)
    fertilizer = getNext(soil,soilToFertilizerData)
    water = getNext(fertilizer,fertilizerToWaterData)
    light = getNext(water,waterToLight)
    temperature = getNext(light,lightToTemparature)
    humidity = getNext(temperature,temparatureToHumidity)
    location =getNext(humidity,humidityToLocation)
    print(f"seed : {seed}, soil : {soil}, fertilizer : {fertilizer}, water : {water}, light : {light}, temperature : {temperature}, humidity : {humidity}, location : {location}")
    return location


if False:
    lignes = []
    lignes.append("seeds: 79 14 55 13\n")
    lignes.append("\n")
    lignes.append("seed-to-soil map:")
    lignes.append("50 98 2\n")
    lignes.append("52 50 48\n")
    lignes.append("\n")
    lignes.append("soil-to-fertilizer map:")
    lignes.append("0 15 37")
    lignes.append("37 52 2")
    lignes.append("39 0 15")
    lignes.append("\n")
    lignes.append("fertilizer-to-water map:")
    lignes.append("49 53 8")
    lignes.append("0 11 42")
    lignes.append("42 0 7")
    lignes.append("57 7 4")
    lignes.append("\n")
    lignes.append("water-to-light map:")
    lignes.append("88 18 7")
    lignes.append("18 25 70")
    lignes.append("\n")
    lignes.append("light-to-temperature map:")
    lignes.append("45 77 23")
    lignes.append("81 45 19")
    lignes.append("68 64 13")
    lignes.append("\n")
    lignes.append("temperature-to-humidity map:")
    lignes.append("0 69 1")
    lignes.append("1 0 69")
    lignes.append("\n")
    lignes.append("humidity-to-location map:")
    lignes.append("60 56 37")
    lignes.append("56 93 4")

else:
    fichier = open("input", "r")
    lignes = fichier.readlines()


# On va extraire les datas du fichiers en parcourant chaque bloc
indexLigne = 0

seeds = lignes[indexLigne]

indexLigne +=3

seedToSoilData = []
while lignes[indexLigne] != '\n':
    seedToSoilData.append(createData(lignes[indexLigne]))
    indexLigne += 1

indexLigne +=2

soilToFertilizerData = []
while lignes[indexLigne] != '\n':
    soilToFertilizerData.append(createData(lignes[indexLigne]))
    indexLigne += 1

indexLigne +=2

fertilizerToWaterData = []
while lignes[indexLigne] != '\n':
    fertilizerToWaterData.append(createData(lignes[indexLigne]))
    indexLigne += 1

indexLigne +=2

waterToLight = []
while lignes[indexLigne] != '\n':
    waterToLight.append(createData(lignes[indexLigne]))
    indexLigne += 1

indexLigne +=2

lightToTemparature = []
while lignes[indexLigne] != '\n':
    lightToTemparature.append(createData(lignes[indexLigne]))
    indexLigne += 1

indexLigne +=2

temparatureToHumidity = []
while lignes[indexLigne] != '\n':
    temparatureToHumidity.append(createData(lignes[indexLigne]))
    indexLigne += 1

indexLigne +=2


humidityToLocation = []
while lignes[indexLigne] != "\n":
    humidityToLocation.append(createData(lignes[indexLigne]))
    indexLigne += 1
    if indexLigne == len(lignes) :
        break

lowerLocation =-1
for seed in seeds.split(" "):
    if seed.strip().isdigit():
        loc = getLocation(int(seed.strip()))
        if lowerLocation == -1 :
            lowerLocation = loc
        elif loc < lowerLocation:
            lowerLocation = loc

print("LowerLoc = ",lowerLocation)
