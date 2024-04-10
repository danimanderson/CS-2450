from Value import *

class Memory:
    def __init__(self, file):
        self._values = []
        self._file = file
        self._legacy = False
        if self._file != None:
            with open(self._file, "r")  as file:
                for line in file:
                    line_len = len(line.strip("\n").strip(" "))
                    if line_len < 6:
                        self._legacy = True
                        self._values.append(Value(line.strip("\n").strip(" ")))
                    elif line_len > 6:
                         self._legacy = False
                         self._values.append(UpdatedValue(line.strip("\n").strip(" ")))
                    else:
                         raise ValueError(f"Invalid input in file. {line}")

    def size(self):
            return len(self._values)
    
    def get_values(self):
         return self._values