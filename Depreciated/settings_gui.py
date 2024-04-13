#this file isn't used in the end
import customtkinter
class SettingGui():
    def __init__(self):
        primary_color = "#275D38"
        secondary_color = "#FFFFFF"

        root = customtkinter.CTk()
        root.geometry("250x300")
        root.title("UVSimulator Settings")

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Settings")
        label.pack(pady=12, padx=10)

        entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Primary Color")
        entry1.pack(pady=12, padx=10)

        prim_button = customtkinter.CTkButton(master=frame, text="Set", command=self.set_primary)
        prim_button.pack(pady=12, padx=10)

        entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Secondary Color")
        entry2.pack(pady=12, padx=10)

        prim_button = customtkinter.CTkButton(master=frame, text="Set", command=self.set_secondary(secondary_color))
        prim_button.pack(pady=12, padx=10)

    def ErrorDisplay(self, error_code):
        print(error_code)
        return input("Try again: ")
    

    def hex_code_check(self, color):
        hex_code_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                            'a', 'b', 'c', 'd', 'e', 'f', 
                            'A', 'B', 'C', 'D', 'E', 'F']

        if (color[1] != "#"):
            color = "#" + color


        if (len(color) != 7):
            return (False, "Needs 7 characters")

        for i in range(len(color)):
            if (color[i] not in hex_code_list):
                return (False, "Character in Hex Value is not valid")


        return color
    

    def set_primary(self):
        prim_color = self.entry1.get()
        prim_color = self.hex_code_check(prim_color)
        while prim_color is tuple:
            prim_color = self.ErrorDisplay(prim_color[1])
            prim_color = self.hex_color_check(prim_color)
        self.primary_color = prim_color
    

    def set_secondary(self, sec_color):
        sec_color = entry2.get()
        sec_color = hex_code_check(sec_color)
        while sec_color is tuple:
            sec_color = ErrorDisplay(sec_color[1])
            sec_color = hex_code_check(sec_color)
        self.secondary_color = sec_color
    


def main():
    settingsGui = SettingGui()
