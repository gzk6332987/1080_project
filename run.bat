@echo off
chcp 65001 >nul

cd /d "%~dp0"

echo Activating virtual environment...

python -m pip install virtualenv

python -m virtualenv venv

call venv\Scripts\activate.bat

pip install -r requirements.txt

if errorlevel 1 (
    echo Failed to activate virtual environment.
    exit /b 1
)

echo Virtual environment activated successfully!

timeout /t 1 /nobreak >nul

:: Now run your Python script
python src\main.py

pause