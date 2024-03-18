import customtkinter
import tkinter as tk

class SettingGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.primary_color = "#275D38"
        self.secondary_color = "#FFFFFF"

        self.geometry("250x300")
        self.title("UVSimulator Settings")

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.label = customtkinter.CTkLabel(master=self.frame, text="Settings")
        self.label.pack(pady=12, padx=10)

        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter Primary Color")
        self.entry1.pack(pady=12, padx=10)

        self.prim_button = customtkinter.CTkButton(master=self.frame, text="Set", command=self.set_primary)
        self.prim_button.pack(pady=12, padx=10)

        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter Secondary Color")
        self.entry2.pack(pady=12, padx=10)

        self.sec_button = customtkinter.CTkButton(master=self.frame, text="Set", command=self.set_secondary)
        self.sec_button.pack(pady=12, padx=10)

    def ErrorDisplay(self, error_code):
        if error_code == 1:
            error_message = "Needs 6 characters in hex code"
        elif error_code == 2:
            error_message = "Character in Hex Value is not valid"

        tk.messagebox.showinfo("Error", error_message)

    def hex_code_check(self, color):
        hex_code_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                         'a', 'b', 'c', 'd', 'e', 'f', 
                         'A', 'B', 'C', 'D', 'E', 'F']

        if color[0] != "#":
            color = "#" + color

        if len(color) != 7:
            return 1  # Error code for "Needs 7 characters"

        for i in range(1, len(color)):
            if color[i] not in hex_code_list:
                return 2  # Error code for "Character in Hex Value is not valid"

        return color

    def set_primary(self):
        prim_color = self.entry1.get()
        prim_color = self.hex_code_check(prim_color)
        if isinstance(prim_color, int):
            self.ErrorDisplay(prim_color)
            return  # Exit the method if there's an error
        self.primary_color = prim_color

    def set_secondary(self):
        sec_color = self.entry2.get()
        sec_color = self.hex_code_check(sec_color)
        if isinstance(sec_color, int):
            self.ErrorDisplay(sec_color)
            return  # Exit the method if there's an error
        self.secondary_color = sec_color

def main():
    settingsGui = SettingGUI()
    settingsGui.mainloop()

if __name__ == "__main__":
    main()
