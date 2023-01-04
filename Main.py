from tkinter import *
from screens.Home import Home
from models.LDA import LDA

root = Tk()

root.title("Predict model GUI")
root.resizable(0,0)
root.geometry("550x400")

Home(root)

metrics = "Accuracy\nPrecision\n"

LDA().predict(0.3, metrics)

root.mainloop()




