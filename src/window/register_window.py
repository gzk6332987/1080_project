from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit, QApplication
from PyQt5.uic import loadUi
import sys


class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("src/window/ui_files/register_window.ui", self)
        
        self.pushButton.clicked.connect(self.say)
            
    def say(self):
        print("Hello")
    
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
    