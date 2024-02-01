from main import *

VM = VirtualMachine()

def test_accumulator():
    assert(VM.get_accumulator() == "0000")