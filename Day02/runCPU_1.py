def compute(code, memory, index):
    while code[index] != 99:
        op = code[index]
        if op == 1:
           first = memory[code[index + 1]]
           second = memory[code[index + 2]]
           memory[code[index + 3]] = first + second
           index += 4
        if op == 2:
           first = memory[code[index + 1]]
           second = memory[code[index + 2]]
           memory[code[index + 3]] = first * second
           index += 4

if __name__ == '__main__':
    code = []
    with open("memory.txt") as file:
        for line in file:
            code = [int(x) for x in line.split(",")]
    code[1] = 12
    code[2] = 2
    memory = code[:]
    compute(code, memory, 0)
    print(memory[0])
