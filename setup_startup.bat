@echo off
REM Script untuk menambahkan Gemini-Project-Generator.exe ke Windows Startup
REM Menggunakan PowerShell untuk membuat shortcut

echo ============================================================
echo Gemini Project Generator - Startup Setup
echo ============================================================
echo.

REM Deteksi EXE (prioritas: nama baru -> nama lama)
set "EXE_NAME="
set "EXE_PATH="

REM Cek nama baru di dist folder
if exist "%~dp0dist\Gemini-Project-Generator.exe" (
    set "EXE_NAME=Gemini-Project-Generator"
    set "EXE_PATH=%~dp0dist\Gemini-Project-Generator.exe"
) else if exist "%~dp0Gemini-Project-Generator.exe" (
    set "EXE_NAME=Gemini-Project-Generator"
    set "EXE_PATH=%~dp0Gemini-Project-Generator.exe"
) else if exist "%~dp0dist\AI-Daily-Summary.exe" (
    REM Fallback ke nama lama
    set "EXE_NAME=AI-Daily-Summary"
    set "EXE_PATH=%~dp0dist\AI-Daily-Summary.exe"
) else if exist "%~dp0AI-Daily-Summary.exe" (
    REM Fallback ke nama lama
    set "EXE_NAME=AI-Daily-Summary"
    set "EXE_PATH=%~dp0AI-Daily-Summary.exe"
)

if not defined EXE_PATH (
    echo [ERROR] EXE not found!
    echo.
    echo Searched for:
    echo   - %~dp0dist\Gemini-Project-Generator.exe
    echo   - %~dp0Gemini-Project-Generator.exe
    echo   - %~dp0dist\AI-Daily-Summary.exe (legacy)
    echo   - %~dp0AI-Daily-Summary.exe (legacy)
    echo.
    echo Please run this script from the project root directory.
    echo Or build EXE first with: build.bat
    pause
    exit /b 1
)

echo [OK] Found EXE: %EXE_PATH%
echo [OK] App Name: %EXE_NAME%
echo.

REM Get Startup folder
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "SHORTCUT_PATH=%STARTUP_FOLDER%\%EXE_NAME%.lnk"

REM Check if already exists (cek nama baru dan lama)
set "OLD_SHORTCUT=%STARTUP_FOLDER%\AI-Daily-Summary.lnk"
set "NEW_SHORTCUT=%STARTUP_FOLDER%\Gemini-Project-Generator.lnk"

if exist "%SHORTCUT_PATH%" (
    echo [WARNING] Already in startup!
    echo    Shortcut: %SHORTCUT_PATH%
    echo.
    set /p REMOVE="Remove from startup? (y/n): "
    if /i "%REMOVE%"=="y" (
        del "%SHORTCUT_PATH%"
        echo [OK] Removed from startup successfully!
        pause
        exit /b 0
    ) else (
        echo Cancelled.
        pause
        exit /b 0
    )
)

REM Cek juga shortcut lama (untuk migration)
if exist "%OLD_SHORTCUT%" (
    if not "%SHORTCUT_PATH%"=="%OLD_SHORTCUT%" (
        echo [INFO] Found old shortcut, will be replaced.
        del "%OLD_SHORTCUT%"
    )
)

REM Create shortcut using PowerShell
echo Creating shortcut in Startup folder...
powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT_PATH%'); $Shortcut.TargetPath = '%EXE_PATH%'; $Shortcut.WorkingDirectory = '%~dp0'; $Shortcut.IconLocation = '%EXE_PATH%'; $Shortcut.Save()"

if exist "%SHORTCUT_PATH%" (
    echo.
    echo [SUCCESS] Added to startup successfully!
    echo    Shortcut: %SHORTCUT_PATH%
    echo.
    echo The application will start automatically when Windows boots.
) else (
    echo.
    echo [ERROR] Failed to create shortcut.
    echo    You may need to run as Administrator.
)

echo.
pause

