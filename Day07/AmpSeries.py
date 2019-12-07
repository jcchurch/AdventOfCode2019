import sys
import itertools

class IntComputer:
    def __init__(self, code):
        self.code = code
        self.index = 0

    def getMemory(self, paramOffset):
        mode = self.code[self.index] // (10 ** (1+paramOffset)) % 10
        if mode == 0:
            return self.code[self.code[self.index + paramOffset]]
        if mode == 1:
            return self.code[self.index + paramOffset]
        raise Exception("invalid mode. mode={}".format(mode))

    def writeMemory(self, position, value):
        assert type(value) == type(0)
        self.code[self.code[position]] = value

    def run(self, in_sequence):
        in_index = 0
        while self.code[self.index] != 99:
            op = self.code[self.index] % 100
            if op == 1:
                first = self.getMemory(1)
                second = self.getMemory(2)
                self.writeMemory(self.index + 3, first + second)
                self.index += 4
            if op == 2:
                first = self.getMemory(1)
                second = self.getMemory(2)
                self.writeMemory(self.index + 3, first * second)
                self.index += 4
            if op == 3:
                value = in_sequence[in_index]
                self.writeMemory(self.index + 1, value)
                in_index += 1
                self.index += 2
            if op == 4:
                value = self.getMemory(1)
                self.index += 2
                return value
            if op == 5:
                first = self.getMemory(1)
                second = self.getMemory(2)
                self.index += 3
                if first != 0:
                    self.index = second
            if op == 6:
                first = self.getMemory(1)
                second = self.getMemory(2)
                self.index += 3
                if first == 0:
                    self.index = second
            if op == 7:
                first = self.getMemory(1)
                second = self.getMemory(2)
                self.writeMemory(self.index + 3, 0)
                if first < second:
                    self.writeMemory(self.index + 3, 1)
                self.index += 4
            if op == 8:
                first = self.getMemory(1)
                second = self.getMemory(2)
                self.writeMemory(self.index + 3, 0)
                if first == second:
                    self.writeMemory(self.index + 3, 1)
                self.index += 4

if __name__ == '__main__':
    code = []
    with open(sys.argv[1]) as file:
        for line in file:
            code = [int(x) for x in line.split(",")]

    best = 0
    best_phase_sequence = []
    for phase_sequence in itertools.permutations([0,1,2,3,4]):
        previous = 0
        for phase in phase_sequence:
            cpu = IntComputer(code)
            out = cpu.run([phase, previous])
            previous = out
        if previous > best:
            best = previous
            best_phase_sequence = phase_sequence

    print("First:", best_phase_sequence, best)

    best = 0
    best_phase_sequence = []
    for phase_sequence in itertools.permutations([5,6,7,8,9]):
        previous = 0
        cpus = []
        for phase in phase_sequence:
            cpus.append(IntComputer(code))
            previous = cpus[-1].run([phase, previous])

        last = previous
        while previous != None:
            last = previous
            i = 0
            for phase in phase_sequence:
                previous = cpus[i].run([previous])
                i += 1
        if last > best:
            best = last
            best_phase_sequence = phase_sequence

    print("Second:", best_phase_sequence, best)
