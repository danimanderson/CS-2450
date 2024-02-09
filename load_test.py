from main import *


def load_test_1():
    vm = VirtualMachine()
    vm._memory = ["1002", "0000", "9899"]
    vm.run()
    assert vm._accumulator == "9899"

def load_test_2():
    vm = VirtualMachine()
    vm._memory = ["1000", "0000", "9899", "0000", "0000", "0000"]
    vm.run()
    assert vm.get_accumulator() == "1000"

def store_test_1():
    vm = VirtualMachine()
    vm._accumulator = "9999"
    vm._memory = ["1102", "0000", "1234", "0000", "0000", "0000"]
    vm.run()
    assert vm.get_memory() == ["1102", "0000", "9999", "0000", "0000", "0000"]

def store_test_2():
    vm = VirtualMachine()
    vm._accumulator = "4321"
    vm._memory = ["1100", "0000", "1234", "0000", "0000", "0000"]
    vm.run()
    assert vm.get_memory() == ["4321", "0000", "1234", "0000", "0000", "0000"]

load_test_1()
load_test_2()