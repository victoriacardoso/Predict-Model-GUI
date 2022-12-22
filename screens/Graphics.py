from tkinter import *

class Graphics:
    def __init__(self,):
        self.graphics_window = Tk()
        self.graphics_window["pady"] = 10
        self.graphics_window.resizable(0,0)

        self.fonte_padrao = ("Arial", "10")
        self.parameters_container = Frame(self.graphics_window)
        self.parameters_container.pack()

        self.test_size_container = Frame(self.parameters_container, width=540, height=80)
        self.test_size_container["highlightbackground"] = "gray"
        self.test_size_container["highlightthickness"] = 0.5
        self.test_size_container.pack_propagate(0)
        self.test_size_container.pack()

        self.test_size_label = Label(self.test_size_container, text="Test size", font=self.fonte_padrao)
        self.test_size_label["padx"] = 20
        self.test_size_label.pack(side=LEFT)

        current_value = StringVar(value=0.2)
        self.test_size_spin_box = Spinbox(self.test_size_container, format="%.1f", increment=0.1, from_=0.1, to=0.9, textvariable=current_value, wrap=True)
        self.test_size_spin_box.pack(side=LEFT)

        self.metrics_container = Frame(self.parameters_container, width=540, height=80)
        self.metrics_container["highlightbackground"] = "gray"
        self.metrics_container["highlightthickness"] = 0.5
        self.metrics_container.pack_propagate(0)
        self.metrics_container.pack(pady=15)

        self.metrics_label = Label(self.metrics_container, text="Metrics", font=self.fonte_padrao)
        self.metrics_label["padx"] = 20
        self.metrics_label.pack(side=LEFT)

        option_list = ["Accuracy", "Precision", "Recall", "F1-score"]
        value_inside = StringVar( self.graphics_window)
        value_inside.set("Select an Option")

        metrics_option_menu = OptionMenu(self.metrics_container, value_inside, *option_list)
        metrics_option_menu.pack(side=LEFT)

        self.newProject = Button(self.parameters_container)
        self.newProject["text"] = "Save"
        self.newProject["font"] = self.fonte_padrao
        self.newProject["width"] = 5
        # self.newProject["command"] = self.salvar_projeto
        self.newProject.pack(side=BOTTOM, pady=20)