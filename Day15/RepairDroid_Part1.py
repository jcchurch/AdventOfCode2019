import sys
import IntComputer

def updatePosition(x, y, direction, status):
    if status == 1 or status == 2:
        if direction == 1:
            y += 1
        if direction == 2:
            y -= 1
        if direction == 3:
            x -= 1
        if direction == 4:
            x += 1
    return (x, y)

if __name__ == '__main__':
    code = []
    with open(sys.argv[1]) as file:
        for line in file:
            code = [int(x) for x in line.strip().split(",")]

    x = 0
    y = 0
    direction = 1
    cpu = IntComputer.IntComputer(code, [])

    status = -1
    while status != 2:
        cpu.add(direction)
        status = cpu.run()
        (x, y) = updatePosition(x, y, direction, status)
        
            
        


    print(block_tiles)
