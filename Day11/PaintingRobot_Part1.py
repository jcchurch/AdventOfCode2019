import sys
import IntComputer

if __name__ == '__main__':
    code = []
    with open(sys.argv[1]) as file:
        for line in file:
            code = [int(x) for x in line.strip().split(",")]

    x = 0
    y = 0
    dx = 0
    dy = 1
    local = str(x)+","+str(y)
    grid = {}

    cpu = IntComputer.IntComputer(code, [0])
    color = cpu.run()
    xs = []
    ys = []
    while color != None:
        grid[local] = color

        xs.append(x)
        ys.append(y)

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
        local = str(x)+","+str(y)
        cpu.add( grid.get(local, 0) )
        color = cpu.run()

    print("First", len(grid))
