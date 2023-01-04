import sqlite3
from datetime import datetime


class DatabaseConnection:
    conn = sqlite3.connect("database/database.db")
    cursor = conn.cursor()
    id_project = ""
        
    def disconnect(self):
        self.conn.close()

    def create_project_table(self):
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS project (
                id_project INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR NOT NULL,
                creation_date VARCHAR NOT NULL,
                status VARCHAR NOT NULL, 
                input VARCHAR NOT NULL,
                id_models VARCHAR NOT NULL
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

    def insert_project(self, project_name):
        last_id = self.cursor.lastrowid
        now = datetime.now()
        date = now.strftime("%m/%d/%Y %H:%M:%S")

        project_sql = """ INSERT INTO project (name, creation_date, status, input, id_models) values (?, ?, ?, ?,?)"""
        data_tuple = (project_name, date, "", "", "")

        self.cursor.execute(project_sql, data_tuple)
        self.conn.commit()
    
    def insert_input(self, input):
        last_id = self.cursor.lastrowid
    
        project_sql = """UPDATE project set input=? WHERE id_project=?"""
        data_tuple = (input, last_id)

        self.cursor.execute(project_sql, data_tuple)
        self.conn.commit()

    def insert_parameter(self, test_size, metrics):
        last_id = self.cursor.lastrowid
        parameter_sql = """ INSERT INTO parameter (test_size, metrics, id_project) values (?, ?, ?)"""
        data_tuple = (test_size, metrics, last_id)
        self.cursor.execute(parameter_sql, data_tuple)
        self.conn.commit()

    def insert_id_models(self, id_models):
        last_id = self.cursor.lastrowid
        
        project_sql = """UPDATE project set id_models=? WHERE id_project=?"""
        data_tuple = (input, last_id)

        self.cursor.execute(project_sql, data_tuple)
        self.conn.commit()
    
    def verify_project(self):
        last_id = self.cursor.lastrowid
        project = self.get_project_by_id(last_id)

        if len(project) == 0 :
            return False
        else:
            row_project = project[0]
            if row_project[4] == "":
                return True
            else:
                return True

    def verify_parameter(self):
        last_id = self.cursor.lastrowid
        parameter = self.get_parameter_by_id(last_id)
        project = self.get_project_by_id(last_id)

        if len(parameter) == 0 and len(project) !=0:
            record = project[0]
            input = record[4]
            if input != "":
                return False
            else:
                return True
        else:
            return True

    def convertToBinaryData(self, filename):
    # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData
    
    def insert_model(self, name, content):
        model_sql = """ INSERT INTO model (name, content) values (?, ?)"""
        model_content = self.convertToBinaryData(content)
        data_tuple = (name, model_content)

        self.cursor.execute(model_sql, data_tuple)
        self.conn.commit()
    
    def writeTofile(self, data, filename):
    # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)
    
    def get_model(self, id_model):
        retrieve_model = """ SELECT * from model WHERE id_model = ?"""
        self.cursor.execute(retrieve_model, (id_model,))

        record = self.cursor.fetchall()

        for row in record:
            name = row[1]
            content = row[2]
            model_file = "models/" + name + ".py"
            self.writeTofile(content, model_file)
        
    def get_projects(self):
        retrieve_project = """ SELECT * from project"""
        self.cursor.execute(retrieve_project)

        record = self.cursor.fetchall()
        return record

    def get_project_by_id(self, id_project):
        retrieve_project = """ SELECT * from project where id_project=?"""
        self.cursor.execute(retrieve_project, (id_project,))
        project = self.cursor.fetchall()
        return project

    def get_parameter_by_id(self, id):
        retrieve_parameter = """ SELECT * from parameter where id_project=?"""
        self.cursor.execute(retrieve_parameter, (id,))
        parameter = self.cursor.fetchall()
        return parameter

    def start(self):
        self.create_project_table()
        self.create_parameters_table()
        self.create_models_table()
        # self.insert_model("LDA-LR-CART-KNN-NB-SVM", "models/classificationlr_lda_knn_cart_nb_svm.py")
        #self.get_model(1) 
        # self.disconnect()