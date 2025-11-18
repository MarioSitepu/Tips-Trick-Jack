@echo off
REM Script untuk cek status git di Project-Showcase
echo ============================================================
echo Check Git Status - Project Showcase
echo ============================================================
echo.

set "SHOWCASE_PATH=%~dp0..\Project-Showcase"

if not exist "%SHOWCASE_PATH%" (
    echo [ERROR] Project-Showcase folder not found!
    echo    Expected: %SHOWCASE_PATH%
    echo.
    pause
    exit /b 1
)

echo [OK] Showcase path: %SHOWCASE_PATH%
echo.

REM Cek apakah ini git repo
if not exist "%SHOWCASE_PATH%\.git" (
    echo [WARNING] Not a git repository!
    echo    Please initialize or clone the repository first.
    echo.
    echo To initialize:
    echo   cd "%SHOWCASE_PATH%"
    echo   git init
    echo   git remote add origin https://github.com/MarioSitepu/Jack-s-Cards.git
    echo.
    pause
    exit /b 1
)

echo [OK] Git repository detected
echo.

REM Cek remote
echo Checking remote...
cd /d "%SHOWCASE_PATH%"
git remote -v
echo.

REM Cek status
echo Checking status...
git status --short
echo.

REM Cek last commit
echo Last commit:
git log -1 --oneline
echo.

REM Cek branch
echo Current branch:
git branch --show-current
echo.

echo ============================================================
echo Check complete!
echo ============================================================
pause

