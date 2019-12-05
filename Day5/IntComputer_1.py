def getMemory(code, position, mode):
    if mode == 0:
        return code[code[position]]
    if mode == 1:
        return code[position]
    raise Exception("invalid mode. mode={}".format(mode))

def writeMemory(code, position, value):
    code[code[position]] = value

def intComputer(code):
    index = 0
    while code[index] != 99:
        op = int(code[index] % 100)
        m1 = code[index] // 100 % 10
        m2 = code[index] // 1000 % 10
        m3 = code[index] // 10000 % 10 # Currently not in use
        if op == 0:
            return
        if op == 1:
            first = getMemory(code, index + 1, m1)
            second = getMemory(code, index + 2, m2)
            writeMemory(code, index + 3, first + second)
            index += 4
        if op == 2:
            first = getMemory(code, index + 1, m1)
            second = getMemory(code, index + 2, m2)
            writeMemory(code, index + 3, first * second)
            index += 4
        if op == 3:
            value = int(input("Enter a value: "))
            writeMemory(code, index + 1, value)
            index += 2
        if op == 4:
            print(getMemory(code, index + 1, m1))
            index += 2

if __name__ == '__main__':
    code = []
    with open("memory.txt") as file:
        for line in file:
            code = [int(x) for x in line.split(",")]

    intComputer(code)
