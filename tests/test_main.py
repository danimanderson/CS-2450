import pytest, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main



def test_multiply():
    VM = main.VirtualMachine()
    #assert(VM.get_accumulator() == "2099")
    VM.run()
    assert(VM.get_accumulator() == "0020")

def test_divide():
    VM = main.VirtualMachine()
    assert(VM.get_accumulator() == "2008")
    VM.run()
    assert(VM.get_accumulator() == "0020")

def test_read(monkeypatch): #Fischer
    inputs = iter(['1234', '2345'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    VM = main.VirtualMachine()
    VM.run()
    assert VM._memory[9] == '1234'
    assert VM._memory[10] == '2345'

