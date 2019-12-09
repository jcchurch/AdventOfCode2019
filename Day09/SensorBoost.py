import sys
import itertools

class IntComputer:
    def __init__(self, code):
        self.code = { i: code[i] for i in range(len(code)) }
        self.index = 0
        self.relative_base = 0

    def __get(self, paramOffset):
        mode = self.code[self.index] // (10 ** (1+paramOffset)) % 10
        address = -1
        if mode == 0:
            address = self.code[self.index + paramOffset]
        elif mode == 1:
            address = self.index + paramOffset
        elif mode == 2:
            address = self.relative_base + self.code[self.index + paramOffset]
        else:
            raise Exception("invalid mode. mode={}".format(mode))
        assert address >= 0
        return self.code.get(address, 0)

    def __write(self, position, value):
        assert type(value) == type(0)
        assert position >= 0
        assert self.code[position] >= 0
        self.code[self.code[position]] = value

    def run(self, in_sequence=[]):
        in_index = 0
        while self.code[self.index] != 99:
            op = self.code[self.index] % 100
            print("INDEX", self.index, "OP", op, "RB", self.relative_base)
            if op == 1:
                self.__write(self.index + 3, self.__get(1) + self.__get(2))
                self.index += 4
            if op == 2:
                self.__write(self.index + 3, self.__get(1) * self.__get(2))
                self.index += 4
            if op == 3:
                print("READING VALUE", in_sequence[in_index])
                self.__write(self.index + 1, in_sequence[in_index])
                in_index += 1
                self.index += 2
            if op == 4:
                value = self.__get(1)
                self.index += 2
                return value
            if op == 5:
                nextInstruction = self.index + 3
                if self.__get(1) != 0:
                    nextInstruction = self.__get(2)
                print("JUMP NOT ZERO to", nextInstruction, "(", self.__get(1), ")")
                self.index = nextInstruction
            if op == 6:
                nextInstruction = self.index + 3
                if self.__get(1) == 0:
                    nextInstruction = self.__get(2)
                print("JUMP ZERO to", nextInstruction, "(", self.__get(1), ")")
                self.index = nextInstruction
            if op == 7:
                valueToStore = 0
                if self.__get(1) < self.__get(2):
                    valueToStore = 1
                self.__write(self.index + 3, valueToStore)
                self.index += 4
            if op == 8:
                print("IS", self.__get(1) ,"==", self.__get(2))
                valueToStore = 0
                if self.__get(1) == self.__get(2):
                    valueToStore = 1
                self.__write(self.index + 3, valueToStore)
                self.index += 4
            if op == 9:
                self.relative_base += self.__get(1)
                self.index += 2

if __name__ == '__main__':
    code = []
    with open(sys.argv[1]) as file:
        for line in file:
            code = [int(x) for x in line.split(",")]

    cpu = IntComputer(code)
    value = cpu.run([1])
    while value != None:
        print(value)
        value = cpu.run()
