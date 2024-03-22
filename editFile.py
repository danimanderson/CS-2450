from tkinter import *
from tkinter import filedialog
import customtkinter
from VirtualMachine import *

class EditFile():
    def __init__(self):
        # Instantiate 
        customtkinter.set_appearance_mode("default")
        customtkinter.set_default_color_theme("settings.json")
        self.gui = customtkinter.CTk()
        #frame = customtkinter.CTkFrame(master=self.gui)
        #frame.pack(pady=20, padx=60, fill="both", expand=True)
        # Setting size of the gui
        self.gui.geometry("500x600")
        self.text_box = Text(self.gui, width=40, height=20)
        self.text_box.pack(pady=12, padx=10)
        self.file_to_open = None
        self.root = None

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

    def assemble(self):
        if self.root != None:
            self.root.destroy()
        #Sets light or dark mode
        customtkinter.set_appearance_mode("default")
        customtkinter.set_default_color_theme("settings.json")
        #Initalizes tkinter
        self.root = customtkinter.CTk()
        root = self.root

        #Sets screen size
        root.geometry("500x600")
        root.title(f"UVSimulator - File")

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="UVSim - Run File", text_color = "white")
        label.pack(pady=12, padx=10)

        #entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter File Name")
        #entry1.pack(pady=12, padx=10)

        entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Inputs Ex. 1234, 3245")
        entry2.pack(pady=12, padx=10)

        def run():  # Use nonlocal to modify the outer scope variable
            # Creates Obj
            label2.configure(text = "")
            file_text = self.file_to_open


            #with open(file_text, "r") as file:
                #file_data = file.readlines()
            #if len(file_data) < 100:  
            VM = VirtualMachine(file_text)
            VM.set_inputs(entry2.get())
            
            valid, required_inputs = VM.validate_inputs()

            if valid == False:
                label2.configure(text = f"Error: This file requires {required_inputs} inputs.")
            else:
                try:
                    VM.run()
                except FileNotFoundError:
                    assert False, label2.configure(text = "File is not found!")
                except ValueError:
                    assert False, label2.configure(text = "Invalid input!")
                except IndexError:
                    assert False, label2.configure(text = "Invalid memory address or no \n more executable instructions!")
                
                label2.configure(text = VM.get_output())
                label3.configure(text = VM)
            #root.destroy()

        # button 1 is a "run" button that will execute the "run" function.
        button = customtkinter.CTkButton(master=frame, text="Run", command=run)
        button.pack(pady=12, padx=10)

        # button 2 is a quit button. The text="Quit" displays the button and the "command" terminates the gui
        button2 = customtkinter.CTkButton(master=frame, text="Quit", command=root.destroy)
        button2.pack(pady=12, padx=10)

        frame2 = customtkinter.CTkScrollableFrame(frame, orientation="vertical", width=200, height=300)
        frame2.pack(pady=40)

        label2 = customtkinter.CTkLabel(frame2, text="")
        label2.pack()

        label3 = customtkinter.CTkLabel(frame2, text="")
        label3.pack()

        # entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Output")
        # entry2.pack(pady=12, padx=10)
        root.mainloop()
    
    def create_gui(self):
        label = customtkinter.CTkLabel(self.gui, text="UVSim - Editor", text_color = "white")
        label.pack(pady=12, padx=10)
        # Creating the open file button  upon click of the button, the "command" area executes the save file function
        open_button = customtkinter.CTkButton(self.gui, text="Open File", command=self.open_file)
        open_button.pack(pady=12, padx=10)
        # Creating the save button, upon click of the button, the "command" area executes the save file function
        save_button = customtkinter.CTkButton(self.gui, text="Save", command=self.save_file)
        save_button.pack(pady=12, padx=10)

        # Creating the save button, upon click of the button, the "command" area executes the save file function
        save_button = customtkinter.CTkButton(self.gui, text="Assemble", command=self.assemble)
        save_button.pack(pady=12, padx=10)
        
        #executes the gui
        self.gui.mainloop()
        
        


