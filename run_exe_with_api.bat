@echo off
REM Launcher untuk EXE dengan API Key
REM Edit API key di bawah ini

set GEMINI_API_KEY=your-api-key-here

REM Ganti dengan path ke EXE Anda
cd /d "%~dp0"
if exist "dist\AI-Daily-Summary.exe" (
    echo Starting AI Daily Summary Generator...
    echo API Key: SET
    dist\AI-Daily-Summary.exe
) else if exist "AI-Daily-Summary.exe" (
    echo Starting AI Daily Summary Generator...
    echo API Key: SET
    AI-Daily-Summary.exe
) else (
    echo Error: AI-Daily-Summary.exe not found!
    echo Please build EXE first with: build.bat
    pause
)

