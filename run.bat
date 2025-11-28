@echo off
chcp 65001 >nul

cd /d "%~dp0"

echo -e "\033[32We suggest you run script/pull_latest.sh to update project(not force), in case of some critical problems were fixed\033[0m"

timeout /t 1 /nobreak >nul

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

:: Now run your Python script
python src\main.py

pause