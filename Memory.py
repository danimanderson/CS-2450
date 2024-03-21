from Value import *

class Memory:
    def __init__(self, file):
        self._values = []
        self._file = file
        if self._file != None:
            with open(self._file, "r")  as file:
                for line in file:
                    self._values.append(Value(line.strip("\n").strip(" ")))

    def size(self):
            return len(self._values)
    
    def get_values(self):
         return self._values