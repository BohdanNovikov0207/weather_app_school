# import customtkinter as an UI library is needed for better GUI, also we import function from read_json
import customtkinter as ctk
from ..read_json import *
# using this we get access to information from confing.json
config = read('config.json')
# we create to get imported customtkinter funcionallity
class App(ctk.CTk):
# we use __init__ to create parameters we need
    def __init__(self, name: str, width: int, height: int):
# we use this to apply color from config to self
        ctk.CTk.__init__(
            self = self,
            fg_color = config['color']
        )
# we use name parameter and apply it to name of the window
        self.title(string = name)
# we get size of screem
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
# colculating size for app window
        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)
# creating window according to previous colcuculations
        self.geometry(f'{width}x{height}+{x}+{y}')
# sets information, we took from config.json, to name, width and height
app = App(name = config['name'], width = config['width'], height = config['height'])

