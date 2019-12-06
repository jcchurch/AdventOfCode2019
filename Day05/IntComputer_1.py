def getMemory(code, index, paramOffset):
    mode = code[index] // (10 ** (1+paramOffset)) % 10
    if mode == 0:
        return code[code[index + paramOffset]]
    if mode == 1:
        return code[index + paramOffset]
    raise Exception("invalid mode. mode={}".format(mode))

def writeMemory(code, position, value):
    code[code[position]] = value

def intComputer(code):
    index = 0
    while code[index] != 99:
        op = code[index] % 100
        if op == 1:
            first = getMemory(code, index, 1)
            second = getMemory(code, index, 2)
            writeMemory(code, index + 3, first + second)
            index += 4
        if op == 2:
            first = getMemory(code, index, 1)
            second = getMemory(code, index, 2)
            writeMemory(code, index + 3, first * second)
            index += 4
        if op == 3:
            value = int(input("Enter a value: "))
            writeMemory(code, index + 1, value)
            index += 2
        if op == 4:
            print(getMemory(code, index, 1))
            index += 2

if __name__ == '__main__':
    code = []
    with open("memory.txt") as file:
        for line in file:
            code = [int(x) for x in line.split(",")]

    intComputer(code)
