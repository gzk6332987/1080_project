from sqlite3 import Connection
from typing import Tuple
from database import DatabaseManager
from problem_generator import ProblemGenerator
from database import DatabaseManager
from initialize import InitializeInfo
import random

class StudentBuilder:
    def __init__(self):
        self.name = "no name"
        self.id = 0
        self.score = InitializeInfo.default_score

    def set_name(self, name):
        self.name = name
        return self
    
    def set_id(self, id):
        self.id = id
        return self
    
    def set_score(self, score: int):
        self.score = score
    
    def set_score_from_db(self, student_db: DatabaseManager):
        score = student_db.execute_custom_command(
            """
            select score from students where id = ?
            """.strip(),
            (self.id,)
        ).fetchone()[0]
        self.score = score
        return self

    def build(self, students_database: DatabaseManager):
        return Student(students_database, self.id, self.name, self.score)
    
    # Or load from database
    def from_db_record(self, database: DatabaseManager, student_id: int):
        info = database.query_by_id(student_id)
        # TODO debug to get correct fields
        
        # TODO # return Student()


class Student:
    def __init__(self, question_db: DatabaseManager, id: int, username: str, score: int):
        self.id = id
        self.username = username
        self.score = score
        
        if score > InitializeInfo.max_score:
            raise ValueError("Please make sure score under max limitation writed in config.toml")
        self._level = self.score // InitializeInfo.level_gap
        
        # Init this student question database if not
        # - check exist
        # - insert record
        if not question_db.check_table_exist(str(id)):
            question_db.execute_custom_command(f"""
                CREATE TABLE "{id}" (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    mistake_count INTEGER DEFAULT 0
                );
            """.strip())
                    

    def get_info(self):
        return f"Name: {self.username}, Age: {self.age}"
    
    def get_level(self) -> int:
        return self._level
    
    def generate_quiz_from_level(self) -> Tuple[int, str, int | float | str]:
        """
        generate a random question from specific level

        Args:
            level (int): from 1 to 10, out of range will raise `ValueError`
            type (str): "basic", "fraction", "polynomial", "algebra", "calculus"
            
        Return:
            Tuple[int, str, int | float | str]: first is question index , second is question, third is answer
        """ 
        random_number = random.random()
        generator = ProblemGenerator()
        
        if self._level <= 3:
            generator.generate_problem(self._level, "basic")
        elif self._level <= 5:
            if random_number < 0.5:
                generator.generate_problem(self._level, "basic")
            else:
                generator.generate_problem(self._level, "fraction")
        elif self._level <= 7:
            if random_number < 0.33:
                generator.generate_problem(self._level, "fraction")
            elif random_number < 0.66:
                generator.generate_problem(self._level, "polynomial")
            else:
                generator.generate_problem(self._level, "algebra")
        elif self._level <= 9:
            if random_number < 0.20:
                generator.generate_problem(self._level, "fraction")
            elif random_number < 0.50:
                generator.generate_problem(self._level, "polynomial")
            elif random_number < 0.75:
                generator.generate_problem(self._level, "algebra")
            else:
                generator.generate_problem(self._level, "calculus")
        else:
            if random_number < 0.33:
                generator.generate_problem(self._level, "polynomial")
            elif random_number < 0.66:
                generator.generate_problem(self._level, "algebra")
            else:
                generator.generate_problem(self._level, "calculus")
            
        return generator.generate_problem(self._level, type)
    
    def generate_quiz_from_db(self, question_db: DatabaseManager) -> Tuple[str, int | float | str]:
        history_questions = question_db.query_all(str(self.id))
        # sorted_history_questions = sorted(history_questions, key=lambda x: x[-1])
        probability_weights = [question[-1] for question in history_questions]
        result = random.choices(history_questions, probability_weights)[0]
        return (result[0], result[1], result[2])
        
    def insert_question_to_db(self, database: DatabaseManager, question: str, answer: int | float| str):
        database.insert_record(str(self.id), ["question", "answer", "mistake_count"])
        
    def relative_modify_score(self, delta_score: int):
        self.score += delta_score
        self.score = max(0, self.score)
        self.score = min(self.score, InitializeInfo.max_score)
        
        self._level = self.score // InitializeInfo.level_gap
    
    def update_to_db(self, student_db: DatabaseManager):
        student_db.execute_custom_command(
            """
            UPDATE students SET score = ? WHERE id = ?
            """.strip(),
            (self.score, self.id),
            should_commit=True
        )
    
    def modify_wrong_question_to_db(self, question_description: str, correct_answer: str | None, student_db: DatabaseManager, mistake: int):
        """
        TODO
        Modify mistake count in database, if no this record, create one and set mistake count

        Args:
            student_db (DatabaseManager): The student database manager object
            mistake (int): the abstract value want to apply in database
        """
        # - check exist
        if student_db.execute_custom_command(
            f"""
            select id from "{self.id}" where question = ?
            """
            .strip(),
            (question_description, ),
            False
        ).fetchone() is None:
            if correct_answer is None:
                raise ValueError("Parameter `correct_answer` must null")
            # create
            student_db.execute_custom_command(
                f"""
                insert into "{self.id}" (question, answer, mistake_count) values (?, ?, ?) 
                """.strip(),
                (question_description, correct_answer, InitializeInfo.default_mistake_count + mistake)
            )
        else:
            # This means the record exist, just update mistake count
            student_db.execute_custom_command(
                f"""
                update "{self.id}" SET mistake_count = mistake_count + ?
                """.strip(),
                (mistake, )
            )
    