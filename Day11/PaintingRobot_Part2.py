import sys
import IntComputer

if __name__ == '__main__':
    code = []
    with open(sys.argv[1]) as file:
        for line in file:
            code = [int(x) for x in line.strip().split(",")]

    height = 10
    width = 50
    mymap = [0] * height
    for i in range(height):
        mymap[i] = [0] * width

    x = 0
    y = 0
    dx = 0
    dy = 1

    cpu = IntComputer.IntComputer(code, [1])
    color = cpu.run()
    while color != None:
        mymap[y][x] = color

        direction = cpu.run()
        if dy == 1 and direction == 0:
            dy = 0
            dx = -1
        elif dy == 1 and direction == 1:
            dy = 0
            dx = 1
        elif dy == -1 and direction == 0:
            dy = 0
            dx = 1
        elif dy == -1 and direction == 1:
            dy = 0
            dx = -1
        elif dx == 1 and direction == 0:
            dy = 1
            dx = 0
        elif dx == 1 and direction == 1:
            dy = -1
            dx = 0
        elif dx == -1 and direction == 0:
            dy = -1 
            dx = 0
        elif dx == -1 and direction == 1:
            dy = 1
            dx = 0
        x += dx
        y -= dy
        cpu.add( mymap[y][x] )
        color = cpu.run()

    print("Second")
    colors = [' ', '#']
    for m in mymap:
        print("".join([colors[x] for x in m]))
