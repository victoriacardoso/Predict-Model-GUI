from tkinter import *
from tkinter import ttk

class Parameters:
    def __init__(self,):
        self.parameters_window = Tk()
        self.parameters_window.geometry("500x280")
        self.parameters_window.title("Add Parameters")
        self.parameters_window["pady"] = 10
        self.parameters_window["padx"] = 10
        self.parameters_window.resizable(0,0)

        self.fonte_padrao = ("Arial", "10")
        self.parameters_container = Frame(self.parameters_window)
        self.parameters_container.pack()

        self.test_size_container = LabelFrame(self.parameters_container, text="Dataset Parameters", width=480, height=80)
        self.test_size_container.pack_propagate(0)
        self.test_size_container.pack()

        self.test_size_label = Label(self.test_size_container, text="Test size", font=self.fonte_padrao)
        self.test_size_label["padx"] = 20
        self.test_size_label.pack(side=LEFT)

        # current_value = StringVar(value='0.2')
        self.test_size_spin_box = Spinbox(self.test_size_container, format="%.1f", increment=0.1, from_=0.1, to=0.9, wrap=True)
        self.test_size_spin_box.pack(side=LEFT)

        self.metrics_container = LabelFrame(self.parameters_container, text= "Metrics", width=480, height=80)
        self.metrics_container.pack_propagate(0)
        self.metrics_container.pack(pady=15)

        accuracy = IntVar()
        precision = IntVar()
        recall = IntVar()
        f1_score = IntVar()

        accuracy_check = Checkbutton(self.metrics_container, text="Accuracy", variable=accuracy, onvalue=1, offvalue=0)
        accuracy_check.pack(side=LEFT, padx=10)

        precision_check = Checkbutton(self.metrics_container, text="Precision", variable=precision, onvalue=1, offvalue=0)
        precision_check.pack(side=LEFT, padx=10)

        recall_check = Checkbutton(self.metrics_container, text="Recall", variable=recall, onvalue=1, offvalue=0)
        recall_check.pack(side=LEFT, padx=10)

        f1_score_check = Checkbutton(self.metrics_container, text="F1-Score", variable=f1_score, onvalue=1, offvalue=0)
        f1_score_check.pack(side=LEFT, padx=10)

        

        self.newProject = Button(self.parameters_container)
        self.newProject["text"] = "Save"
        self.newProject["font"] = self.fonte_padrao
        self.newProject["width"] = 5
        # self.newProject["command"] = self.salvar_projeto
        self.newProject.pack(side=BOTTOM, pady=20)