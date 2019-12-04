WIRES_CROSS = 3

def setGrid(grid, x, y, value):
    s = str(y) + "," + str(x)
    grid[s] = value

def getGrid(grid, x, y):
    s = str(y) + "," + str(x)
    return grid.get(s, 0)

def layWire(grid, crosses, y, x, swipe):
    if getGrid(grid, x, y) < 0 and swipe > 0:
        crosses.append([y,x])
        setGrid(grid, x, y, WIRES_CROSS)
    else:
        setGrid(grid, x, y, getGrid(grid, x, y) + swipe)

def updateXY(direction, x, y):
    if direction == "R":
        x += 1
    if direction == "L":
        x -= 1
    if direction == "U":
        y -= 1
    if direction == "D":
        y += 1
    return (x, y)

if __name__ == '__main__':

    grid = {}
    paths = []
    with open("paths.txt") as file:
        for line in file:
            line = line.strip()
            paths.append( line.split(",") )

    crosses = []

    swipe = -1
    for path in paths:
        x = 0
        y = 0
        setGrid(grid, x, y, swipe)
        for stretch in path:
            direction = stretch[0]
            distance = int(stretch[1:])

            for i in range(1, distance+1):
                (x, y) = updateXY(direction, x, y)
                layWire(grid, crosses, y, x, swipe)
        swipe = 1

    wires = [{},{}]
    for path in range(2):
        x = 0
        y = 0
        total_dist = 1
        for stretch in paths[path]:
            direction = stretch[0]
            distance = int(stretch[1:])

            for i in range(1, distance+1):
                (x, y) = updateXY(direction, x, y)
                if getGrid(grid, x, y) == WIRES_CROSS:
                    wires[path][str(y)+","+str(x)] = total_dist
                total_dist += 1

    minCross = 100000
    for cross in crosses:
        (y, x) = cross
        key = str(y) + "," + str(x)

        distance = wires[0][key] + wires[1][key]
        if distance < minCross:
            minCross = distance 
    print(minCross)

