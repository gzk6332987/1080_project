from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sys

from database import DatabaseManager
import hashlib
from window.login_window import LoginWindow
from initialize import InitializeInfo

class RegisterWindow(QMainWindow):
    student_db = None
    
    def __init__(self):
        super().__init__()
        loadUi("src/window/ui_files/register_window.ui", self)
        self.student_db = InitializeInfo.student_db
        self.regButton.clicked.connect(self.create_user)
        
    def create_user(self):
        # get input content
        username = self.username.text().strip()
        password = self.password.text().strip()
        if username == "" or password == "":
            QMessageBox(self, "NULL username or password is not allowed!")
            return
        # TODO check whether username exist
        
        self.student_db.insert_record("students", ["username", "password", "score"], [username, self.hash_password(password).hexdigest(), InitializeInfo.default_score])
        # redirect to login window
        self.close()
        
        
    def hash_password(self, raw_password: str) -> str:
        return hashlib.sha256(raw_password.encode())
        
    # def init_ui(self):
    #     central_widget = QWidget()
    #     self.setCentralWidget(central_widget)
        
    #     layout = QVBoxLayout()
        
    #     self.username_edit_line = QLineEdit("")
    #     self.username_edit_line.setPlaceholderText("Please enter your username")
    #     self.username_edit_line.setStyleSheet("padding: 8px; font-size: 14px; margin: 10px;")

    #     self.password_edit_line = QLineEdit()
    #     self.password_edit_line.setPlaceholderText("Please enter your password (Secure)")
    #     self.password_edit_line.setStyleSheet("padding: 8px; font-size: 14px; margin: 10px;")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    register_window = RegisterWindow()
    register_window.show()
    sys.exit(app.exec())
    