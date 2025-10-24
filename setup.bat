@echo off
SETLOCAL

REM -----------------------------
REM Check if Python is installed
REM -----------------------------
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b 1
)

echo Python detected: 
python --version

REM -----------------------------
REM Set project directory
REM -----------------------------
SET "PROJECT_DIR=%CD%"
SET "VENV_DIR=%PROJECT_DIR%\venv"

REM -----------------------------
REM Create virtual environment if not exists
REM -----------------------------
IF NOT EXIST "%VENV_DIR%" (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
) ELSE (
    echo Virtual environment already exists.
)

REM -----------------------------
REM Activate venv and install requirements
REM -----------------------------
IF EXIST "%PROJECT_DIR%\requirements.txt" (
    echo Installing packages from requirements.txt...
    call "%VENV_DIR%\Scripts\activate.bat"
    pip install --upgrade pip
    pip install -r "%PROJECT_DIR%\requirements.txt"
    call "%VENV_DIR%\Scripts\deactivate.bat"
) ELSE (
    echo No requirements.txt found, skipping package installation.
)

echo Done!
pause
