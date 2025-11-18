@echo off
REM Script untuk test git commit dan push ke Project-Showcase
echo ============================================================
echo Test Git Commit & Push - Project Showcase
echo ============================================================
echo.

set "SHOWCASE_PATH=%~dp0..\Project-Showcase"

if not exist "%SHOWCASE_PATH%" (
    echo [ERROR] Project-Showcase folder not found!
    pause
    exit /b 1
)

cd /d "%SHOWCASE_PATH%"

echo [1] Checking git status...
git status --short
echo.

echo [2] Checking for uncommitted files in projects/...
if exist "projects" (
    dir /b projects | find /c /v "" > temp_count.txt
    set /p PROJECT_COUNT=<temp_count.txt
    del temp_count.txt
    echo    Found %PROJECT_COUNT% project folders
) else (
    echo    No projects folder found!
)
echo.

echo [3] Checking GitHub token...
if defined GITHUBTOKENPAT (
    echo    [OK] GITHUBTOKENPAT is set
) else if defined GITHUB_TOKEN_PAT (
    echo    [OK] GITHUB_TOKEN_PAT is set
) else if defined GITHUB_TOKEN (
    echo    [OK] GITHUB_TOKEN is set
) else (
    echo    [WARNING] No GitHub token found!
    echo    Set one of: GITHUBTOKENPAT, GITHUB_TOKEN_PAT, or GITHUB_TOKEN
)
echo.

echo [4] Testing git add...
if exist "index.html" (
    echo    Adding: projects/ and index.html
    git add projects/ index.html 2>&1
) else (
    echo    index.html not found, only adding projects/
    git add projects/ 2>&1
)
if errorlevel 1 (
    echo    [ERROR] Git add failed!
) else (
    echo    [OK] Git add successful
)
echo.

echo [5] Checking staged files...
git diff --cached --name-only
echo.

echo [6] Testing git commit (dry-run)...
git diff --cached --quiet
if errorlevel 1 (
    echo    [OK] There are changes to commit
    echo    Would commit with message: "🎨 Test commit from script"
) else (
    echo    [INFO] No changes to commit (all files already committed)
)
echo.

echo [7] Checking remote URL...
git remote get-url origin
echo.

echo ============================================================
echo Test complete!
echo.
echo If you want to actually commit and push, run:
echo   git commit -m "Test commit"
echo   git push origin main
echo ============================================================
pause

