from VirtualMachine import *

def main():
    file = str(input("Enter File Name (include .txt): "))
    VM = VirtualMachine(file)
    VM.run()

if __name__ == "__main__":
    main()