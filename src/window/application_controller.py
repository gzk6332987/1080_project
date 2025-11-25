from .login_window import LoginWindow
from .quiz_window import QuizWindow
from PyQt5.QtWidgets import QApplication
from student import Student
import sys


class ApplicationController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = LoginWindow()
        self.quiz_window = QuizWindow()
        
        self.login_window.login_success.connect(self.show_quiz_window)
    
    def show_login(self):
        self.login_window.show()
        
    def show_quiz_window(self, student: Student):
        self.quiz_window.set_student(student)
        self.quiz_window.show()
        if self.login_window.isVisible():
            self.login_window.close()
            
    def run(self):
        self.show_login()
        sys.exit(self.app.exec_())
        