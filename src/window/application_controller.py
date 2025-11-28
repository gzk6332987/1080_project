from window.login_window import LoginWindow
from window.quiz_window import QuizWindow
from window.register_window import RegisterWindow
from PyQt5.QtWidgets import QApplication
from student import Student
import sys

RegisterWindow.__init__
class ApplicationController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = LoginWindow()
        self.quiz_window = QuizWindow()
        self.register_window = RegisterWindow()
        
        self.login_window.login_success.connect(self.show_quiz_window)
        self.login_window.require_register.connect(self.show_register)
        
    
    def show_login(self):
        self.login_window.show()
        
    def show_quiz_window(self, student: Student):
        self.quiz_window.set_student(student)
        self.quiz_window.show()
        if self.login_window.isVisible():
            self.login_window.close()
            
    def show_register(self):
        self.register_window.show()
            
    def run(self):
        self.show_login()
        sys.exit(self.app.exec_())
        