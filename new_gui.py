import customtkinter
from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor
import change_settings as change
import json
from VirtualMachine import *


class mainGui(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # This will automatically set the theme of your background according to your computer. e.g. light or dark mode
        customtkinter.set_appearance_mode("default")
        # Sets default color theme
        customtkinter.set_default_color_theme("settings.json")
        with open('settings.json', 'r') as fin:
                settings = json.load(fin)

        self.configure(fg_color=settings["CTk"]["fg_color"][0])

        self.title("UVsim")
        self.geometry("1050x700")
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(5, weight=1)

    def make_frame(self):
        # Creates a frame to hold the run button and the text box
        self.text_frame = customtkinter.CTkFrame(master=self, width=500, height=200)
        self.text_frame.grid(row=5, column=1, padx=20, pady=(20, 0), columnspan=2)
    
    def make_textbox(self):
        # This creates the textbox that will hold all the values
        self.textbox = customtkinter.CTkTextbox(master=self.text_frame, width=250, height=300, corner_radius=10)
        self.textbox.grid(row=0, column=0, sticky="nsew")
    
    def make_user_input(self):
        # Creates a user input box when the uvsim needs user input
        self.user_input = customtkinter.CTkEntry(self.text_frame, placeholder_text="Inputs Ex. 1234")
        self.user_input.grid(row=1, column=0, padx=20, pady=20, columnspan=1)
        
    def open_file(self):
        # Function to open files
        self.file_to_open = filedialog.askopenfilename(title="Open File")
        with open(self.file_to_open, 'r') as directory:
            values = directory.read()
            self.textbox.insert(END, values)

    def change_color(self):
        # Pulls up a color wheel and then sets a primary color
        primary_color = askcolor()
        change.change_primary(primary_color[1])
        self.configure(fg_color=primary_color[1])
        self.text_frame.configure(fg_color=primary_color[1])
        
        # Pulls up a color wheel and then sets a secondary color and updates the color of the buttons. It also changes the color of the text to be the same as the primary color
        secondary_color2 = askcolor()
        change.change_secondary(secondary_color2[1])
        self.run_button.configure(fg_color=secondary_color2[1], text_color=primary_color[1])
        self.save_button.configure(fg_color=secondary_color2[1], text_color=primary_color[1])
        self.quit_button.configure(fg_color=secondary_color2[1], text_color=primary_color[1])
        self.change_color_button.configure(fg_color=secondary_color2[1], text_color=primary_color[1])
        self.open_file_button.configure(fg_color=secondary_color2[1], text_color=primary_color[1])
        self.textbox.configure(fg_color=secondary_color2[1], text_color=primary_color[1])
        self.user_input.configure(fg_color=secondary_color2[1], border_color=primary_color[1], text_color=primary_color[1])
        self.reset_color_button.configure(fg_color=secondary_color2[1], text_color=primary_color[1])

        # Refreshes the gui so the colors are applied
        print("Colors have been changed!")
        self.update_idletasks()

    
    def reset_colors(self):
        primary = "#275D38"
        secondary = "#FFFFFF"
        change.reset_colors()

        self.configure(fg_color=primary)
        self.text_frame.configure(fg_color=primary)
        
        self.run_button.configure(fg_color=secondary, text_color=primary)
        self.save_button.configure(fg_color=secondary, text_color=primary)
        self.quit_button.configure(fg_color=secondary, text_color=primary)
        self.change_color_button.configure(fg_color=secondary, text_color=primary)
        self.open_file_button.configure(fg_color=secondary, text_color=primary)
        self.textbox.configure(fg_color=secondary, text_color=primary)
        self.user_input.configure(fg_color=secondary, border_color=primary, text_color=primary)
        self.reset_color_button.configure(fg_color=secondary, text_color=primary)

        print("Colors reset")
        self.update_idletasks()


    def save_file(self):
        # Allows the user to write and save whatever is edited in the texbox to it's original file that was opened
         with open(self.file_to_open, 'w') as file_to_save:
            save = file_to_save.write(self.textbox.get(1.0, END))

    def run(self):
        # file_text = list(self.textbox.get("0.0", "end"))
        file_text = "Test3.txt"
        # print(isinstance(file_text, list))
        inputs = self.user_input.get()
        try:
            VM = VirtualMachine(file_text)
            VM.set_inputs(inputs)
            VM.run()
        except FileNotFoundError:
            assert False, self.textbox.insert("end", "File is not found!")
        except ValueError:
            assert False, self.textbox.insert("end", "Invalid input!")
        except IndexError:
            self.textbox.insert("end", "\n Invalid memory address or no \n more executable instructions!")
            assert False, "\n Invalid memory address or no \n more executable instructions!"
        # Adds the output to the textbox. Newlines for formatting
        self.textbox.insert("end", f"\n \n {VM.get_output()} {VM}")

    def open_file_button(self):
        # Creates the open file button, upon clicking, it will execute the open_file function
        self.open_file_button = customtkinter.CTkButton(self, text="Open File", command=self.open_file)
        self.open_file_button.grid(row=0, column=0, padx=36, pady=10, columnspan=1)
    
    def change_color_button(self):
        # Creates the change color button, upon clicking it will execute the change_color function
        self.change_color_button = customtkinter.CTkButton(self, text="Change Color", command=self.change_color)
        self.change_color_button.grid(row=0, column=1, padx=36, pady=20, columnspan=1)
    
    def save_button(self):
        # Creates the save button, upon clicking it will execute the save function
        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.save_file)
        self.save_button.grid(row=0, column=2, padx=36, pady=20, columnspan=1)

    def quit_button(self):
        # Creates the quit button, upon clicking it will quit the program
        self.quit_button = customtkinter.CTkButton(self, text="Quit", command=self.destroy)
        self.quit_button.grid(row=0, column=3, padx=36, pady=20, columnspan=1)

    def reset_color_button(self):
        self.reset_color_button = customtkinter.CTkButton(self, text="Reset Colors", command=self.reset_colors)
        self.reset_color_button.grid(row=0, column=4, padx=36, pady=20, columnspan=1)
    
    def run_button(self):
        # Creates a run button that will execute the commands in a .txt file
        self.run_button = customtkinter.CTkButton(self.text_frame, text="Run", command=self.run)
        self.run_button.grid(row=2, column=0, padx=20, pady=20, columnspan=1)
    
    def create_gui(self):
        self.open_file_button()
        self.change_color_button()
        self.save_button()
        self.quit_button()
        self.make_frame()
        self.make_textbox()
        self.run_button()
        self.make_user_input()
        self.reset_color_button()
        self.mainloop()

def main():
    gui = mainGui()
    gui.create_gui()

if __name__ == "__main__":
    main()


