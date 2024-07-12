import json
import tkinter as tk
import customtkinter

"""git comment change"""

def change_primary(primary_hex):
    primary = [primary_hex, primary_hex]

    with open('settings.json', 'r') as fin:
        settings = json.load(fin)

    settings["CTk"]["fg_color"] = primary 
    settings["CTkToplevel"]["fg_color"] = primary
    settings["CTkFrame"]["fg_color"] = primary
    settings["CTkFrame"]["border_color"] = primary
    settings["CTkButton"]["border_color"] = primary
    settings["CTkEntry"]["border_color"] = primary
    settings["CTkCheckBox"]["border_color"] = primary
    settings["CTkSwitch"]["progress_color"] = primary
    settings["CTkRadioButton"]["border_color"] = primary
    settings["CTkProgressBar"]["progress_color"] = primary
    settings["CTkProgressBar"]["border_color"] = primary
    settings["CTkOptionMenu"]["border_color"] = primary
    settings["CTkComboBox"]["border_color"] = primary
    settings["CTkTextbox"]["border_color"] = primary
    settings["CTkTextbox"]["text_color"] = primary
    
    with open('settings.json', 'w') as fout:
        json.dump(settings, fout, indent=4)
 
    #tk.messagebox.showinfo("showinfo", "Primary color changed. \nRestart app to see changes")
 
def change_secondary(secondary_hex):
    secondary = [secondary_hex, secondary_hex]
    
    with open('settings.json', 'r') as fin:
        settings = json.load(fin)

    settings["CTkFrame"]["top_fg_color"] = secondary
    settings["CTkEntry"]["fg_color"] = secondary
    settings["CTkButton"]["fg_color"] = secondary
    settings["CTkCheckBox"]["fg_color"] = secondary
    settings["CTkCheckBox"]["hover_color"] = secondary
    settings["CTkSwitch"]["fg_color"] = secondary
    settings["CTkRadioButton"]["fg_color"] = secondary
    settings["CTkProgressBar"]["fg_color"] = secondary
    settings["CTkSlider"]["fg_color"] = secondary
    settings["CTkOptionMenu"]["fg_color"] = secondary
    settings["CTkOptionMenu"]["button_color"] = secondary
    settings["CTkComboBox"]["fg_color"] = secondary
    settings["CTkComboBox"]["button_color"] = secondary
    settings["CTkSegmentedButton"]["fg_color"] = secondary
    settings["CTkSegmentedButton"]["selected_color"] = secondary
    settings["CTkTextbox"]["fg_color"] = secondary
    settings["CTkScrollableFrame"]["label_fg_color"] = secondary
    settings["DropdownMenu"]["fg_color"] = secondary
    settings["DropdownMenu"]["hover_color"] = secondary

    with open('settings.json', 'w') as fout:
            json.dump(settings, fout, indent=4)
    customtkinter.set_default_color_theme("settings.json")   

    #tk.messagebox.showinfo("showinfo", "Secondary color changed. \nRestart app to see changes")

def reset_colors():
    primary = ["#275D38", "#275D38"]
    secondary = ["#FFFFFF", "#FFFFFF"]

    with open('settings.json', 'r') as fin:
        settings = json.load(fin)

    settings["CTk"]["fg_color"] = primary
    settings["CTkToplevel"]["fg_color"] = primary
    settings["CTkFrame"]["fg_color"] = primary
    settings["CTkFrame"]["border_color"] = primary
    settings["CTkButton"]["border_color"] = primary
    settings["CTkEntry"]["border_color"] = primary
    settings["CTkCheckBox"]["border_color"] = primary
    settings["CTkSwitch"]["progress_color"] = primary
    settings["CTkRadioButton"]["border_color"] = primary
    settings["CTkProgressBar"]["progress_color"] = primary
    settings["CTkProgressBar"]["border_color"] = primary
    settings["CTkOptionMenu"]["border_color"] = primary
    settings["CTkComboBox"]["border_color"] = primary
    settings["CTkTextbox"]["border_color"] = primary
    settings["CTkTextbox"]["text_color"] = primary
    
    settings["CTkFrame"]["top_fg_color"] = secondary
    settings["CTkEntry"]["fg_color"] = secondary
    settings["CTkButton"]["fg_color"] = secondary
    settings["CTkCheckBox"]["fg_color"] = secondary
    settings["CTkCheckBox"]["hover_color"] = secondary
    settings["CTkSwitch"]["fg_color"] = secondary
    settings["CTkRadioButton"]["fg_color"] = secondary
    settings["CTkProgressBar"]["fg_color"] = secondary
    settings["CTkSlider"]["fg_color"] = secondary
    settings["CTkOptionMenu"]["fg_color"] = secondary
    settings["CTkOptionMenu"]["button_color"] = secondary
    settings["CTkComboBox"]["fg_color"] = secondary
    settings["CTkComboBox"]["button_color"] = secondary
    settings["CTkSegmentedButton"]["fg_color"] = secondary
    settings["CTkSegmentedButton"]["selected_color"] = secondary
    settings["CTkTextbox"]["fg_color"] = secondary
    settings["CTkScrollableFrame"]["label_fg_color"] = secondary
    settings["DropdownMenu"]["fg_color"] = secondary
    settings["DropdownMenu"]["hover_color"] = secondary

    with open('settings.json', 'w') as fout:
        json.dump(settings, fout, indent=4)

    #tk.messagebox.showinfo("showinfo", "Colorscheme reset. \nRestart app to see changes")
