import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QMessageBox)

from initialize import InitializeInfo
from student import Student


class QuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Quiz App")
        self.setGeometry(200, 200, 500, 300)
        self.init_ui()
        
        self.check_callback: callable[[str], int] = None  # Callback function to verify answers
        self.student: Student = None
        self.correct_answer = ""
        
    def set_student(self, student: Student):
        self.student = student
        # refresh score/level display when a student is set
        self.refresh_status()
    
    def init_ui(self):
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create layout
        layout = QVBoxLayout()
        
        # Score and Level labels
        self.score_level_label = QLabel("Score: 0 | Level: 0")
        self.score_level_label.setStyleSheet("font-size: 14px; margin: 6px;")



        # Question label (Update it later...)
        self.question_label = QLabel("Sorry, we don't have questions available at the moment ):")
        self.question_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        
        # Answer input field
        self.answer_input = QLineEdit()
        self.answer_input.setPlaceholderText("Enter your answer here...")
        self.answer_input.setStyleSheet("padding: 8px; font-size: 14px; margin: 10px;")
    
        # Submit button
        self.submit_button = QPushButton("Check Answer")
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
                margin: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        
        # Show answer button
        self.show_answer_button = QPushButton("Next question")
        self.show_answer_button.setStyleSheet("""
            QPushButton {
                background-color: #008CBA;
                color: white;
                padding: 10px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
                margin: 10px;
            }
            QPushButton:hover {
                background-color: #007B9A;
            }
        """)
        
        # Connect buttons to functions
        self.submit_button.clicked.connect(self.button_clicked)
        self.show_answer_button.clicked.connect(self.next_question)
        
        
        layout.addWidget(self.question_label)
        layout.addWidget(self.answer_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.show_answer_button)
        layout.addWidget(self.score_level_label)
        central_widget.setLayout(layout)
    
    def button_clicked(self):
        """
        verify the inputed answer use callback function
        """
        user_answer = self.answer_input.text().strip()
        if not user_answer:
            QMessageBox.warning(self, "No Answer", "Please enter an answer first!")
            return
            
        if answer_checker(user_answer, self.correct_answer):
            # get score
            increase_score = InitializeInfo.question_score
            self.student.relative_modify_score(increase_score)
            self.student.update_to_db(InitializeInfo.student_db)
            score = self.student.score
            level = self.student.get_level()
            # TODO log to database
            self.student.modify_wrong_question_to_db(self.question_label.text(), self.correct_answer, InitializeInfo.student_db, -1)
            # refresh UI status
            self.refresh_status()
            QMessageBox.information(self, "Nice", f"Good job, your score is {score} now! (level: {level})")
        else:
            decrease_score = InitializeInfo.wrong_answer_deduct
            self.student.relative_modify_score(-decrease_score)
            self.student.update_to_db(InitializeInfo.student_db)
            score = self.student.score
            level = self.student.get_level()
            # log into database
            self.student.modify_wrong_question_to_db(self.question_label.text(), self.correct_answer, InitializeInfo.student_db, 1)
            # refresh UI status
            self.refresh_status()
            QMessageBox.information(self, "Wrong", f"Wrong answer! your score is {score} now! (level: {level})")
        self.next_question()
            
    
    def next_question(self):
        if self.student is None:
            raise AttributeError("self.student equal to None, this is not allowed.")
        review_factor = InitializeInfo.review_factor
        random_num = random.random()
        
        if random_num > review_factor:
            # normal generate
            (question, answer) = self.student.generate_quiz_from_level()
        else:
            # get from database if have, if not, still generate normal
            (id, question, answer) = self.student.generate_quiz_from_db(InitializeInfo.student_db)
            
        (answer, is_rounded) = self.check_round(answer)
        
        self.update(question, answer, is_rounded)
        
    def update(self, question: str, answer: str, is_rounded: bool):
        self.answer_input.setText("")  # empty the answer input field
        self.correct_answer = answer
        self.question_label.setText(question + "(Round to 2 decimal place)") if is_rounded else self.question_label.setText(question)
        # also refresh status in case level/score changed
        self.refresh_status()

    def refresh_status(self):
        """Update the on-screen score and level labels from the current student."""
        if self.student is None:
            return
        try:
            score = getattr(self.student, 'score', 0)
        except Exception:
            score = 0
        try:
            level = self.student.get_level()
        except Exception:
            level = 0
        self.score_level_label.setText(f"Score: {score} | Level: {level}")
    
    def check_round(self, number: str) -> (str, bool):
        """
        Round a float number only if it has more than 2 decimal places

        Args:
            number (str): The float number as string

        Returns:
            str: The original number or rounded number
        """
        try:
            # Convert to float first
            num_float = float(number)
            
            # Check if it's an integer (no decimal part)
            if num_float.is_integer():
                return (str(int(num_float)), False)
            
            # Convert to string to check decimal places
            num_str = str(num_float)
            
            # Find the decimal point and check digits after it
            if '.' in num_str:
                integer_part, decimal_part = num_str.split('.')
                # If 2 or fewer decimal places, return original
                if len(decimal_part) <= 2:
                    return (num_str, False)
            
            # Only round if more than 2 decimal places
            return (f"{num_float:.2f}", True)
            
        except (ValueError, TypeError):
            return (number, False)

def answer_checker(answer, correct) -> bool:
    return str(answer) == str(correct)

if __name__ == "__main__":
    # This is just a TEST!!!
    
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    window = QuizWindow()
    window.show()
    
    sys.exit(app.exec_())