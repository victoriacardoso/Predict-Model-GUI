from tkinter import *
from tkinter import ttk
from database.DatabaseConnection import DatabaseConnection

class LoadProject:
    def __init__(self):
        self.load_project_window = Toplevel()
        self.load_project_window.geometry("450x200")
        self.load_project_window.title("Load Project")
        self.load_project_window["pady"] = 10
        self.load_project_window["padx"] = 10
        self.load_project_window.resizable(0,0)

        self.fonte_padrao = ("Arial", "10")
        self.load_project_container = Frame(self.load_project_window, width=400, height=120)
        self.load_project_container.pack_propagate(0)
        self.load_project_container.pack(pady=20)
    
        self.load_button_container = Frame(self.load_project_window)
        self.load_button_container.pack(side=BOTTOM)

        self.open_table()
        
        self.load_project = Button(self.load_button_container)
        self.load_project["text"] = "Load"
        self.load_project["font"] = self.fonte_padrao
        self.load_project["width"] = 5
        # self.load_project["command"] = self.save_project
        self.load_project.pack(side=LEFT, padx=5)

        self.remove_project = Button(self.load_button_container)
        self.remove_project["text"] = "Remove"
        self.remove_project["font"] = self.fonte_padrao
        self.remove_project["width"] = 5
        # self.remove_project["command"] = self.save_project
        self.remove_project.pack(side=LEFT)

        self.update = Button(self.load_button_container)
        self.update["text"] = "Update parameters"
        self.update["font"] = self.fonte_padrao
        self.update["width"] = 15
        # self.update["command"] = self.save_project
        self.update.pack(side=LEFT, padx=5)

    def open_table(self):
        style = ttk.Style()
        #Pick a theme
        style.theme_use("default")
        # Configure our treeview colors

        style.configure("Treeview", 
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3"
            )
        # Change selected color
        style.map('Treeview', 
            background=[('selected', 'blue')])

        # Treeview Scrollbar
        tree_scroll = Scrollbar(self.load_project_container)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create Treeview
        my_tree = ttk.Treeview(self.load_project_container, yscrollcommand=tree_scroll.set, selectmode="extended")
        # Pack to the screen
        my_tree.pack()

        #Configure the scrollbar
        tree_scroll.config(command=my_tree.yview)

        my_tree["columns"] = ("id", "Name", "Date", "Status")
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("id", anchor=CENTER, width=10)
        my_tree.column("Name", anchor=CENTER, width=100)
        my_tree.column("Date", anchor=CENTER, width=150)
        my_tree.column("Status", anchor=CENTER, width=130)
        
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("id", text="id", anchor=CENTER)
        my_tree.heading("Name", text="Name", anchor=CENTER)
        my_tree.heading("Date", text="Date", anchor=CENTER)
        my_tree.heading("Status", text="Status", anchor=CENTER)

        data = DatabaseConnection().get_project()
        # DatabaseConnection().disconnect()
        for record in data:
	        my_tree.insert(parent='', index='end', text="", values=(record[0], record[1], record[2], record[3]))

        

        


    
