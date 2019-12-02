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

    for noun in range(100):
        for verb in range(100):
            code[1] = noun
            code[2] = verb
            memory = code[:]
            compute(code, memory, 0)
            if memory[0] == 19690720:
                print(100 * noun + verb)
