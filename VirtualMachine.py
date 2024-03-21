from Memory import *

class VirtualMachine:
    def __init__(self, file = None):
        self._memory = Memory(file)
        self._accumulator = Value()
        self._output = "Output:\n"
        self._input = []

    def set_inputs(self, new):
        if new != "":
            [self._input.append(i) for i in new.split(',')]
    
    def get_output(self):
        return self._output

    def sign(self, val):
        if int(val) == 0:
            return "+0000"
        if int(val) > 0:
            if len(val) == 4:
                return "+" + val
            elif len(val) < 4:
                while len(val) != 4:
                    val = "0" + val.strip('+')
                return "+" + val
            elif len(val) > 4:
                return "+" + val[len(val) - 4 : len(val)]
        else:
            sub = val.strip("-")
            if len(sub) == 4:
                return "-" + sub
            elif len(sub) < 4:
                while len(sub) < 4:
                    sub = "0" + sub
                return "-" + sub
            elif len(sub) > 4:
                return "-" + val[len(val) - 4 : len(val)]

    def __str__(self):
        text = "\n------------------------\n"
        text += "Resulting Memory:\n"
        for i in self._memory.get_values():
            text += f"{i.get_val()}\n"
        text += "\nAccumulator:\n"
        text += self._accumulator.get_val()
        text += "\n------------------------\n"
        return text

    def run(self):
        count = 0
        while True:
            curr_operator = self._memory._values[count].operator()
            curr_operand = self._memory._values[count].operand()
            
            if curr_operator == "43":
                break

            elif curr_operator == "40":
                count = int(curr_operand) - 1

            elif curr_operator == "20":
                self.load(curr_operand)

            elif curr_operator == "21":
                self.store(curr_operand)

            elif curr_operator == "10":
                address = int(curr_operand)
                self.read(count, address)

            elif curr_operator == "11":
                address = int(curr_operand)
                self.write(count, address)

            elif curr_operator == "41":
                if "-" in self._accumulator.get_val():
                    count = int(curr_operand) - 1
            
            elif curr_operator == "42":
                if int(self._accumulator.get_val()) == 0:
                    count = int(curr_operand) - 1

            elif curr_operator == "30":
                if int(curr_operand) > self._memory.size() - 1:
                    raise IndexError("Invalid memory address")
                self.add(self._memory._values[int(curr_operand)].get_val())

            #checks if operator is 31, if true executes addition.
            elif curr_operator == "31":
                if int(curr_operand) > self._memory.size() - 1: #change this into function
                    raise IndexError("Invalid memory address")
                self.subtract(self._memory._values[int(curr_operand)].get_val())

            elif curr_operator == "33":
                if int(curr_operand) > self._memory.size() - 1:
                    raise IndexError("Invalid memory address")
                self.multiply(self._memory._values[int(curr_operand)].get_val())

            elif curr_operator == "32":
                if int(curr_operand) > self._memory.size() - 1:
                    raise IndexError("Invalid memory address")
                self.divide(self._memory._values[int(curr_operand)].get_val())
            
            elif (self._memory.size() - 1) == count:
                raise IndexError("No More Executable Instructions")
            
            count += 1
        print(self)

    def resize_memory(self):
        new_list = [Value()] * 100
        for i in range(self._memory.size()):
            new_list[i] = self._memory._values[i]
        self._memory._values = new_list

    def load(self, curr):
        if self._memory.size() <= int(curr):
            self.resize_memory()
        self._accumulator.set_val(self._memory._values[int(curr)].get_val())

    def store(self, curr):
        if self._memory.size() <= int(curr):
            self.resize_memory()
        self._memory._values[int(curr)].set_val(self._accumulator.get_val())

    def read(self, count, address):
        if self._memory.size() > count:
            self.resize_memory()
        try:
            user_word = self._input[0]
            self._input.remove(self._input[0])
        except:
            raise ValueError("Invalid Inputs")
        if len(user_word) > 5:
            raise ValueError("Command too long")
        if address < 100 and address >= 0:
            self._memory._values[address].set_val(f"{self.sign(user_word)}")
        else:
            raise ValueError("Address not in memory")
        
    def write(self, count, address):
        if self._memory.size() > count:
            self.resize_memory()
        if self._memory._values[address].get_val() == None:
            output = "None"
        elif self._memory._values[address].get_val() != None and count >= 0 and count < 100:
            output = self.sign(self._memory._values[address].get_val())
        else:
            raise ValueError("Address not in memory")
        print(output)
        self._output += output + "\n"
        return output
    
    def add(self, curr):
        new = self.sign(str(int(curr) + int(self._accumulator.get_val())))
        self._accumulator.set_val(new)

    def subtract(self, curr):
        new = self.sign(str(int(self._accumulator.get_val()) - int(curr)))
        self._accumulator.set_val(new)

    def multiply(self, curr):
        new = self.sign(str(int(self._accumulator.get_val()) * int(curr)))
        self._accumulator.set_val(new)

    def divide(self, curr):
        new = self.sign(str(int(self._accumulator.get_val()) // int(curr)))
        self._accumulator.set_val(new)