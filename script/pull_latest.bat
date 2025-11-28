@echo off
REM git_auto_pull.bat - Auto pull with automatic directory change

setlocal EnableDelayedExpansion

REM Auto CD to script directory
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Configuration
set "BRANCH=main"
set "LOG_FILE=git_auto_pull.log"

echo [%date% %time%] Script running from: %SCRIPT_DIR%
echo [%date% %time%] Current directory: %cd%

REM Check if this is a git repository
if not exist ".git" (
    echo [%date% %time%] ERROR: Not a git repository
    echo [%date% %time%] Please run this script from a git repository directory
    pause
    exit /b 1
)

REM Fetch latest changes
echo [%date% %time%] Fetching latest changes...
git fetch origin

REM Get local and remote commit hashes
for /f "tokens=*" %%i in ('git rev-parse HEAD') do set "LOCAL_COMMIT=%%i"
for /f "tokens=*" %%i in ('git rev-parse origin/%BRANCH%') do set "REMOTE_COMMIT=%%i"

REM Compare commits
if "%LOCAL_COMMIT%"=="%REMOTE_COMMIT%" (
    echo [%date% %time%] Already up-to-date.
) else (
    echo [%date% %time%] Pulling new changes...
    git pull origin %BRANCH%
    echo [%date% %time%] Successfully updated!
)

pause