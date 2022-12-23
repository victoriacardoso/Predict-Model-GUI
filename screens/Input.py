from tkinter import *
from tkinter.filedialog import askopenfilename

class Input:
    def __init__(self,):
        self.input_window = Tk()
        self.input_window.geometry("500x130")
        self.input_window.title("Input CSV")
        self.input_window["pady"] = 5
        self.input_window.resizable(0,0)

        self.fonte_padrao = ("Arial", "10")
        self.input_container = Frame(self.input_window, width=480, height=80)
        self.input_container.pack_propagate(0)
        self.input_container.pack()

        self.input_label = Label(self.input_container, text="CSV", font=self.fonte_padrao)
        self.input_label["padx"] = 20
        self.input_label.pack(side=LEFT)

        self.path = Entry(self.input_container)
        self.path["width"] = 40
        self.path.pack(side=LEFT)

        self.choose = Button(self.input_container)
        self.choose["text"] = "Choose file"
        self.choose["font"] = self.fonte_padrao
        self.choose["width"] = 8
        self.choose["command"] = self.open_file
        self.choose.pack(side=RIGHT, padx=20)

        self.save = Button(self.input_window)
        self.save["text"] = "Save"
        self.save["font"] = self.fonte_padrao
        self.save["width"] = 5
        self.save["command"] = self.open_file
        self.save.pack(side=BOTTOM, pady=5)
    
    def open_file(self):
        Tk().withdraw()
        self.input_window.lift()
        file_name = askopenfilename(filetypes=[("CSV files", ".csv")])
        self.path.config(state='normal')
        self.path.insert(0, file_name)
        self.path.config(state='disabled')

    
    