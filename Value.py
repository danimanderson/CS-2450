class Value:
    def __init__(self, val = "+0000"):
        self._val = val

    def operator(self):
        return self._val[1:3]
    
    def operand(self):
        return self._val[3:]
    
    def get_val(self):
        return self._val
    
    def set_val(self, new):
        self._val = new

class UpdatedValue:
    def __init__(self, val = "+000000"):
        self._val = val

    def operator(self):
        return self._val[1:4]
    
    def operand(self):
        return self._val[4:]
    
    def get_val(self):
        return self._val
    
    def set_val(self, new):
        self._val = new
