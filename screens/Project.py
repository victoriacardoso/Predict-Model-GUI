from tkinter import *

class Project:
    def __init__(self, root):
        root["pady"] = 10
        self.fonte_padrao = ("Arial", "10")
        self.project_container = Frame(root, width=540, height=80)
        self.project_container["highlightbackground"] = "gray"
        self.project_container["highlightthickness"] = 0.5
        self.project_container.pack_propagate(0)

        self.projeto_label = Label(self.project_container, text="Project Name", font=self.fonte_padrao)
        self.projeto_label["padx"] = 20
        self.projeto_label.pack(side=LEFT)

        self.project = Entry(self.project_container)
        self.project["width"] = 40
        self.project["font"] = self.fonte_padrao
        self.project.pack(side=LEFT)

        self.newProject = Button(self.project_container)
        self.newProject["text"] = "Save"
        self.newProject["font"] = self.fonte_padrao
        self.newProject["width"] = 5
        self.newProject["command"] = self.salvar_projeto
        self.newProject.pack(side=RIGHT, padx=25)

        # self.msg = Label(self.quarto_container, text="", font=self.fonte_padrao)
        # self.msg.pack()

    def salvar_projeto(self):
        self.msg["text"] = "Salvo com sucesso"

