import sys

class IntComputer:
    def __init__(self, code, in_sequence=[]):
        self.code = { i: code[i] for i in range(len(code)) }
        self.instruction_pointer = 0
        self.relative_base = 0
        self.in_sequence = in_sequence
        self.in_index = 0

    def __getMode(self, offset):
        return self.code[self.instruction_pointer] // (10 ** (1+offset)) % 10

    def __get(self, offset):
        address = [
                   self.code[self.instruction_pointer + offset], 
                   self.instruction_pointer + offset,
                   self.relative_base + self.code[self.instruction_pointer + offset]
                  ][ self.__getMode(offset) ]
        assert address >= 0
        return self.code.get(address, 0)

    def __write(self, offset, value):
        assert type(value) == type(0)
        position = self.instruction_pointer + offset
        assert position >= 0

        address = [
                   self.code[position],
                   -1,
                   self.relative_base + self.code[position]
                  ][ self.__getMode(offset) ]
        assert address >= 0
        self.code[address] = value

    def full_run(self):
        outs = []
        value = self.run()
        while value != None:
            outs.append(value)
            value = self.run()
        return outs

    def add_input(self, data):
        self.in_sequence.append(data)

    def run(self):
        while self.code[self.instruction_pointer] != 99:
            op = self.code[self.instruction_pointer] % 100
            if op == 1:
                self.__write(3, self.__get(1) + self.__get(2))
                self.instruction_pointer += 4
            if op == 2:
                self.__write(3, self.__get(1) * self.__get(2))
                self.instruction_pointer += 4
            if op == 3:
                self.__write(1, self.in_sequence[self.in_index])
                self.in_index += 1
                self.instruction_pointer += 2
            if op == 4:
                value = self.__get(1)
                self.instruction_pointer += 2
                return value
            if op == 5:
                next_instruction_pointer = self.instruction_pointer + 3
                if self.__get(1) != 0:
                    next_instruction_pointer = self.__get(2)
                self.instruction_pointer = next_instruction_pointer
            if op == 6:
                next_instruction_pointer = self.instruction_pointer + 3
                if self.__get(1) == 0:
                    next_instruction_pointer = self.__get(2)
                self.instruction_pointer = next_instruction_pointer
            if op == 7:
                valueToStore = 0
                if self.__get(1) < self.__get(2):
                    valueToStore = 1
                self.__write(3, valueToStore)
                self.instruction_pointer += 4
            if op == 8:
                valueToStore = 0
                if self.__get(1) == self.__get(2):
                    valueToStore = 1
                self.__write(3, valueToStore)
                self.instruction_pointer += 4
            if op == 9:
                self.relative_base += self.__get(1)
                self.instruction_pointer += 2

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

    cpu = IntComputer(code, [0])
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
        cpu.add_input( grid.get(local, 0) )
        color = cpu.run()

    print("First", len(grid))
