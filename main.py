class VirtualMachine:
    def __init__(self):
        self._memory = []
        self._accumulator = "0000"
        with open("Test2.txt", "r") as file:
            for line in file:
                self._memory.append(line.strip("+").strip("\n"))

    def get_memory(self):
        return self._memory
    
    def get_accumulator(self):
        return self._accumulator

    def __str__(self):
        text = "------------------------\n"
        text += "Memory:\n"
        for i in self._memory:
            text += f"{i},\n"
        text += "\nAccumulator:\n"
        text += self.get_accumulator()
        text += "\n------------------------\n"
        return text
    
    def run(self):
        count = 0
        while True:
            curr = self._memory[count][0:2]

            if curr == "43":
                break
            elif curr == "33":
                self.multiply(self._memory[int(self._memory[count][2:4])])
            elif curr == "32":
                self.divide(self._memory[int(self._memory[count][2:4])])
            elif curr == "40":
                count = int(self._memory[count][2:4]) - 1
            elif curr == "10":
                address = int(self._memory[count][2:])
                self.read(count, address)
            elif curr == '11':
                address = int(self._memory[count][2:])
                self.write(count, address)
            elif curr == "42":
                address = int(self._memory[count][2:])
                count = branchzero(address)
            elif len(self._memory) == count:
                raise IndexError("No More Executable Instructions")
            
            count += 1
        print(self)

        """
        for i in range(0, len(self._memory)):
            curr = self._memory[i][0:2]
            if curr == "43":
                break
            elif curr == "33":
                self.multiply(self._memory[int(self._memory[i][2:4])])
            elif curr == "32":
                self.divide(self._memory[int(self._memory[i][2:4])])
            elif curr == "40":
                curr = 
        print(self)"""

    def write(self, count, address): #Fischer
        """Triggered by instruction '11'. Write a word from a specific location in memory to screen""" 
        if len(self._memory) > count:
            self.resize_memory() 
        if self._memory[address] == None:
            print("None")
        elif self._memory[address] != None and count >= 0 and count < 100:
            print(self._memory[address])
        else:
            raise ValueError("Address not in memory")
    

    def resize_memory(self): #Fischer
        """helper function to resize memory if needed"""
        new_list = [None] * 100
        for i in range(len(self._memory)):
                new_list[i] = self._memory[i]
        self._memory = new_list


    def read(self, count, address):    #Fischer
        """Triggered by instruction '10'. Read a word form the keyboard into a specific location in memory"""
        if len(self._memory) > count:
            self.resize_memory()
        user_word = input("Enter a 4-digit command (Digits 0-9 only): ")
        if len(user_word) > 4:
            raise ValueError("Command too long")
        if address < 100 and address >= 0:
            self._memory[address] = user_word
        else:
            raise IndexError("Segmentation fault. Cannot write to that memory address")

    def load(self):
        pass

    def store(self):
        pass

    def add(self):
        pass

    def subtract(self):
        pass

    def divide(self, curr):
        self._accumulator = str(int(curr) // int(self._accumulator))
        while len(self.get_accumulator()) != 4:
            self._accumulator = "0" + self._accumulator

    def multiply(self, curr):
        self._accumulator = str(int(curr) * int(self._accumulator))
        while len(self.get_accumulator()) < 4:
            self._accumulator = "0" + self._accumulator
        if len(self.get_accumulator()) > 4:
            raise ValueError(f"Value Overflow; Accumlulator only supports up to 4 digits.")

    def branchzero(self, address):
        """Triggered by instruction '42'. If accumulator is 0, branch to a specific memory address"""
        if self._accumulator == '0000':
            return address


def main():
    cole = VirtualMachine()
    cole.run()


if __name__ == "__main__":
    main()
