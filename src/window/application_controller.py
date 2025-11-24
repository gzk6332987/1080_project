from login_window import LoginWindow
from quiz_window import QuizWindow
from PyQt5.QtWidgets import QApplication
import sys


class ApplicationController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = LoginWindow()
        self.quiz_window = QuizWindow()
        
        self.login_window.login_success.connect(self.show_main_window)
    
    def show_login(self):
        self.login_window
        
    def show_main_window(self, user_id: int):
        pass