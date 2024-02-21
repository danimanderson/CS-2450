class VirtualMachine:
    def __init__(self, file = None):
        self._memory = []
        self._accumulator = "+0000"
        self._file = file
        if self._file != None:
            with open(self._file, "r")  as file:
                for line in file:
                    self._memory.append(line.strip("\n").strip(" "))
    
    def operator(self, val):
        return val[1:3]
    
    def operand(self, val):
        return val[3:]
    
    def sign(self, val):
        if int(val) == 0:
            return "+0000"
        if int(val) > 0:
            if len(val) == 4:
                return "+" + val
            elif len(val) < 4:
                while len(val) != 4:
                    val = "0" + val
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
    
    def get_memory(self):
        return self._memory
    
    def get_accumulator(self):
        return self._accumulator
    
    def __str__(self):
        text = "\n------------------------\n"
        text += "Resulting Memory:\n"
        for i in self._memory:
            text += f"{i}\n"
        text += "\nAccumulator:\n"
        text += self.get_accumulator()
        text += "\n------------------------\n"
        return text
    
    def run(self):
        count = 0
        while True:
            curr_operator = self.operator(self._memory[count])
            curr_operand = self.operand(self._memory[count])

            if curr_operator == "43":
                # Halt the program
                break

            elif curr_operator == "40":
                # Branch to a different location in memory
                count = int(curr_operand) - 1

            elif curr_operator == "20":
                self.load(curr_operand)

            elif curr_operator == "21":
                self.store(curr_operand)
            
            elif curr_operator == "30":
                #if first two numbers are 30 it excutes the adding function
                if int(curr_operand) > len(self._memory) - 1:
                    raise IndexError("Invalid Memory Address")
                self.add(self._memory[int(curr_operand)])
            
            elif curr_operator == "31":
                #if first two numbers are 31 executes the subtraction function
                if int(curr_operand) > len(self._memory) - 1:
                    raise IndexError("Invalid Memory Address")
                self.subtract(self._memory[int(curr_operand)])

            elif curr_operator == "33":
                # Checks if memory address is invalid. 
                if int(curr_operand) > len(self._memory) - 1:
                    raise IndexError("Invalid Memory Address")
                # Multiplies nth element by Acc. Value. 
                self.multiply(self._memory[int(curr_operand)])

            elif curr_operator == "32":
                # Checks if memory address is invalid. 
                if int(curr_operand) > len(self._memory) - 1:
                    raise IndexError("Invalid Memory Address")
                # Divides nth element by Acc. Value. 
                self.divide(self._memory[int(curr_operand)])

            elif curr_operator == "10":
                address = int(curr_operand)
                self.read(count, address)

            elif curr_operator == '11':
                address = int(curr_operand)
                self.write(count, address)
            
            elif curr_operator == "41":
                if "-" in self._accumulator:
                    count = int(curr_operand) - 1
            
            elif curr_operator == '11':
                address = int(curr_operand)
                self.write(count, address)
            
            elif curr_operator == "42":
                if int(self._accumulator) == 0:
                    count = int(curr_operand) - 1

            elif len(self._memory) - 1 <= count:
                # Check if there are more instructions. 
                raise IndexError("No More Executable Instructions")
            
            count += 1
        print(self)

    def read(self, count, address): #Fischer
        """Triggered by instruction '10'. Reads a word from the keyboard in to a specific location in memory"""
        if len(self._memory) > count:
            self.resize_memory()
        user_word = input("Enter a 4-digit command (Digits 0-9 only): ")
        if len(user_word) > 4:
            raise ValueError("Command too long")
        if address < 100 and address >= 0:
            self._memory[address] = f"+{user_word}"
        else:
            raise ValueError("Address not in memory")
    

    def write(self, count, address): #Fischer
        """Triggered by instruction '11'. Write a word from a specific location in memory to screen""" 
        if len(self._memory) > count:
            self.resize_memory() 
        if self._memory[address] == None:
            output = "None"
        elif self._memory[address] != None and count >= 0 and count < 100:
            output = self._memory[address]
        else:
            raise ValueError("Address not in memory")
        print(output)
        return output

    def resize_memory(self): #Fischer
        """helper function to resize memory if needed"""
        new_list = ["+0000"] * 100
        for i in range(len(self._memory)):
                new_list[i] = self._memory[i]
        self._memory = new_list

    
    def load(self, i):
        if len(self._memory) > int(i):
            self.resize_memory() 
        self._accumulator = self._memory[int(i)]

    
    def store(self, i):
        if len(self._memory) > int(i):
            self.resize_memory() 
        self._memory[int(i)] = self._accumulator

    
    def add(self, curr):
        self._accumulator = self.sign(str(int(curr) + int(self._accumulator)))
        """if len(self.get_accumulator()) > 4:
            self._accumulator = self._accumulator[len(self._accumulator) - 4 : len(self._accumulator)]
        while len(self.get_accumulator()) < 4:
            self._accumulator = "0" + self._accumulator"""

    
    def subtract(self, curr):
        self._accumulator = self.sign(str(int(self._accumulator) - int(curr)))
        """if len(self.get_accumulator()) > 4:
            raise ValueError("Value Overflow; Accumulator only supports up to 4 digits!")
        while len(self.get_accumulator()) < 4:
            self._accumulator = "0" + self._accumulator"""

    
    def divide(self, curr):           # Cole

        # Divides the desired value by the amount in the Acc. and leaves the result in the Acc. 
        self._accumulator = self.sign(str(int(self._accumulator) // int(curr)))

        # Adds 0's to ensure the Acc. is always 4 digits.
        """while len(self.get_accumulator()) < 4:
            self._accumulator = "0" + self._accumulator"""

    
    def multiply(self, curr):         # Cole
        #print(self._accumulator)
        # Multiplies the desired value by the amount in the Acc. and leaves result in the Acc.
        self._accumulator = self.sign(str(int(curr) * int(self._accumulator)))

        # Adds 0's to ensure the Acc. is always 4 digits.
        """while len(self.get_accumulator()) < 4:
            self._accumulator = "0" + self._accumulator

        # Exception if result is larger than 4 digits.
        if len(self.get_accumulator()) > 4:
            self._accumulator = self._accumulator[len(self._accumulator) - 4 : len(self._accumulator)]"""

    def branchzero(self, address):
        if self._accumulator == '0000':
            return address