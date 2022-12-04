from tkinter import *

class Models:
    def __init__(self, root):
        root["pady"] = 10
        self.fonte_padrao = ("Arial", "10")

        self.models_container = Frame(root)

        self.select_model_container = Frame(self.models_container, width=540, height=80)
        self.select_model_container["highlightbackground"] = "gray"
        self.select_model_container["highlightthickness"] = 0.5
        self.select_model_container.pack_propagate(0)
        self.select_model_container.pack()

        self.model_label = Label(self.select_model_container, text="Model", font=self.fonte_padrao)
        self.model_label["padx"] = 20
        self.model_label.pack(side=LEFT)

        option_list = ["Naive bayes", 
                        "Fann2", 
                        "DecisionTreeClassifier", 
                        "Artificial Neural Network with Keras",
                        "Random Forest"]
        value_inside = StringVar(root)
        value_inside.set("Select an Option")

        metrics_option_menu = OptionMenu(self.select_model_container, value_inside, *option_list)
        metrics_option_menu.pack(side=LEFT)

        self.newProject = Button(self.models_container)
        self.newProject["text"] = "Save"
        self.newProject["font"] = self.fonte_padrao
        self.newProject["width"] = 5
        # self.newProject["command"] = self.salvar_projeto
        self.newProject.pack(side=BOTTOM, pady=20)