@echo off
REM Build script untuk Windows - Convert ke EXE
echo ========================================
echo AI Daily Summary Generator - EXE Builder
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found!
    echo Please install Python first.
    pause
    exit /b 1
)

echo Step 1: Installing dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Step 2: Building executable...
python build_exe.py

echo.
echo ========================================
echo Build process completed!
echo ========================================
echo.
echo Your EXE file is in the 'dist' folder.
echo.
pause

