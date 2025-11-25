from sqlite3 import Connection
from typing import Tuple
from database import DatabaseManager
from problem_generator import ProblemGenerator
from database import DatabaseManager


class StudentBuilder:
    def __init__(self):
        self.name = "no name"
        self.id = 0

    def set_name(self, name):
        self.name = name
        return self
    
    def set_id(self, id):
        self.id = id
        return self

    def build(self, students_database: DatabaseManager):
        return Student(students_database, self.id, self.name)
    
    # Or load from database
    def from_db_record(self, database: DatabaseManager, student_id: int):
        info = database.query_by_id(student_id)
        # TODO debug to get correct fields
        
        # TODO # return Student()


class Student:
    def __init__(self, question_db: DatabaseManager, id: int, username: str):
        self.id = id
        self.username = username
        # Init this student question database if not
        # - check exist
        # - insert record
        if not question_db.check_table_exist(str(id)):
            question_db.run_custom_command(f"""
                CREATE TABLE "{id}" (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    mistake_count INTEGER DEFAULT 0
                );
            """.strip())
                    

    def get_info(self):
        return f"Name: {self.username}, Age: {self.age}"
    
    def generate_quiz_from_level(self, level: int, type: str) -> Tuple[str, int | float | str]:
        """
        generate a random question from specific level

        Args:
            level (int): from 1 to 10, out of range will raise `ValueError`
            type (str): "basic", "fraction", "polynomial", "algebra", "calculus"
            
        Return:
            Tuple[str, int | float | str]: first is question, second is answer
        """ 
        generator = ProblemGenerator()
        return generator.generate_problem(level, type)
    
    def generate_quiz_from_db(self, question_db: DatabaseManager) -> Tuple[str, int | float | str]:
        history_questions = question_db.query_all()
        history_questions.sort()
        
    def insert_question_to_db(self, database: DatabaseManager, question: str, answer: int | float| str):
        database.insert_record(str(self.id), ["question", "answer", "mistake_count"])

    
    