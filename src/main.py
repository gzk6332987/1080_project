from initialize import load_db_config
from database import DatabaseManager
from window.quiz_window import QuizWindow
from PyQt5.QtWidgets import QApplication
import sys


def main():
    # Initalize database connection
    try:
        db_info = load_db_config()
        q_db_path = db_info.get("questions_db_path")
        s_db_path = db_info.get("students_db_path")
        question_db = DatabaseManager(q_db_path)
        student_db = DatabaseManager(s_db_path)
        
        # Initialize window
        app = QApplication(sys.argv)
        window = QuizWindow()
        window.show()
    except Exception as e:
        print(f"Error during initialization: {e}")
        sys.exit(1)
        
    # Run application
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    # main()
    load_db_config()
    
    from window.application_controller import ApplicationController
    controller = ApplicationController()
    controller.run()
    
    