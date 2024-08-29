
import sqlite3

class SQLiteDB:
    
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def init_app(self, db_name):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        
    def query(self, query_str):
        return self.cursor.execute(query_str)
    