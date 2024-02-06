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

    def read(self):
        pass

    def write(self):
        pass

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

def main():
    cole = VirtualMachine()
    cole.run()


if __name__ == "__main__":
    main()