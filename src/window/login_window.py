import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QMessageBox, QCheckBox, QFrame)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from initialize import InitializeInfo
from student import StudentBuilder, Student
import hashlib


class LoginWindow(QMainWindow):
    login_success = pyqtSignal(Student)  # Signal emitted on successful login
    
    def __init__(self, ):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Login System')
        self.setFixedSize(400, 500)
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #667eea, stop: 1 #764ba2);
            }
        """)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        
        # Title
        title = QLabel('Welcome Back')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 30px;
            }
        """)
        layout.addWidget(title)
        
        # Login frame
        login_frame = QFrame()
        login_frame.setFixedSize(320, 350)
        login_frame.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 15px;
                padding: 20px;
            }
        """)
        
        # Login form layout
        form_layout = QVBoxLayout(login_frame)
        form_layout.setSpacing(20)
        form_layout.setAlignment(Qt.AlignCenter)
        
        # Username section
        username_layout = QVBoxLayout()
        username_layout.setSpacing(8)
        
        username_label = QLabel('Username')
        username_label.setStyleSheet("""
            QLabel {
                color: #333;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Enter your username')
        self.username_input.setFixedHeight(45)
        self.username_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                padding: 0 15px;
                font-size: 14px;
                background: #fafafa;
            }
            QLineEdit:focus {
                border-color: #667eea;
                background: white;
            }
        """)
        
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        
        # Password section
        password_layout = QVBoxLayout()
        password_layout.setSpacing(8)
        
        password_label = QLabel('Password')
        password_label.setStyleSheet("""
            QLabel {
                color: #333;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Enter your password')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedHeight(45)
        self.password_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                padding: 0 15px;
                font-size: 14px;
                background: #fafafa;
            }
            QLineEdit:focus {
                border-color: #667eea;
                background: white;
            }
        """)
        
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        
        # Remember me checkbox
        self.remember_check = QCheckBox('Remember me')
        self.remember_check.setStyleSheet("""
            QCheckBox {
                color: #666;
                font-size: 13px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border-radius: 3px;
                border: 2px solid #ccc;
            }
            QCheckBox::indicator:checked {
                background: #667eea;
                border: 2px solid #667eea;
            }
        """)
        
        # Login button
        self.login_button = QPushButton('Login')
        self.login_button.setFixedHeight(50)
        self.login_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y1: 0,
                    stop: 0 #667eea, stop: 1 #764ba2);
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y1: 0,
                    stop: 0 #5a6fd8, stop: 1 #6a4190);
            }
            QPushButton:pressed {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y1: 0,
                    stop: 0 #4c5bc0, stop: 1 #5c3578);
            }
            QPushButton:disabled {
                background: #cccccc;
                color: #666666;
            }
        """)
        
        # Forgot password
        forgot_password = QLabel('<a href="#" style="color: #667eea; text-decoration: none;">Forgot password?</a>')
        forgot_password.setAlignment(Qt.AlignCenter)
        forgot_password.setOpenExternalLinks(False)
        
        # Add widgets to form layout
        form_layout.addLayout(username_layout)
        form_layout.addLayout(password_layout)
        form_layout.addWidget(self.remember_check)
        form_layout.addWidget(self.login_button)
        form_layout.addWidget(forgot_password)
        
        # Add login frame to main layout
        layout.addWidget(login_frame)
        
        # Connect signals
        self.login_button.clicked.connect(self.attempt_login)
        forgot_password.linkActivated.connect(self.forgot_password)
        self.username_input.returnPressed.connect(self.attempt_login)
        self.password_input.returnPressed.connect(self.attempt_login)
        
        # Enable/disable login button based on input
        self.username_input.textChanged.connect(self.validate_inputs)
        self.password_input.textChanged.connect(self.validate_inputs)
        self.validate_inputs()
        
    def validate_inputs(self):
        """Enable login button only if both fields have text"""
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        self.login_button.setEnabled(bool(username and password))
    
    def attempt_login(self):
        """Attempt to log in with provided credentials"""
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            self.show_message('Error', 'Please fill in all fields')
            return
        
        user_id = self.authenticate(username, password)
        if user_id != -1:
            self.show_message('Success', f'Welcome, {username}!', QMessageBox.Information)
            # Construct student
            student = StudentBuilder()\
                .set_id(user_id)\
                .set_name(username)\
                .build(InitializeInfo.student_db)
            self.login_success.emit(student)
        else:
            self.show_message('Error', 'Invalid username or password')
            self.password_input.clear()
            self.password_input.setFocus()
    
    def authenticate(self, username: str, password: str) -> int:
        """
        Authenticate user credentials
        In a real application, this would connect to a database or API
        """
        return InitializeInfo.student_db.check_password("students", "username", "password", username, self.hash_password(password))
    
    def hash_password(self, password: str) -> str:
        """Hash password for storage/verification"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def forgot_password(self):
        """Handle forgot password functionality"""
        self.show_message('Info', 'Please contact system administrator to reset your password.', QMessageBox.Information)
    
    def show_message(self, title: str, message: str, icon=QMessageBox.Warning):
        """Show message dialog"""
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.exec_()
        

# test the login window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    window = LoginWindow()
    window.show()
    
    sys.exit(app.exec_())