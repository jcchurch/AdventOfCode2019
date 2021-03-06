class IntComputer:
    def __init__(self, code, in_sequence=[]):
        """
        This builds a new IntComputer object.
        
        `code` is a list of integers representing the code
               that the IntComputer should execute.
        `in_sequence` is a list of integer inputs that will
               be sequenctially supplied to the computer
               each time an input instruction is encountered.
               Methods are available should you wish to supply
               additional input after execution as started.
               This parameter is optional.
        """
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
        """
        Runs a computer until it stops.
        Returns a list of the outputs.
        """
        outs = []
        value = self.run()
        while value != None:
            outs.append(value)
            value = self.run()
        return outs

    def add(self, value):
        """
        Adds a single value to the input stream.
        """
        assert type(value) == type(0)
        self.in_sequence.append(value)

    def run(self):
        """
        Runs a computer until it stops or it outputs any data.
        The internal state of the computer is kept so that this
        function can be called again to resume execution.

        This will return a single output upon an output instruction
        or it will return None. None represents the conclusion
        of the program's execution.
        """
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
