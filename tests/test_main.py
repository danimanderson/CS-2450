from main import *

def test_multiply():
    VM = VirtualMachine()
    #assert(VM.get_accumulator() == "2099")
    VM.run()
    assert(VM.get_accumulator() == "0020")

def test_divide():
    VM = VirtualMachine()
    assert(VM.get_accumulator() == "2008")
    VM.run()
    assert(VM.get_accumulator() == "0020")