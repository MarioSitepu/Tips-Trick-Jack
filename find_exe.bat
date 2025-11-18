@echo off
REM Script untuk mencari dan menampilkan lokasi EXE yang tersedia
REM Mendeteksi nama baru dan lama

echo ============================================================
echo Gemini Project Generator - EXE Finder
echo ============================================================
echo.

set "FOUND=0"

REM Cek nama baru di dist folder
if exist "%~dp0dist\Gemini-Project-Generator.exe" (
    echo [OK] Found: dist\Gemini-Project-Generator.exe
    echo    Full path: %~dp0dist\Gemini-Project-Generator.exe
    set "FOUND=1"
)

REM Cek nama baru di root
if exist "%~dp0Gemini-Project-Generator.exe" (
    echo [OK] Found: Gemini-Project-Generator.exe
    echo    Full path: %~dp0Gemini-Project-Generator.exe
    set "FOUND=1"
)

REM Cek nama lama di dist folder (legacy)
if exist "%~dp0dist\AI-Daily-Summary.exe" (
    echo [LEGACY] Found: dist\AI-Daily-Summary.exe (old name)
    echo    Full path: %~dp0dist\AI-Daily-Summary.exe
    echo    Note: Please rebuild to get new name
    set "FOUND=1"
)

REM Cek nama lama di root (legacy)
if exist "%~dp0AI-Daily-Summary.exe" (
    echo [LEGACY] Found: AI-Daily-Summary.exe (old name)
    echo    Full path: %~dp0AI-Daily-Summary.exe
    echo    Note: Please rebuild to get new name
    set "FOUND=1"
)

if "%FOUND%"=="0" (
    echo [ERROR] No EXE found!
    echo.
    echo Searched locations:
    echo   - %~dp0dist\Gemini-Project-Generator.exe
    echo   - %~dp0Gemini-Project-Generator.exe
    echo   - %~dp0dist\AI-Daily-Summary.exe (legacy)
    echo   - %~dp0AI-Daily-Summary.exe (legacy)
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

