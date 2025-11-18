@echo off
REM Build script untuk Windows - Convert ke EXE
echo ========================================
echo Gemini Project Generator - EXE Builder
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

REM Cek apakah EXE berhasil dibuat
if exist "dist\Gemini-Project-Generator.exe" (
    echo [SUCCESS] EXE created successfully!
    echo.
    echo EXE Location: dist\Gemini-Project-Generator.exe
    echo.
    echo Next steps:
    echo   1. Run: run_exe_with_api.bat (to test with API key)
    echo   2. Or: setup_startup.bat (to add to Windows startup)
    echo   3. Or: Double-click dist\Gemini-Project-Generator.exe
) else if exist "dist\AI-Daily-Summary.exe" (
    echo [WARNING] Old EXE name found: AI-Daily-Summary.exe
    echo   Please rebuild to get new name: Gemini-Project-Generator.exe
) else (
    echo [WARNING] EXE not found in dist folder.
    echo   Please check build errors above.
)

echo.
pause

