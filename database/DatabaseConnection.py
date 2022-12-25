from tkinter import *
import sqlite3

class DatabaseConnection:
    def connect(self):
        self.conn = sqlite3.connect("database/database.db")
        self.cursor = self.conn.cursor()
    
    def disconnect(self):
        self.conn.close()

    def create_project_table(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS project (
                id_project INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR NOT NULL,
                creation_date VARCHAR NOT NULL,
                status VARCHAR NOT NULL, 
                id_model INTEGER NOT NULL, 
                FOREIGN KEY(id_model) REFERENCES model(id_model)
            );
        """)
        self.conn.commit()

    def create_parameters_table(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS parameter (
                id_parameter INTEGER PRIMARY KEY AUTOINCREMENT, 
                test_size DOUBLE NOT NULL,
                metrics VARCHAR NOT NULL,
                id_project INTEGER NOT NULL,
                FOREIGN KEY(id_project) REFERENCES project(id_project)
            );
        """)
        self.conn.commit()

    def create_models_table(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS model (
                id_model INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR NOT NULL,
                content BLOB NOT NULL
            );
        """)
        self.conn.commit()
    
    def start(self):
        self.connect()
        self.create_project_table()
        self.create_parameters_table()
        self.create_models_table()
        self.disconnect()