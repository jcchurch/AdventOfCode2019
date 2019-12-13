import sys
import IntComputer

if __name__ == '__main__':
    code = []
    with open(sys.argv[1]) as file:
        for line in file:
            code = [int(x) for x in line.strip().split(",")]

    cpu = IntComputer.IntComputer(code, [])
    output = cpu.full_run()

    block_tiles = 0
    for i in range(0, len(output), 3):
        start = output[i]
        end = output[i+1]
        tile = output[i+2]

        if tile == 2:
            block_tiles += 1

    print(block_tiles)
