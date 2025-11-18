@echo off
REM Launcher untuk EXE dengan API Key
REM Edit API key di bawah ini

set GEMINI_API_KEY=your-api-key-here

REM Ganti dengan path ke EXE Anda
cd /d "%~dp0"

REM Deteksi EXE (prioritas: nama baru -> nama lama)
set "EXE_NAME="
set "EXE_PATH="

REM Cek nama baru di dist folder
if exist "dist\Gemini-Project-Generator.exe" (
    set "EXE_NAME=Gemini-Project-Generator.exe"
    set "EXE_PATH=dist\Gemini-Project-Generator.exe"
) else if exist "Gemini-Project-Generator.exe" (
    set "EXE_NAME=Gemini-Project-Generator.exe"
    set "EXE_PATH=Gemini-Project-Generator.exe"
) else if exist "dist\AI-Daily-Summary.exe" (
    REM Fallback ke nama lama
    set "EXE_NAME=AI-Daily-Summary.exe"
    set "EXE_PATH=dist\AI-Daily-Summary.exe"
) else if exist "AI-Daily-Summary.exe" (
    REM Fallback ke nama lama
    set "EXE_NAME=AI-Daily-Summary.exe"
    set "EXE_PATH=AI-Daily-Summary.exe"
)

if defined EXE_PATH (
    echo Starting Gemini Project Generator...
    echo EXE: %EXE_NAME%
    echo API Key: SET
    echo.
    %EXE_PATH%
) else (
    echo [ERROR] EXE not found!
    echo.
    echo Searched for:
    echo   - dist\Gemini-Project-Generator.exe
    echo   - Gemini-Project-Generator.exe
    echo   - dist\AI-Daily-Summary.exe (legacy)
    echo   - AI-Daily-Summary.exe (legacy)
    echo.
    echo Please build EXE first with: build.bat
    pause
)

