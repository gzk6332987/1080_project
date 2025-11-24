import tomllib


def load_db_config() -> dict[str, str]:
    with open("config.toml", "rb") as f:
        config_raw = tomllib.load(f)
        
    db_config = config_raw.get("database", {})
    
    return {
        "questions_db_path": db_config.get("questions_db_path", "data/questions.sqlite3"),
        "students_db_path": db_config.get("students_db_path", "data/students.sqlite3"),
    }
    
    