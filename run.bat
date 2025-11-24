@echo off
echo [32mActivating virtual environment...[0m

call venv\Scripts\activate.bat

if errorlevel 1 (
    echo [31mFailed to activate virtual environment.[0m
    exit /b 1
)

echo [32mVirtual environment activated successfully![0m

timeout /t 1 /nobreak >nul
REM Now run your Python script
python src\main.py