import tkinter
import customtkinter 
import SettingGui
from VirtualMachine import *
from tkinter import colorchooser
from editFile import *
 
# Function that will be invoked when the
# button will be clicked in the main window


def set_colors():
    customtkinter.set_default_color_theme("settings.json")


def call_settings():
    SettingGui.main() 

def main():
    
    #Sets light or dark mode
    customtkinter.set_appearance_mode("default")
    #Sets color of buttons
    customtkinter.set_default_color_theme("settings.json")
    #Initalizes tkinter
    root = customtkinter.CTk()

    #Sets screen size
    root.geometry("500x700")
    root.title("UVSimulator")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="UVSim", text_color="white")
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter File Name")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Inputs Ex. 1234, 3245")
    entry2.pack(pady=12, padx=10)

    def run():  # Use nonlocal to modify the outer scope variable
        # Creates Obj
        file_text = entry1.get()

        try:
            VM = VirtualMachine(file_text)
            VM.set_inputs(entry2.get())
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

    button3 = customtkinter.CTkButton(master=frame, text="Settings", command=call_settings)
    button3.pack(pady=12, padx=10)

    frame2 = customtkinter.CTkScrollableFrame(frame, orientation="vertical", width=200, height=300)
    frame2.pack(pady=40)

    label2 = customtkinter.CTkLabel(frame2, text="")
    label2.pack()

    label3 = customtkinter.CTkLabel(frame2, text="")
    label3.pack()

    
    # entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Output")
    # entry2.pack(pady=12, padx=10)
    file_editor = EditFile()
    file_editor.create_gui()
    root.mainloop()
    

if __name__ == "__main__":
    main()
