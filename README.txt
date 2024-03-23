This program is a python program and assumes you use it from VS Code.
In order to launch the GUI from the command line enter: pip install tkinter.
Then from the command line enter: pip install customtkinter.
In order to launch the application from the command line enter: 'py -m main' or 'python3 main.py' (without quotation marks).

Once you run main.py in the terminal you will two  windows that open up. One that has a singular buttonn named "Settings" and another window that has buttons for opening files. 
If you wish to change the color feel free to do so in settings button. You'll have the option to set a primary color and secondary color.
This will only accept hex values, for example #FFFFFF is white in hex. Once you set the colors, do not close out of the settings window.

Now you will navigate to the other window. Here you can open a file anywhere in your computers directory, it must be a .txt file. Once the file is opened up, you can view the file and edit to your liking.
Please keep in mind that you can only have 100 lines of commands in the text file. Once you're happy with your changes, hit assemble and it will open a new window. You can then just click run and it will execute the program.

In the file you will need to have 4 digits instructions. The first two digits will be the operation code specifying the operation to be performed. The last two digits of the four-digit instructions are the operands. 

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

As the program reads the file it will follow the instructions from the file. 
At the end it will print the outputs, the resulting memory and the accumulator or give a reason as to why it wasn't able to complete the instructions in the file.


