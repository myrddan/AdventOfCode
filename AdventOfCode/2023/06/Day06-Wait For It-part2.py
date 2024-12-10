

if False:
    # Time:      7  15   30
    # Distance:  9  40  200"

    time =71530
    distance = 940200
else:
  # Time:        46     85     75     82
  # Distance:   208   1412   1257   1410"

    time = 46857582
    distance = 208141212571410

cptWinPossible = 0

start = time / 2
index = start

win = True


while True:
    speed = index
    distanceTheorique = (time - index) * speed

    if distanceTheorique > distance:
        cptWinPossible += 1
        index += 1
        if index == time:
            break
    else:
        break


index = start -1
while True:
    speed = index
    distanceTheorique = (time - index) * speed

    if distanceTheorique > distance:
        cptWinPossible += 1
        index -= 1
    else:
        break




print("cptWinPossible : ",cptWinPossible)