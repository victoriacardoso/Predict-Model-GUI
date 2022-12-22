from tkinter import *

class Input:
    def __init__(self):
        self.input_window = Tk()
        self.input_window["pady"] = 10
        self.input_window.resizable(0,0)

        self.fonte_padrao = ("Arial", "10")
        self.input_container = Frame(self.input_window, width=540, height=80)
        self.input_container["highlightbackground"] = "gray"
        self.input_container["highlightthickness"] = 0.5
        self.input_container.pack_propagate(0)
        self.input_container.pack()

        self.input_label = Label(self.input_container, text="CSV file", font=self.fonte_padrao)
        self.input_label["padx"] = 20
        self.input_label.pack(side=LEFT)

        self.path = Entry(self.input_container, state=DISABLED)
        self.path["width"] = 40
        self.path.pack(side=LEFT)

        self.choose = Button(self.input_container)
        self.choose["text"] = "Choose file"
        self.choose["font"] = self.fonte_padrao
        self.choose["width"] = 8
        # self.choose["command"] = self.salvar_projeto
        self.choose.pack(side=RIGHT, padx=30)