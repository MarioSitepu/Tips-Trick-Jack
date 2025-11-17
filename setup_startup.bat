@echo off
REM Script untuk menambahkan AI-Daily-Summary.exe ke Windows Startup
REM Menggunakan PowerShell untuk membuat shortcut

echo ============================================================
echo AI-Daily-Summary - Startup Setup
echo ============================================================
echo.

REM Cari EXE
set "EXE_PATH=%~dp0dist\AI-Daily-Summary.exe"
if not exist "%EXE_PATH%" (
    set "EXE_PATH=%~dp0AI-Daily-Summary.exe"
    if not exist "%EXE_PATH%" (
        echo [ERROR] AI-Daily-Summary.exe not found!
        echo    Searched in: %~dp0dist\
        echo    Searched in: %~dp0
        echo.
        echo Please run this script from the project root directory.
        pause
        exit /b 1
    )
)

echo [OK] Found EXE: %EXE_PATH%
echo.

REM Get Startup folder
set "STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "SHORTCUT_PATH=%STARTUP_FOLDER%\AI-Daily-Summary.lnk"

REM Check if already exists
if exist "%SHORTCUT_PATH%" (
    echo [WARNING] Already in startup!
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

