class VirtualMachine:
    def __init__(self, file = None):
        self._memory = []
        self._accumulator = "0000"
        self._file = file
        if self._file != None:
            with open(file, "r") as file:
                for line in file:
                    self._memory.append(line.strip("+").strip("\n"))

    def get_memory(self):
        return self._memory
    
    def get_accumulator(self):
        return self._accumulator

    def __str__(self):
        text = "\n------------------------\n"
        text += "Resulting Memory:\n"
        for i in self._memory:
            text += f"{i},\n"
        text += "\nAccumulator:\n"
        text += self.get_accumulator()
        text += "\n------------------------\n"
        return text
    
    def run(self):
        # Iterating through memory and performing corresponding opperations

        count = 0
        while True:
            curr = self._memory[count][0:2]                

            if curr == "43":
                # Halt the program
                break

            elif curr == "40":
                # Branch to a different location in memory
                count = int(self._memory[count][2:4]) - 1

            elif curr == "20":
                self.load(self._memory[count][2:4])

            elif curr == "21":
                self.store(self._memory[count][2:4])
            
            elif curr == "30":
                #if first two numbers are 30 it excutes the adding function
                if int(self._memory[count][2:4]) > len(self._memory) - 1:
                    raise IndexError("Invalid Memory Address")
                self.add(self._memory[int(self._memory[count][2:4])])
            
            elif curr == "31":
                #if first two numbers are 31 executes the subtraction function
                if int(self._memory[count][2:4]) > len(self._memory) - 1:
                    raise IndexError("Invalid Memory Address")
                self.subtract(self._memory[int(self._memory[count][2:4])])

            elif curr == "33":
                # Checks if memory address is invalid. 
                if int(self._memory[count][2:4]) > len(self._memory) - 1:
                    raise IndexError("Invalid Memory Address")
                # Multiplies nth element by Acc. Value. 
                self.multiply(self._memory[int(self._memory[count][2:4])])

            elif curr == "32":
                # Checks if memory address is invalid. 
                if int(self._memory[count][2:4]) > len(self._memory) - 1:
                    raise IndexError("Invalid Memory Address")
                # Divides nth element by Acc. Value. 
                self.divide(self._memory[int(self._memory[count][2:4])])

            elif curr == "10":
                address = int(self._memory[count][2:])
                self.read(count, address)

            elif curr == '11':
                address = int(self._memory[count][2:])
                self.write(count, address)
            
            elif curr == "41":
                if "-" in self._accumulator:
                    count = int(self._memory[count][2:4]) - 1
                    
            elif curr == "42":
                address = int(self._memory[count][2:])
                count = self.branchzero(address)
            
            elif len(self._memory) == count:
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
            self._memory[address] = user_word
        else:
            raise ValueError("Address not in memory")

    def resize_memory(self): #Fischer
        """helper function to resize memory if needed"""
        new_list = [None] * 100
        for i in range(len(self._memory)):
                new_list[i] = self._memory[i]
        self._memory = new_list


    def write(self, count, address):    #Fischer
        """Triggered by instruction '11'. Write a word from a specific location in memory to the screen"""
        if len(self._memory) > count:
            self.resize_memory()
        if self._memory[address] == None:
            print("None")
        elif self._memory[address] != None and count >= 0 and count < 100:
            print(self._memory[address])
        else:
            raise ValueError("Address not in memory")

    def load(self, i):
        if int(i) > len(self._memory):
            raise IndexError("Invalid Memory Address")
        self._accumulator = self._memory[int(i)]

    def store(self, i):
        if int(i) > len(self._memory):
            raise IndexError("Invalid Memory Address")
        self._memory[int(i)] = self._accumulator

    def add(self, curr):
        self._accumulator = str(int(curr) + int(self._accumulator))
        if len(self.get_accumulator()) > 4:
            raise ValueError("Value Overflow; Accumulator only supports up to 4 digits!")

    def subtract(self, curr):
        self._accumulator = str(int(curr)) - int(self._accumulator)
        if len(self.get_accumulator()) > 4:
            raise ValueError("Value Overflow; Accumulator only supports up to 4 digits!")

    def divide(self, curr):           # Cole

        # Divides the desired value by the amount in the Acc. and leaves the result in the Acc. 
        self._accumulator = str(int(curr) // int(self._accumulator))

        # Adds 0's to ensure the Acc. is always 4 digits.
        while len(self.get_accumulator()) < 4:
            self._accumulator = "0" + self._accumulator

    def multiply(self, curr):         # Cole
        
        # Multiplies the desired value by the amount in the Acc. and leaves result in the Acc.
        self._accumulator = str(int(curr) * int(self._accumulator))

        # Adds 0's to ensure the Acc. is always 4 digits.
        while len(self.get_accumulator()) < 4:
            self._accumulator = "0" + self._accumulator

        # Exception if result is larger than 4 digits.
        if len(self.get_accumulator()) > 4:
            raise ValueError(f"Value Overflow; Accumlulator only supports up to 4 digits.")

    def branchzero(self, address):
        if self._accumulator == '0000':
            return address

def main():
    file = str(input("Enter File Name (include .txt): "))
    VM = VirtualMachine(file)
    VM.run()

if __name__ == "__main__":
    main()
