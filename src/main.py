from initialize import load_config, InitializeInfo
from database import DatabaseManager
from window.quiz_window import QuizWindow
from PyQt5.QtWidgets import QApplication
from window.application_controller import ApplicationController
import sys


def main():
    # Initalize database connection
    try:
        load_config()
        
        # Initialize window
        application_controller = ApplicationController()
        application_controller.run()
    except Exception as e:
        print(f"Error during initialization: {e}")
        sys.exit(1)
        
    # Run application
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()

    
    