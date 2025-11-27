from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLineEdit


class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        self.username_edit_line = QLineEdit("")
        self.username_edit_line.setPlaceholderText("Please enter your username")
        self.username_edit_line.setStyleSheet("padding: 8px; font-size: 14px; margin: 10px;")
        

        self.password_edit_line = QLineEdit()
    
    