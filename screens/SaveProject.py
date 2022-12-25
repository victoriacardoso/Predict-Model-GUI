from tkinter import *

class SaveProject:
    def __init__(self):
        self.project_window = Tk()
        self.project_window.geometry("500x100")
        self.project_window.title("Save Project")
        self.project_window["pady"] = 10
        self.project_window["padx"] = 10
        self.project_window.resizable(0,0)

        self.fonte_padrao = ("Arial", "10")
        self.project_container = Frame(self.project_window, width=480, height=80)
        self.project_container.pack_propagate(0)
        self.project_container.pack()

        self.projeto_label = Label(self.project_container, text="Project Name", font=self.fonte_padrao)
        self.projeto_label["padx"] = 20
        self.projeto_label.pack(side=LEFT)

        self.project = Entry(self.project_container)
        self.project["width"] = 30
        self.project["font"] = self.fonte_padrao
        self.project.pack(side=LEFT)

        self.newProject = Button(self.project_container)
        self.newProject["text"] = "Save"
        self.newProject["font"] = self.fonte_padrao
        self.newProject["width"] = 5
        self.newProject["command"] = self.save_project
        self.newProject.pack(side=RIGHT, padx=25)


    def save_project(self):
        self.msg["text"] = "Save"
    


