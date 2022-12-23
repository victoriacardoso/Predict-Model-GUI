from tkinter import *
from screens.Project import Project
from screens.Input import Input
from screens.Parameters import Parameters
from screens.Models import Models
from screens.Graphics import Graphics
from screens.About import About

root = Tk()
root.title("Predict model GUI")
root.resizable(0,0)
root.geometry("550x400")

def open_project_interface():
    Project()

def open_input_interface():
    Input()

def open_parameters_interface():
    Parameters()

def open_models_interface():
    Models()

def open_graphics_interface():
    Graphics()

def open_about_interface():
    About()

menu_bar = Menu()
root.config(menu=menu_bar)

project_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Project", menu=project_menu)
project_menu.add_command(label="Save", command=open_project_interface)
project_menu.add_command(label="Load", command=open_project_interface)
project_menu.add_command(label="Exit", command=open_project_interface)

input_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Input", menu=input_menu)
input_menu.add_command(label="CSV", command=open_input_interface)

parameters_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Parameters", menu=parameters_menu)
parameters_menu.add_command(label="Add Parameters", command=open_parameters_interface)

models_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Models", menu=models_menu)
models_menu.add_command(label="Add Models", command=open_models_interface)

graphics_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Graphics", menu=graphics_menu)
graphics_menu.add_command(label="View graphics")

about_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="User Guide", command=open_models_interface)
about_menu.add_command(label="About us", command=open_about_interface)

root.mainloop()
