import customtkinter as ctk
from .main_screen import app
from ..read_json import read
from ..weather_data import *
# we import app from main_screen where will be the following additions, we import function read from read_json to get information from certain fail from static folder, we need weather_date to get needed information about weather

# we need CTkFrame to get access to the certain functions of ctk
class Info(ctk.CTkFrame):
    # we created parameter to use it further
    def __init__(self, child_master: ctk.CTk):
        ctk.CTkFrame.__init__(
            # we created some other parameters and gave them values
            self,
            master = child_master,
            width = 925,
            height = 800,
            fg_color = "#5DA7B1"
        )
        # we used grid to arrange what we have created, it arrange using rows and columns
        self.grid(row = 0, column = 1)
        
        # we used CTkLabel to give value to some parameters and make text looks way we need
        self.current_position = ctk.CTkLabel(
            master = self,
            text = 'Praegune linn',
            font = ('Roboto Slab', 35, 'bold'),
            text_color = '#FFFFFF'
        )
        # we used place to arrange what we have created, it arrange using exact position of x and y axis
        self.current_position.place(x = 350, y = 100)
        city_name = read("config.json")["list_city"][0]
        get_info_weather(city_name, "weather_data.json", False)
        data = read("weather_data.json")
        self.NAME = ctk.CTkLabel(
            self, 
            text = data["name"], 
            text_color = "white",
            font = ('Roboto Slab', 25, 'bold'),
        )
        self.NAME.place(x = 440, y = 145)
        temp = round(data["main"]["temp"])
        self.TEMP = ctk.CTkLabel(
            self, 
            text = f"{temp}°", 
            text_color = "white",
            font = ('Roboto Slab', 70, 'bold'),
        )
        self.TEMP.place(x = 435, y = 180)
        description = data["weather"][0]["description"].capitalize()
        if description == "Clear sky":
            description = "Selge taev"
            
        elif description == "Few clouds":
            description = "Vähesed pilved"

        elif description == "Scattered clouds":
            description = "Hajutatud pilved"

        elif description == "Broken clouds":
            description = "Katkised pilved"

        elif description == "Shower rain":
            description = "Vihmahoog"

        elif description == "Overcast clouds":
            description = "Pilvised pilved"

        elif description == "Rain":
            description = "Vihm"

        elif description == "Thunderstorm":
            description = "Äikesetorm"
        
        elif description == "Snow":
            description = "Lumi"
        
        elif description == "Mist":
            description = "Udu"

        self.DESCRIPTION = ctk.CTkLabel(
            self, 
            text = description, 
            text_color = "white",
            font = ('Roboto Slab', 25, 'bold'),
        )
        self.DESCRIPTION.place(x = 410, y = 300)
        
# в чем суть 89 строки и где этот обьект используется потом, каким образом он выводится в окно приложения
info = Info(child_master = app)