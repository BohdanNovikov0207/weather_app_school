import customtkinter as ctk
from .main_screen import app

# master - параметр, который отвечает за отцовский элемент (тот, к чему крепится)
# CTkScrollableFrame - создает элемент с прокруткой
class VerticalMenu(ctk.CTkScrollableFrame):
    def __init__ (self, master_ch: ctk.CTk, width_ch: int, height_ch: int, **kwargs):
        ctk.CTkScrollableFrame.__init__(
            self = self,
            master = master_ch,
            width = width_ch,
            height = height_ch,
            fg_color = "#096C82",
            **kwargs
        )
        self.grid(row=0, column=0)

menu = VerticalMenu(app, 275, 800)

# **kwargs - позволяет принимать любые параметры, даже с именем. Например: "test_func(firstnumber: 14, secondnumber: 88)"
# *args - позволяет принимать любые параметры без имени, например: "test_func(14, 88)"