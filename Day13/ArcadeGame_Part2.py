import sys
import IntComputer

def displayMap(mymap, tiles, frame):
    display = ""
    for row in mymap:
        display += "".join([ tiles[i] for i in row ]) + "\n"
    print(frame)
    print(display)

if __name__ == '__main__':
    code = []
    with open(sys.argv[1]) as file:
        for line in file:
            code = [int(x) for x in line.strip().split(",")]

    code[0] = 2
    tiles = [' ', '#', '+', '_', 'o']

    height = 26
    width = 42
    mymap = [0] * height
    for i in range(height):
        mymap[i] = [0] * width

    cpu = IntComputer.IntComputer(code)
    x = cpu.run()

    block_tiles = 0
    ball_x = 0
    paddle_x = 0
    while x >= 0:
        y = cpu.run()
        tile = cpu.run()

        if tile == 2: block_tiles += 1
        if tile == 3: paddle_x = x
        if tile == 4: ball_x = x

        if x >= 0 and y >= 0:
            mymap[y][x] = tile
        x = cpu.run()

    if paddle_x > ball_x:
        cpu.add(-1)
        paddle_x -= 1
    elif paddle_x < ball_x:
        cpu.add(1)
        paddle_x += 1
    else:
        cpu.add(0)
    ball_x = -1

    frame = 0
    # displayMap(mymap, tiles, frame)
    while x != None:
        y = cpu.run()
        tile = cpu.run()

        if x == -1 and y == 0: print("SCORE", tile)
        if tile == 0 and mymap[y][x] == 2: block_tiles -= 1
        if tile == 4: ball_x = x

        if x >= 0 and y >= 0:
            mymap[y][x] = tile

        if ball_x >= 0:
            if paddle_x > ball_x:
                cpu.add(-1)
                paddle_x -= 1
            elif paddle_x < ball_x:
                cpu.add(1)
                paddle_x += 1
            else:
                cpu.add(0)
            ball_x = -1

        # displayMap(mymap, tiles, frame)
        frame += 1
        x = cpu.run()
    # displayMap(mymap, tiles, frame)
