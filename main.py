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

            elif len(self._memory) == count:
                # Check if there are more instructions. 
                raise IndexError("No More Executable Instructions")
            
            count += 1
        print(self)

    def read(self):
        pass

    def write(self):
        pass

    def load(self, i):
        """Triggered by instruction '20'. Grabs number from a specific point in memory and puts it into accumulator"""
        self._accumulator = self._memory[int(i)]

    def store(self, i):
        """Triggered by instruction '21'. Grabs number from the accumulator and puts it into a specific point in memory."""
        self._memory[int(i)] = self._accumulator

    def add(self):
        pass

    def subtract(self):
        pass

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

def main():
    VM = VirtualMachine()
    VM.run()

if __name__ == "__main__":
    main()