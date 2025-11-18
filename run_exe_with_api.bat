@echo off
REM Launcher untuk EXE dengan API Key
REM Edit API key di bawah ini

set GEMINI_API_KEY=your-api-key-here

REM Ganti dengan path ke EXE Anda
cd /d "%~dp0"

REM Deteksi EXE (prioritas: nama baru -> nama lama)
set "EXE_NAME="
set "EXE_PATH="
set "SCRIPT_DIR=%~dp0"

REM Normalize path (remove trailing backslash)
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

REM Cek nama baru di dist folder
if exist "%SCRIPT_DIR%\dist\Gemini-Project-Generator.exe" (
    set "EXE_NAME=Gemini-Project-Generator.exe"
    set "EXE_PATH=%SCRIPT_DIR%\dist\Gemini-Project-Generator.exe"
    goto :found
)

REM Cek nama baru di root
if exist "%SCRIPT_DIR%\Gemini-Project-Generator.exe" (
    set "EXE_NAME=Gemini-Project-Generator.exe"
    set "EXE_PATH=%SCRIPT_DIR%\Gemini-Project-Generator.exe"
    goto :found
)

REM Cek nama lama di dist folder (legacy)
if exist "%SCRIPT_DIR%\dist\AI-Daily-Summary.exe" (
    set "EXE_NAME=AI-Daily-Summary.exe"
    set "EXE_PATH=%SCRIPT_DIR%\dist\AI-Daily-Summary.exe"
    goto :found
)

REM Cek nama lama di root (legacy)
if exist "%SCRIPT_DIR%\AI-Daily-Summary.exe" (
    set "EXE_NAME=AI-Daily-Summary.exe"
    set "EXE_PATH=%SCRIPT_DIR%\AI-Daily-Summary.exe"
    goto :found
)

REM Jika tidak ditemukan, tampilkan error
echo [ERROR] EXE not found!
echo.
echo Searched locations:
echo   - %SCRIPT_DIR%\dist\Gemini-Project-Generator.exe
echo   - %SCRIPT_DIR%\Gemini-Project-Generator.exe
echo   - %SCRIPT_DIR%\dist\AI-Daily-Summary.exe (legacy)
echo   - %SCRIPT_DIR%\AI-Daily-Summary.exe (legacy)
echo.
echo Please build EXE first with: build.bat
pause
exit /b 1

:found

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

