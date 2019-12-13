import sys
import IntComputer

if __name__ == '__main__':
    code = []
    with open(sys.argv[1]) as file:
        for line in file:
            code = [int(x) for x in line.strip().split(",")]

    code[0] = 2
    tiles = [' ', '|', '#', '_', 'o']

    height = 30
    width = 42
    mymap = [0] * height
    for i in range(height):
        mymap[i] = [0] * width

    cpu = IntComputer.IntComputer(code)
    value = cpu.run()

    block_tiles = 0
    ball_x = 0
    paddle_x = 0
    while value >= 0:
        cpu.add(0)
        x = value
        y = cpu.run()
        tile = cpu.run()

        if tile == 2:
            block_tiles += 1

        if tile == 3:
            paddle_x = x

        if tile == 4:
            ball_x = x

        if x >= 0 and y >= 0:
            mymap[y][x] = tile

        value = cpu.run()

    gap = ball_x - paddle_x
    if gap > 0:
        cpu.add(1)
        paddle_x += 1
    elif gap < 0:
        cpu.add(-1)
        paddle_x -= 1
    else:
        cpu.add(0)

    y = cpu.run()
    score = cpu.run()
    print(score)
    value = cpu.run()

    while block_tiles > 0:
        block_tiles = 0
        ball_x = -1
        paddle_x = -1
        while value != None:
            x = value
            y = cpu.run()
            tile = cpu.run()
            print(y, x, tile)

            if tile == 4:
                ball_x = x

            gap = ball_x - paddle_x
            if gap > 0:
                cpu.add(1)
                paddle_x += 1
            elif gap < 0:
                cpu.add(-1)
                paddle_x -= 1
            else:
                cpu.add(0)

            value = cpu.run()
        y = cpu.run()
        score = cpu.run()
        print(score)
        value = cpu.run()

  
    """
    display = ""
    for row in mymap:
        display += "".join([ tiles[i] for i in row ]) + "\n"
    print(display)
    """
