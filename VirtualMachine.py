from Memory import *

class VirtualMachine:
    def __init__(self, file = None):
        self._memory = Memory(file)
        self._accumulator = Value()
        self._output = "Output:\n"
        self._input = []
        self._length_of_data = len(self._memory._values[0].get_val())
        self._legacy_length = 5 #5 including the +/-
        self._updated_length = 7 #7 including the +/-

    def set_inputs(self, new):
        if new != "":
            [self._input.append(i) for i in new.split(',')]
    
    def get_output(self):
        return self._output
    
    def validate_inputs(self):
        required_inputs = 0
        for i in self._memory._values:
            if i.operator() == "10" or i.operator() == "010":
                required_inputs += 1
        if required_inputs != len(self._input):
            return False, required_inputs
    
        for single_input in self._input:
            single_input = single_input.strip()
            if len(single_input) != self._length_of_data - 1:
                raise TypeError("Values and inputs must all be 4 or all 6 digits in length.")
                
        return True, required_inputs
    
    def sign(self, val):
        x = 4 if self._memory._legacy else 6
        if int(val) == 0:
            return "+0000" if self._memory._legacy else "+000000"
        if int(val) > 0:
            if len(val) == x:
                return "+" + val
            elif len(val) < x:
                while len(val) != x:
                    val = "0" + val.strip('+')
                return "+" + val
            elif len(val) > x:
                return "+" + val[len(val) - x : len(val)]
        else:
            sub = val.strip("-")
            if len(sub) == x:
                return "-" + sub
            elif len(sub) < x:
                while len(sub) < x:
                    sub = "0" + sub
                return "-" + sub
            elif len(sub) > x:
                return "-" + val[len(val) - x : len(val)]

    def __str__(self):
        text = "\n------------------------\n"
        text += "Resulting Memory:\n"
        for i in self._memory.get_values():
            text += f"{i.get_val()}\n"
        text += "\nAccumulator:\n"
        text += self._accumulator.get_val()
        text += "\n------------------------\n"
        return text
    
    def validate_length(self):
        if len(self._memory._values) > 250:
            raise ValueError("Program too long.")
        
    def check_data_uniformity(self):
        #Checks to see if all the data members in the file have the same length
        if self._length_of_data != self._legacy_length and self._length_of_data != self._updated_length:
            raise TypeError("Values must all be 4 or all 6 digits in length.")
        for data_member in self._memory._values:
            if ((len(data_member.get_val()) != self._length_of_data) and (data_member.get_val() != "")):
                raise TypeError("Values must all be 4 or all 6 digits in length.")

    def run(self):
        self.validate_length()
        self.check_data_uniformity()
        count = 0
        while True:
            curr_operator = self._memory._values[count].operator()
            curr_operand = self._memory._values[count].operand()
            
            if curr_operator == "43" or curr_operator == "043":
                break

            elif curr_operator == "40" or curr_operator == "040":
                count = int(curr_operand) - 1

            elif curr_operator == "20" or curr_operator == "020":
                self.load(curr_operand)

            elif curr_operator == "21" or curr_operator == "021":
                self.store(curr_operand)

            elif curr_operator == "10" or curr_operator == "010":
                address = int(curr_operand)
                self.read(count, address)

            elif curr_operator == "11" or curr_operator == "011":
                address = int(curr_operand)
                self.write(count, address)

            elif curr_operator == "41" or curr_operator == "041":
                if "-" in self._accumulator.get_val():
                    count = int(curr_operand) - 1
            
            elif curr_operator == "42" or curr_operator == "042":
                if int(self._accumulator.get_val()) == 0:
                    count = int(curr_operand) - 1

            elif curr_operator == "30" or curr_operator == "030":
                if int(curr_operand) > self._memory.size() - 1:
                    raise IndexError("Invalid memory address")
                self.add(self._memory._values[int(curr_operand)].get_val())

            #checks if operator is 31, if true executes addition.
            elif curr_operator == "31" or curr_operator == "031":
                if int(curr_operand) > self._memory.size() - 1: #change this into function
                    raise IndexError("Invalid memory address")
                self.subtract(self._memory._values[int(curr_operand)].get_val())

            elif curr_operator == "33" or curr_operator == "033":
                if int(curr_operand) > self._memory.size() - 1:
                    raise IndexError("Invalid memory address")
                self.multiply(self._memory._values[int(curr_operand)].get_val())

            elif curr_operator == "32" or curr_operator == "032":
                if int(curr_operand) > self._memory.size() - 1:
                    raise IndexError("Invalid memory address")
                self.divide(self._memory._values[int(curr_operand)].get_val())
            
            elif (self._memory.size() - 1) == count:
                raise IndexError("No More Executable Instructions")
            
            count += 1
        print(self)

    def resize_memory(self):
        new_list = [Value() if self._memory._legacy else UpdatedValue()] * 250
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
        x = 5 if self._memory._legacy else 7
        if self._memory.size() > count:
            self.resize_memory()
        try:
            user_word = self._input[0]
            self._input.remove(self._input[0])
        except:
            raise ValueError("Invalid Inputs")
        if len(user_word) > x:
            raise ValueError("Command too long")
        if address < 250 and address >= 0:
            self._memory._values[address].set_val(f"{self.sign(user_word)}")
        else:
            raise ValueError("Address not in memory")
        
    def write(self, count, address):
        if self._memory.size() > count:
            self.resize_memory()
        if self._memory._values[address].get_val() == None:
            output = "None"
        elif self._memory._values[address].get_val() != None and count >= 0 and count < 250:
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