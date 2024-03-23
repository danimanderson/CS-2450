from VirtualMachine import *
import pytest
import json
import change_settings as cng

def test_multiply():
    VM = VirtualMachine()

    # Sets Acc. to 0002 and gets multiplied by the 1st item in memory which is 0002 to form 0004 in the Acc.
    # This test ensures that accumulator is always 4 digits
    VM._memory._values = [Value("+0000"), Value("+0002"), Value("+3301"), Value("+0000"), Value("+4300")]
    VM._accumulator = Value("+0002")
    VM.run()
    assert(VM._accumulator.get_val() == "+0004")

def test_multiply2():
    VM = VirtualMachine()

    # Sets Acc. to 0002 and gets multiplied by the 1st item in memory which is 0002 to form 0004 in the Acc.
    VM._memory._values = [Value("+0000"), Value("+0002"), Value("+3301"), Value("+0000"), Value("+4300")]
    VM._accumulator = Value("+1000")
    VM.run()
    assert(VM._accumulator.get_val() == "+2000")

def test_multiply3():
    VM = VirtualMachine()
    
    #Sets Acc. to 9999 and gets multiplied by the 0th item in memort to throw a ValueError (Value Overflow as Acc. == 10,088,991)
    lyst = ["+5212", "+0000", "+3300", "+0000", "+4300"]
    VM._memory._values = [Value(i) for i in lyst]
    VM._accumulator = Value("+5212")
    VM.run()
    assert(VM._accumulator.get_val() == "+4944")

def test_multiply4():
    VM = VirtualMachine()
    # Attempts to multiply the 99th element but throws a IndexError (Memory Address 99 out of range)
    lyst = ["+0000", "+0000", "+3399", "+4300"]
    VM._memory._values = [Value(i) for i in lyst]
    VM._accumulator = Value("+9999")
    with pytest.raises(IndexError):
        VM.run()


def test_divide():
    VM = VirtualMachine()

    # Sets Acc. to 0002 and divdes Acc. by the 1st element which is 0050, leaving 0025 in the Acc.
    lyst = ["+0000", "+0002", "+3201", "+4300"]
    VM._memory._values = [Value(i) for i in lyst]
    VM._accumulator.set_val("+0050")
    VM.run()
    assert(VM._accumulator.get_val() == "+0025")

def test_divide2():
    VM = VirtualMachine()
    # Attempts to use the 99th element but throws a Index Error.
    lyst = ["+0000", "+0000", "+3299", "+4300"]
    VM._memory._values = [Value(i) for i in lyst]
    VM._accumulator = Value("+0002")
    with pytest.raises(IndexError):
        VM.run()

def test_branch():
    VM = VirtualMachine()

    # Branches to the 4th item in memory to divide 16 // 2, then halts 
    lyst = ["+0000", "+0002", "+4004", "+4300", "+3201", "+4300"]
    VM._memory._values = [Value(i) for i in lyst]
    VM._accumulator = Value("+0016")
    VM.run()
    assert(VM._accumulator.get_val() == "+0008")

def test_branch2():
    VM = VirtualMachine()

    # Branches to the 6th location and throws error
    lyst = ["+0000", "+0016", "+4006", "+4300", "+3201", "+4300"]
    VM._memory._values = [Value(i) for i in lyst]
    VM._accumulator = Value("+0002")
    with pytest.raises(IndexError):
        VM.run()

def test_load():
    vm = VirtualMachine()

    #sets the accumulator to the 2nd index in memory
    lyst = ["+2002", "+0000", "+9899", "+4300"]
    vm._memory._values = [Value(i) for i in lyst]
    vm.run()
    assert vm._accumulator.get_val() == "+9899"

def test_load2():
    vm = VirtualMachine()
    #checks if resize mem works
    lyst = ["+2099", "+0000", "+9899", "+4300"]
    vm._memory._values = [Value(i) for i in lyst]
    assert vm._accumulator.get_val() == "+0000"

def test_store():
    vm = VirtualMachine()

    #Sets the memory in the 2nd index to the index
    vm._accumulator = Value("+9999")
    lyst = ["+2101", "+0000", "+1234", "+4300"]
    vm._memory._values = [Value(i) for i in lyst]
    vm.run()
    assert vm._memory._values[1].get_val() == "+9999"

def test_store2():
    vm = VirtualMachine()
    #Checks that resize mem works.
    vm._accumulator = Value("+4321")
    lyst = ["+2199", "+0000", "+1234", "+0000", "+0000", "+0000"]
    vm._memory._values = [Value(i) for i in lyst]
    vm.run()
    assert vm._memory._values[99].get_val() == "+4321"

def test_add():
    # 3001 runs the aadd
    # Ensures Acc. is always 4 digits
    vm = VirtualMachine()
    vm._accumulator = Value("+0002")
    lyst = ["+0000", "+0006", "+3001", "+4300"]
    vm._memory._values = [Value(i) for i in lyst]
    vm.run()
    assert vm._accumulator.get_val()== "+0008"

def test_add2():
    # 3001 runs the aadd
    vm = VirtualMachine()
    vm._accumulator = Value("+1000")
    lyst = ["+0000", "+6000", "+3001", "+4300"]
    vm._memory._values = [Value(i) for i in lyst]
    vm.run()
    assert vm._accumulator.get_val() == "+7000"


def test_subtract():
    vm = VirtualMachine()

    #Ensures Acc. is always 4 digits
    vm._accumulator = Value("+0008")
    lyst = ["+0000", "+0002", "+3101", "+4300"]
    vm._memory._values = [Value(i) for i in lyst]
    vm.run()
    assert vm._accumulator.get_val() == "+0006"

def test_subtract2():
    vm = VirtualMachine()

    # Tests subtract
    vm._accumulator = Value("+5000")
    lyst = ["+0000", "+6000", "+3101", "+4300"]
    vm._memory._values = [Value(i) for i in lyst]
    vm.run()
    assert vm._accumulator.get_val() == "-1000"

def test_negBranch():
    vm = VirtualMachine()
    lyst = ["+0000", "+0008", "+4104", "+4300", "+3001", "+4300"]
    vm._memory._values = [Value(i) for i in lyst]
    vm._accumulator = Value("-0008")
    vm.run()
    assert vm._accumulator.get_val() == "+0000"

def test_read(): #Fischer
    VM = VirtualMachine()
    VM._input = ['1234', '2345']
    lyst = ['+1007', '+1008', '+2007', '+2008', '+2109', '+1109', '+4300']
    VM._memory._values = [Value(i) for i in lyst]
    VM.run()
    assert VM._memory._values[7].get_val() == '+2345'

def test_write():
    VM = VirtualMachine()
    VM._input = ['1234', '2345']
    lyst = ['+1007', '+2007', '+2008', '+2109', '+1109', '+4300']
    VM._memory._values = [Value(i) for i in lyst]
    VM.run()
    assert VM.write(0, 7) == "+1234"

def test_branchzero():
    VM = VirtualMachine()
    lyst = ["+4202","+4301", "+0000"]
    VM._memory._values = [Value(i) for i in lyst]
    with pytest.raises(IndexError):
        VM.run()

def test_negBranch2():
    vm = VirtualMachine()
    lyst = ["+0000", "+0008", "+4104", "+4300", "+3001", "+4300"]
    vm._memory._values = [Value(i) for i in lyst]
    vm._accumulator = Value("-0007")
    vm.run()
    assert vm._accumulator.get_val() == "+0001"

def test_read2(): #Fischer
    VM = VirtualMachine()
    VM._input = ['1234', '2345']
    lyst = ['+1008', '+1008', '+2007', '+2008', '+2109', '+1109', '+4300']
    VM._memory._values = [Value(i) for i in lyst]
    VM.run()
    assert VM._memory._values[8].get_val() == '+2345'

def test_write2():
    VM = VirtualMachine()
    VM._input = ['1234', '2345']
    lyst = ['+1008', '+2007', '+2008', '+2109', '+1109', '+4300']
    VM._memory._values = [Value(i) for i in lyst]
    VM.run()
    assert VM.write(0, 8) == "+1234"

def test_branchzero2():
    VM = VirtualMachine()
    lyst = ["+4202", "+4300", "+3000", "+4300"]
    VM._memory._values = [Value(i) for i in lyst]
    VM._accumulator = Value("+0000")
    VM.run()
    assert VM._accumulator.get_val() == "+4202"

def test_change_primary():
    cng.change_primary("#ABCDEF")
    with open('settings.json', 'r') as fin:
        settings = json.load(fin)

    assert settings["CTk"]["fg_color"] == ["#ABCDEF", "#ABCDEF"]

def test_change_secondary():
    cng.change_secondary("#EEEEEE")
    with open('settings.json', 'r') as fin:
        settings = json.load(fin)

    assert settings["CTkFrame"]["top_fg_color"] == ["#EEEEEE", "#EEEEEE"]

def test_reset():
    cng.reset_colors()
    with open('settings.json', 'r') as fin:
        settings = json.load(fin)

    assert settings["CTk"]["fg_color"] == ["#275D38", "#275D38"] and settings["CTkFrame"]["top_fg_color"] == ["#FFFFFF", "#FFFFFF"]



