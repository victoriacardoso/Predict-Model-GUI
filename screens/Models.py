from tkinter import *

class Models:
    def __init__(self):
        self.models_window = Tk()
        self.models_window.title("Models")
        self.models_window.geometry("500x250")
        self.models_window["pady"] = 10
        self.models_window.resizable(0,0)

        self.fonte_padrao = ("Arial", "10")
        self.models_container = Frame(self.models_window)
        self.models_container.pack()

        self.select_model_container = LabelFrame(self.models_container, text="Models", width=480, height=170)
        self.select_model_container["pady"] = 5
        self.select_model_container.grid_propagate(0)
        self.select_model_container.pack()

        self.model_label = Label(self.select_model_container, text="Select the models", font=self.fonte_padrao)
        self.model_label["pady"] = 5
        self.model_label.grid(columnspan=2, sticky='w')

        nb = IntVar()
        dtc = IntVar()
        ann_keras = IntVar()
        rf = IntVar()
        lr = IntVar()
        lda = IntVar()
        knn = IntVar()
        cart = IntVar()
        gaussian_nb = IntVar()
        svn = IntVar()

        nb_check = Checkbutton(self.select_model_container, text="Naive bayes", variable=nb, onvalue=1, offvalue=0)
        nb_check.grid(row=1, column=0, sticky='w')

        dtc_check = Checkbutton(self.select_model_container, text="DecisionTreeClassifier", variable=dtc, onvalue=1, offvalue=0)
        dtc_check.grid(row=1, column=1, sticky='w')

        ann_keras_check = Checkbutton(self.select_model_container, text="Artificial Neural Network with Keras", variable=ann_keras, onvalue=1, offvalue=0)
        ann_keras_check.grid(row=2, column=0, sticky='w')

        rf_check = Checkbutton( self.select_model_container, text="Random Forest", variable=rf, onvalue=1, offvalue=0)
        rf_check.grid(row=2, column=1, sticky='w')

        lr_check = Checkbutton( self.select_model_container, text="LogisticRegression-LR", variable=lr, onvalue=1, offvalue=0)
        lr_check.grid(row=3, column=0, sticky='w')

        lda_check = Checkbutton( self.select_model_container, text="LinearDiscriminantAnalysis-LDA", variable=lda, onvalue=1, offvalue=0)
        lda_check.grid(row=3, column=1, sticky='w')

        knn_check = Checkbutton( self.select_model_container, text="KNeighborsClassifier-KNN", variable=knn, onvalue=1, offvalue=0)
        knn_check.grid(row=4, column=0, sticky='w')

        cart_check = Checkbutton( self.select_model_container, text="DecisionTreeClassifier-CART", variable=cart, onvalue=1, offvalue=0)
        cart_check.grid(row=4, column=1, sticky='w')

        gaussian_nb_check = Checkbutton( self.select_model_container, text="GaussianNB-NB", variable=gaussian_nb, onvalue=1, offvalue=0)
        gaussian_nb_check.grid(row=5, column=0, sticky='w')

        svn_check = Checkbutton( self.select_model_container, text="SVC-SVN", variable=svn, onvalue=1, offvalue=0)
        svn_check.grid(row=5, column=1, sticky='w')

        self.newProject = Button(self.models_container)
        self.newProject["text"] = "Save"
        self.newProject["font"] = self.fonte_padrao
        self.newProject["width"] = 5
        # self.newProject["command"] = self.salvar_projeto
        self.newProject.pack(side=BOTTOM, pady=10)