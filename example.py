class VirtualMachine:
    def __init__(self):
        self._memory = []
        self._accumulator = "0000"
        with open("Test1.txt", "r") as file:
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
        for i in range(0, len(self._memory)):
            curr = self._memory[i][0:2]
            if curr == "43":
                break

        print(self)

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

    def divide(self):
        pass

    def multiply(self):
        pass


def main():
    cole = VirtualMachine()
    cole.run()


if __name__ == "__main__":
    main()