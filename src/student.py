from sqlite3 import Connection
from database import DatabaseManager


class StudentBuilder:
    def __init__(self):
        self.name = "no name"
        self.age = 0

    def set_name(self, name):
        self.name = name
        return self

    def set_age(self, age):
        self.age = age
        return self

    def build(self):
        return Student(self.name, self.age)
    
    # Or load from database
    def from_db_record(self, connection: DatabaseManager, student_id: int):
        info = connection.query_by_id(student_id)
        # TODO debug to get correct fields
        
        # TODO # return Student()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    