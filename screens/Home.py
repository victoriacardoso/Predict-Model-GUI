from tkinter import *
from tkinter import messagebox
from screens.SaveProject import SaveProject
from screens.Input import Input
from screens.Parameters import Parameters
from screens.Models import Models
from screens.Graphics import Graphics
from screens.About import About
from screens.LoadProject import LoadProject
from database.DatabaseConnection import DatabaseConnection

class Home:
    def __init__(self, root):
        self.menu_bar = Menu()
        self.project_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Project", menu=self.project_menu)
        self.project_menu.add_command(label="Save", command=self.open_save_project_interface)
        self.project_menu.add_command(label="Load", command=self.open_load_project_interface)
        self.project_menu.add_command(label="Exit", command=root.quit)

        self.input_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Input", menu=self.input_menu)
        self.input_menu.add_command(label="CSV", command=self.verify_project)

        self.parameters_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Parameters", menu=self.parameters_menu)
        self.parameters_menu.add_command(label="Add Parameters", command=self.verify_parameter)

        self.models_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Models", menu=self.models_menu)
        self.models_menu.add_command(label="Add Models", command=self.verify_model)

        self.graphics_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Graphics", menu=self.graphics_menu)
        self.graphics_menu.add_command(label="View graphics")

        self.about_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)
        self.about_menu.add_command(label="User Guide")
        self.about_menu.add_command(label="About us", command=self.open_about_interface)
        root.config(menu=self.menu_bar)


    def open_save_project_interface(self):
        SaveProject()

    def open_load_project_interface(self):
        LoadProject()

    def open_input_interface(self):
        Input()

    def open_parameters_interface(self):
        
        Parameters()

    def open_models_interface(self):
        Models()

    def open_graphics_interface(self):
        Graphics()

    def open_about_interface(self):
        About()

    def verify_parameter(self): 
        if DatabaseConnection().verify_parameter() == True:
            messagebox.showinfo("Information","Please, create a project and add a input first!")

        else:
            self.open_parameters_interface()


    def verify_project(self):
        if DatabaseConnection().verify_project():
            self.open_input_interface()

        else:
            messagebox.showinfo("Information","Please, create a project first!")

    def verify_model(self):
        if DatabaseConnection().verify_parameter() == True:
            messagebox.showinfo("Information","Please, create a project and add a input first!")

        else:
            self.open_parameters_interface()


DatabaseConnection().start()



