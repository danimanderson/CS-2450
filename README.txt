This program is a python program and assumes you use it from VS Code.
In order to launch the application from the command line: py -m main.

You will need a file named Test2.txt. If you want it to use a different file, on line 5 it specifies which txt file to use, change that file name if you want to change which file it reads from.
In that file you will need to have 4 digits instructions. The first two digits will be the operation code specifying the operation to be performed. The last two digits of the four-digit instructions are the operands. 
The following is the allotted operations:

I/O operation:
READ = 10 Read a word from the keyboard into a specific location in memory.
WRITE = 11 Write a word from a specific location in memory to screen.

Load/store operations:
LOAD = 20 Load a word from a specific location in memory into the accumulator.
STORE = 21 Store a word from the accumulator into a specific location in memory.

Arithmetic operation:
ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
SUBTRACT = 31 Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
DIVIDE = 32 Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).
MULTIPLY = 33 multiply a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator).

Control operation:
BRANCH = 40 Branch to a specific location in memory
BRANCHNEG = 41 Branch to a specific location in memory if the accumulator is negative.
BRANCHZERO = 42 Branch to a specific location in memory if the accumulator is zero.
HALT = 43 Stop the program

As the program reads the file it will follow the instructions from the file. At the end it will print the resulting memory and the accumulator.  
