@echo off
REM Script untuk mencari dan menampilkan lokasi EXE yang tersedia
REM Mendeteksi nama baru dan lama

echo ============================================================
echo Gemini Project Generator - EXE Finder
echo ============================================================
echo.

set "FOUND=0"
set "SCRIPT_DIR=%~dp0"

REM Normalize path (remove trailing backslash)
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

REM Cek nama baru di dist folder
if exist "%SCRIPT_DIR%\dist\Gemini-Project-Generator.exe" (
    echo [OK] Found: dist\Gemini-Project-Generator.exe
    echo    Full path: %SCRIPT_DIR%\dist\Gemini-Project-Generator.exe
    set "FOUND=1"
)

REM Cek nama baru di root
if exist "%SCRIPT_DIR%\Gemini-Project-Generator.exe" (
    echo [OK] Found: Gemini-Project-Generator.exe
    echo    Full path: %SCRIPT_DIR%\Gemini-Project-Generator.exe
    set "FOUND=1"
)

REM Cek nama lama di dist folder (legacy)
if exist "%SCRIPT_DIR%\dist\AI-Daily-Summary.exe" (
    echo [LEGACY] Found: dist\AI-Daily-Summary.exe (old name)
    echo    Full path: %SCRIPT_DIR%\dist\AI-Daily-Summary.exe
    echo    Note: Please rebuild to get new name
    set "FOUND=1"
)

REM Cek nama lama di root (legacy)
if exist "%SCRIPT_DIR%\AI-Daily-Summary.exe" (
    echo [LEGACY] Found: AI-Daily-Summary.exe (old name)
    echo    Full path: %SCRIPT_DIR%\AI-Daily-Summary.exe
    echo    Note: Please rebuild to get new name
    set "FOUND=1"
)

if "%FOUND%"=="0" (
    echo [ERROR] No EXE found!
    echo.
    echo Searched locations:
    echo   - %SCRIPT_DIR%\dist\Gemini-Project-Generator.exe
    echo   - %SCRIPT_DIR%\Gemini-Project-Generator.exe
    echo   - %SCRIPT_DIR%\dist\AI-Daily-Summary.exe (legacy)
    echo   - %SCRIPT_DIR%\AI-Daily-Summary.exe (legacy)
    echo.
    echo Current directory: %CD%
    echo Script directory: %SCRIPT_DIR%
    echo.
    echo Please build EXE first with: build.bat
) else (
    echo.
    echo ============================================================
    echo Use one of these scripts to run:
    echo   - run_exe_with_api.bat (with API key)
    echo   - setup_startup.bat (add to Windows startup)
    echo ============================================================
)

echo.
pause

