import tomllib
from database import DatabaseManager

class InitializeInfo:
    questions_db_path: str
    students_db_path: str
    
    question_db: DatabaseManager
    student_db: DatabaseManager
    
    default_mistake_count: int
    review_factor: float
    
    default_score: int
    max_score: int
    level_gap: int
    question_score: int
    high_level_score: int
    
    


def load_config():
    with open("config.toml", "rb") as f:
        config_raw = tomllib.load(f)
        
    db_config = config_raw.get("database", {})
    
    InitializeInfo.questions_db_path = db_config.get("questions_db_path", "data/questions.sqlite3")
    InitializeInfo.students_db_path = db_config.get("students_db_path", "data/students.sqlite3")
    
    InitializeInfo.question_db = DatabaseManager(InitializeInfo.questions_db_path)
    InitializeInfo.student_db = DatabaseManager(InitializeInfo.students_db_path)
    
    review_setting = config_raw.get("review_setting", {})
    InitializeInfo.default_mistake_count = int(review_setting.get("default_mistake_count"))
    InitializeInfo.review_factor = float(review_setting.get("review_factor"))
    
    score_setting = int(config_raw.get("score_setting", {}))
    InitializeInfo.default_score = int(score_setting.get("default_score"))
    InitializeInfo.max_score = int(score_setting.get("max_score"))
    InitializeInfo.level_gap = int(score_setting.get("level_gap"))
    InitializeInfo.question_score = int(score_setting.get("question_score"))
    InitializeInfo.high_level_score = int(score_setting.get("high_level_score"))
    
    
    