import customtkinter
from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor
import change_settings as change
import json
from VirtualMachine import *

class RequiredInputPopUp(customtkinter.CTkToplevel):
    def __init__(self, invalid_inputs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.invaid = invalid_inputs
        customtkinter.set_default_color_theme("settings.json")
        with open('settings.json', 'r') as fin:
                settings = json.load(fin)

        self.configure(fg_color=settings["CTk"]["fg_color"][0])

        self.title("UVsim")
        self.geometry("310x200")
        self.label = customtkinter.CTkLabel(self, text=f"{self.invaid} inputs are required!\n Please enter in input box. \n(Ex: 1234, 5678, etc) then run", font=("arial", 20), text_color="white")
        self.label.pack(padx=20, pady=20)
