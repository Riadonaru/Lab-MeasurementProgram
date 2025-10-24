@echo off
SETLOCAL

REM -----------------------------
REM Set project and venv directories
REM -----------------------------
SET "PROJECT_DIR=%CD%"
SET "VENV_DIR=%PROJECT_DIR%\venv"
SET "SCRIPT_PATH=%PROJECT_DIR%\src\main.py"

REM -----------------------------
REM Check if virtual environment exists
REM -----------------------------
IF NOT EXIST "%VENV_DIR%\Scripts\activate.bat" (
    echo Virtual environment not found. Please run setup_venv.bat first.
    pause
    exit /b 1
)

REM -----------------------------
REM Activate venv and run the script
REM -----------------------------
echo Activating virtual environment...
call "%VENV_DIR%\Scripts\activate.bat"

echo Running script: %SCRIPT_PATH%
python "%SCRIPT_PATH%"

REM -----------------------------
REM Deactivate venv
REM -----------------------------
call "%VENV_DIR%\Scripts\deactivate.bat"

pause
