import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QMessageBox)

class QuizWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Quiz App")
        self.setGeometry(200, 200, 500, 300)
        self.initUI()
    
    def initUI(self):
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create layout
        layout = QVBoxLayout()
        
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
        self.show_answer_button = QPushButton("Show Correct Answer")
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
        self.submit_button.clicked.connect(self.check_answer)
        self.show_answer_button.clicked.connect(self.show_correct_answer)
        
        # Add widgets to layout
        layout.addWidget(self.question_label)
        layout.addWidget(self.answer_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.show_answer_button)
        
        central_widget.setLayout(layout)
    
    def check_answer(self):
        user_answer = self.answer_input.text().strip()
        if user_answer:
            QMessageBox.information(self, "Answer Submitted", 
                                  f"You answered: {user_answer}\n\nClick 'Show Correct Answer' to see the correct answer!")
        else:
            QMessageBox.warning(self, "No Answer", "Please enter an answer first!")
    
    def show_correct_answer(self):
        correct_answer = "Paris"
        QMessageBox.information(self, "Correct Answer", 
                              f"The correct answer is: {correct_answer}")
        
    def update(self, quesion: str, answer: str):
        self.question_label.setText(quesion)
        


def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    window = QuizWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()