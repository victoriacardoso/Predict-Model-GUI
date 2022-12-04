from tkinter import *
from screens.Project import Project
from screens.Input import Input
from screens.Parameters import Parameters
from screens.Models import Models

root = Tk()
root.title("Predict model GUI")
root.resizable(0,0)
root.geometry("550x400")

project =  Project(root)
project.project_container.pack()
input = Input(root)
parameters = Parameters(root)
models = Models(root)

def open_project_interface():
    if input.input_container.winfo_exists:
        input.input_container.pack_forget()
    if parameters.parameters_container.winfo_exists:
        parameters.parameters_container.pack_forget()
    if models.models_container.winfo_exists:
        models.models_container.pack_forget()
    project.project_container.pack()

def open_input_interface():
    if project.project_container.winfo_exists:
        project.project_container.pack_forget()
    if models.models_container.winfo_exists:
        models.models_container.pack_forget()
    if parameters.parameters_container.winfo_exists:
        parameters.parameters_container.pack_forget()
    input.input_container.pack()

def open_parameters_interface():
    if project.project_container.winfo_exists:
        project.project_container.pack_forget()
    if input.input_container.winfo_exists:
        input.input_container.pack_forget()
    if models.models_container.winfo_exists:
        models.models_container.pack_forget()
    parameters.parameters_container.pack()

def open_models_interface():
    if project.project_container.winfo_exists:
        project.project_container.pack_forget()
    if input.input_container.winfo_exists:
        input.input_container.pack_forget()
    if parameters.parameters_container.winfo_exists:
        parameters.parameters_container.pack_forget()
    models.models_container.pack()

menu_bar = Menu()
menu_bar.add_command(label="Project", command=open_project_interface)
menu_bar.add_command(label="Input", command=open_input_interface)
menu_bar.add_command(label="Models", command= open_models_interface)
menu_bar.add_command(label="Parameters", command=open_parameters_interface)
menu_bar.add_command(label="Grafics")
menu_bar.add_command(label="About")

root.config(menu=menu_bar)
root.mainloop()
