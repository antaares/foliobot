
import sqlite3

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)
        

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id int primary key NOT NULL,
            Name varchar(255) NOT NULL
            );
"""
        self.execute(sql, commit=True)
    
    def create_table_robots(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Robots (
            id int primary key NOT NULL,
            name varchar(200),
            url varchar(255)
            );"""
        self.execute(sql, commit=True)
    def create_table_web(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Web (
            id int primary key NOT NULL,
            name varchar(200),
            url varchar(255)
            );"""
        self.execute(sql, commit=True)
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


    def add_user(self, id: int, name: str):
        sql = """
        INSERT or IGNORE INTO Users(id, Name) VALUES(?, ?)
        """
        self.execute(sql, parameters=(id, name,), commit=True)
    def count(self):
        sql = """SELECT COUNT(*) FROM Users"""
        count = self.execute(sql=sql, fetchone=True)
        return count[0]
    

    def add_robot(self, name: str, url: str):
        sql = """
        INSERT or IGNORE INTO Robots(id, name, url) VALUES(?,?,?)
        """
        id = self.count_robot()
        self.execute(sql=sql, parameters=(id, name, url,), commit=True)
    
    def get_robots(self):
        sql = """
        SELECT * FROM Robots
        """
        robots = self.execute(sql=sql, fetchall=True)
        return robots
    
    def count_robot(self):
        sql = """
        SELECT COUNT(*) FROM Robots"""
        count = self.execute(sql=sql, fetchone=True)
        return count[0]
    
    def add_web(self, name: str, url: str):
        sql = """
        INSERT or IGNORE INTO Web(id, name, url) VALUES(?,?,?)
        """
        id = self.count_web()
        self.execute(sql=sql, parameters=(id, name, url,), commit=True)
    
    def get_webs(self):
        sql = """
        SELECT * FROM Web
        """
        webs = self.execute(sql=sql, fetchall=True)
        return webs
    
    def count_web(self):
        sql = """
        SELECT COUNT(*) FROM Web"""
        count = self.execute(sql=sql, fetchone=True)
        return count[0]
    
    def delete_robot(self, id):
        sql = """DELETE FROM Robots WHERE id=?"""
        self.execute(sql, parameters=(id,), commit=True)

    def delete_web(self, id):
        sql = """DELETE FROM Web WHERE id=?"""
        self.execute(sql, parameters=(id,), commit=True)
    
