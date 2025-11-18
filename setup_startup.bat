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
set "SCRIPT_DIR=%~dp0"

REM Normalize path (remove trailing backslash)
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

REM Cek nama baru di dist folder
if exist "%SCRIPT_DIR%\dist\Gemini-Project-Generator.exe" (
    set "EXE_NAME=Gemini-Project-Generator"
    set "EXE_PATH=%SCRIPT_DIR%\dist\Gemini-Project-Generator.exe"
    goto :found
)

REM Cek nama baru di root
if exist "%SCRIPT_DIR%\Gemini-Project-Generator.exe" (
    set "EXE_NAME=Gemini-Project-Generator"
    set "EXE_PATH=%SCRIPT_DIR%\Gemini-Project-Generator.exe"
    goto :found
)

REM Cek nama lama di dist folder (legacy)
if exist "%SCRIPT_DIR%\dist\AI-Daily-Summary.exe" (
    set "EXE_NAME=AI-Daily-Summary"
    set "EXE_PATH=%SCRIPT_DIR%\dist\AI-Daily-Summary.exe"
    goto :found
)

REM Cek nama lama di root (legacy)
if exist "%SCRIPT_DIR%\AI-Daily-Summary.exe" (
    set "EXE_NAME=AI-Daily-Summary"
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
echo Current directory: %CD%
echo Script directory: %SCRIPT_DIR%
echo.
echo Please run this script from the project root directory.
echo Or build EXE first with: build.bat
pause
exit /b 1

:found

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

