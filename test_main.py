from main import *
import pytest

def test_multiply():
    VM = VirtualMachine()

    # Sets Acc. to 0002 and gets multiplied by the 1st item in memory which is 0002 to form 0004 in the Acc.
    # This test ensures that accumulator is always 4 digits
    VM._memory = ["0000", "0002", "3301", "0000", "4300"]
    VM._accumulator = "0002"
    VM.run()
    assert(VM.get_accumulator() == "0004")

def test_multiply2():
    VM = VirtualMachine()

    # Sets Acc. to 0002 and gets multiplied by the 1st item in memory which is 0002 to form 0004 in the Acc.
    VM._memory = ["0000", "0002", "3301", "0000", "4300"]
    VM._accumulator = "1000"
    VM.run()
    assert(VM.get_accumulator() == "2000")

def test_multiply3():
    VM = VirtualMachine()
    #Sets Acc. to 9999 and gets multiplied by the 0th item in memort to throw a ValueError (Value Overflow as Acc. == 10,088,991)
    VM._memory = ["9999", "0000", "3300", "0000", "4300"]
    VM._accumulator = "9999"
    VM.run()
    assert(VM._accumulator == "0001")

def test_multiply4():
    VM = VirtualMachine()
    # Attempts to multiply the 99th element but throws a IndexError (Memory Address 99 out of range)
    VM._memory = ["0000", "0000", "3399", "4300"]
    VM._accumulator = "9999"
    with pytest.raises(IndexError):
        VM.run()


def test_divide():
    VM = VirtualMachine()

    # Sets Acc. to 0002 and divdes Acc. by the 1st element which is 0050, leaving 0025 in the Acc.
    VM._memory = ["0000", "0050", "3201", "4300"]
    VM._accumulator = "0002"
    VM.run()
    assert(VM.get_accumulator() == "0025")

def test_divide2():
    VM = VirtualMachine()
    # Attempts to use the 99th element but throws a Index Error.
    VM._memory = ["0000", "0000", "3299", "4300"]
    VM._accumulator = "0002"
    with pytest.raises(IndexError):
        VM.run()

def test_branch():
    VM = VirtualMachine()

    # Branches to the 4th item in memory to divide 16 // 2, then halts 
    VM._memory = ["0000", "0016", "4004", "4300", "3201", "4300"]
    VM._accumulator = "0002"
    VM.run()
    assert(VM._accumulator == "0008")

def test_branch2():
    VM = VirtualMachine()

    # Branches to the 6th location and throws error
    VM._memory = ["0000", "0016", "4006", "4300", "3201", "4300"]
    VM._accumulator = "0002"
    with pytest.raises(IndexError):
        VM.run()

def test_load():
    vm = VirtualMachine()

    #sets the accumulator to the 2nd index in memory
    vm._memory = ["2002", "0000", "9899", "4300"]
    vm.run()
    assert vm._accumulator == "9899"

def test_load2():
    vm = VirtualMachine()
    #checks that if memory doesn't exist, it will raise an IndexError
    vm._memory = ["2099", "0000", "9899", "4300"]
    with pytest.raises(IndexError):
        vm.run()

def test_store():
    vm = VirtualMachine()

    #Sets the memory in the 2nd index to the index
    vm._accumulator = "9999"
    vm._memory = ["2101", "0000", "1234", "4300"]
    vm.run()
    assert vm._memory[1] == "9999"

def test_store2():
    vm = VirtualMachine()
    #Checks that if memory doesn't exist, it will raise an IndexError
    vm._accumulator = "4321"
    vm._memory = ["2199", "0000", "1234", "0000", "0000", "0000"]
    with pytest.raises(IndexError):
        vm.run()

def test_add():
    # 3001 runs the aadd
    # Ensures Acc. is always 4 digits
    vm = VirtualMachine()
    vm._accumulator = "0002"
    vm._memory = ["0000", "0006", "3001", "4300"]
    vm.run()
    assert vm.get_accumulator() == "0008"

def test_add2():
    # 3001 runs the aadd
    vm = VirtualMachine()
    vm._accumulator = "1000"
    vm._memory = ["0000", "6000", "3001", "4300"]
    vm.run()
    assert vm.get_accumulator() == "7000"


def test_subtract():
    vm = VirtualMachine()

    #Ensures Acc. is always 4 digits
    vm._accumulator = "0002"
    vm._memory = ["0000", "0008", "3101", "4300"]
    vm.run()
    assert vm.get_accumulator() == "0006"

def test_subtract2():
    vm = VirtualMachine()

    # Tests subtract
    vm._accumulator = "5000"
    vm._memory = ["0000", "6000", "3101", "4300"]
    vm.run()
    assert vm.get_accumulator() == "1000"

def test_negBranch():
    vm = VirtualMachine()
    vm._memory = ["0000", "0008", "4104", "4300", "3001", "4300"]
    vm._accumulator = "-0008"
    vm.run()
    assert vm._accumulator == "0000"

def test_read(monkeypatch): #Fischer
    inputs = iter(['1234', '2345'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    VM = VirtualMachine()
    VM._memory = ['1007', '1008', '2007', '2008', '2109', '1109', '4300']
    VM.run()
    assert VM._memory[7] == '1234'

def test_write(monkeypatch):
    inputs = iter(['1234', '2345'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    VM = VirtualMachine()
    VM._memory = ['1007', '2007', '2008', '2109', '1109', '4300']
    VM.run()
    assert VM.write(0, 7) == "1234"

def test_branchzero():
    VM = VirtualMachine()
    VM._memory = ["4301", "0000"]
    VM.run()
    assert VM.branchzero(int("01")) == 1

def test_negBranch2():
    vm = VirtualMachine()
    vm._memory = ["0000", "0008", "4104", "4300", "3001", "4300"]
    vm._accumulator = "-0007"
    vm.run()
    assert vm._accumulator == "0001"

def test_read2(monkeypatch): #Fischer
    inputs = iter(['1234', '2345'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    VM = VirtualMachine()
    VM._memory = ['1008', '1008', '2007', '2008', '2109', '1109', '4300']
    VM.run()
    assert VM._memory[8] == '2345'

def test_write2(monkeypatch):
    inputs = iter(['1234', '2345'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    VM = VirtualMachine()
    VM._memory = ['1008', '2007', '2008', '2109', '1109', '4300']
    VM.run()
    assert VM.write(0, 8) == "1234"

def test_branchzero2():
    VM = VirtualMachine()
    VM._memory = ["4302", "0000", "0000", "4300"]
    VM.run()
    assert VM.branchzero(int("02")) ==  2

