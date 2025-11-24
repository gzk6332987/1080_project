import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        """
        Connect to a sqlite database

        Args:
            db_path (str): the sqlite database path
        """
        self.connection = sqlite3.connect(db_path)
        
    def length(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        return count
    
    def get_id_list(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT id FROM {table_name}")
        id_list = [row[0] for row in cursor.fetchall()]
        return id_list
    
    def query_by_id(self, table_name, record_id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name} WHERE id=?", (record_id,))
        record = cursor.fetchone()
        return record
    
    def insert_record(self, table_name, columns: [str, ...], values: [str, ...]):
        cursor = self.connection.cursor()
        placeholders = ', '.join('?' * len(values))
        columns_formatted = ', '.join(columns)
        cursor.execute(f"INSERT INTO {table_name} ({columns_formatted}) VALUES ({placeholders})", values)
        self.connection.commit()
    
    def __del__(self):
        self.connection.close()
        
