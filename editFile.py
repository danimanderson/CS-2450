from tkinter import *
from tkinter import filedialog

class EditFile():
    def __init__(self):
        # Instantiate tkinter
        self.gui = Tk()
        # Setting size of the gui
        self.gui.geometry("500x600")
        self.text_box = Text(self.gui, width=40, height=10)
        self.text_box.pack(pady=20)

    def open_file(self):
        # Function to open files
        self.file_to_open = filedialog.askopenfilename(title="Open File")
        with open(self.file_to_open, 'r') as directory:
            values = directory.read()
            self.text_box.insert(END, values)
    
    def save_file(self):
        # Function to save files
        with open(self.file_to_open, 'w') as file_to_save:
            save = file_to_save.write(self.text_box.get(1.0, END))
    
    def create_gui(self):
        # Creating the open file button  upon click of the button, the "command" area executes the save file function
        open_button = Button(self.gui, text="Open File", command=self.open_file)
        open_button.pack(pady=20)
        # Creating the save button, upon click of the button, the "command" area executes the save file function
        save_button = Button(self.gui, text="Save", command=self.save_file)
        save_button.pack(pady=20)
        
        #executes the gui
        self.gui.mainloop()


def main():
    file_editor = EditFile()
    file_editor.create_gui()

if __name__ == "__main__":
    main()
        
        


