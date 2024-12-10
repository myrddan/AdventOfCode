

if False:
    # Time:      7  15   30
    # Distance:  9  40  200"

    times = []
    times.append(7)
    times.append(15)
    times.append(30)

    distances = []
    distances.append(9)
    distances.append(40)
    distances.append(200)
else:
  # Time:        46     85     75     82
  # Distance:   208   1412   1257   1410"

    times = []
    times.append(46)
    times.append(85)
    times.append(75)
    times.append(82)

    distances = []
    distances.append(208)
    distances.append(1412)
    distances.append(1257)
    distances.append(1410)

sum = 0
for i in range(len(times)):
    time = times[i]
    distance = distances[i]

    cptWinPossible = 0

    for j in range(1,time):
        speed = j
        distanceTheorique = (time-j) * j

        if distanceTheorique > distance:
            cptWinPossible += 1


    if sum == 0:
        sum = cptWinPossible
    else:
        sum *= cptWinPossible


print("sum : ",sum)