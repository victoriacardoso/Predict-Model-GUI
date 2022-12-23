from tkinter import *

class About:
    def __init__(self,):
        self.about_window = Toplevel()
        # self.about_window.geometry("550x300")
        self.about_window.title("About")
        self.about_window.resizable(0,0)

        self.fonte_titulo = ("Century Schoolbook L", "14", "bold")
        self.fonte_subtitulo = ("Century Schoolbook L", "10")
        self.about_container = Frame(self.about_window)
        self.about_container["pady"] = 5
        # self.about_container.pack_propagate(0)
        self.about_container.pack()

        self.image_group = PhotoImage(file='image/biod.png')

        self.label_image = Label(self.about_container, image=self.image_group)
        self.label_image.image = self.image_group

        self.label_image.pack(side=LEFT, padx=10)

        self.software_name = Label(self.about_container, text="PREDICT MODEL GUI", font=self.fonte_titulo)
        self.software_name.pack(side=TOP, padx=20)

        self.about_software = Label(self.about_container, text="This software is part of scientific research\n developed by the BIOD group. \n www.biod.ufpa.br", font=self.fonte_subtitulo)
        self.about_software.pack(side=RIGHT, padx=20)


       