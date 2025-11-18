@echo off
REM Script untuk manual commit dan push semua file di Project-Showcase
echo ============================================================
echo Manual Git Commit & Push - Project Showcase
echo ============================================================
echo.

set "SHOWCASE_PATH=%~dp0..\Project-Showcase"

if not exist "%SHOWCASE_PATH%" (
    echo [ERROR] Project-Showcase folder not found!
    pause
    exit /b 1
)

cd /d "%SHOWCASE_PATH%"

echo [1] Checking for changes...
git status --short
echo.

echo [2] Adding files...
if exist "index.html" (
    echo    Adding: projects/ and index.html
    git add projects/ index.html
) else (
    echo    index.html not found, only adding projects/
    git add projects/
)
if errorlevel 1 (
    echo [ERROR] Git add failed!
    pause
    exit /b 1
)
echo [OK] Files added
echo.

echo [3] Checking staged files...
git diff --cached --name-only
echo.

echo [4] Committing...
set "COMMIT_MSG=🤖 Manual commit: Update projects and gallery"
git commit -m "%COMMIT_MSG%"
if errorlevel 1 (
    echo [WARNING] Commit failed or no changes to commit
    git status
) else (
    echo [OK] Committed successfully
)
echo.

echo [5] Checking GitHub token...
set "GIT_TOKEN="
if defined GITHUBTOKENPAT (
    set "GIT_TOKEN=%GITHUBTOKENPAT%"
    echo [OK] Using GITHUBTOKENPAT
) else if defined GITHUB_TOKEN_PAT (
    set "GIT_TOKEN=%GITHUB_TOKEN_PAT%"
    echo [OK] Using GITHUB_TOKEN_PAT
) else if defined GITHUB_TOKEN (
    set "GIT_TOKEN=%GITHUB_TOKEN%"
    echo [OK] Using GITHUB_TOKEN
) else (
    echo [WARNING] No GitHub token found - push may fail
)
echo.

echo [6] Updating remote URL with token (if available)...
if defined GIT_TOKEN (
    git remote get-url origin > temp_remote.txt
    set /p REMOTE_URL=<temp_remote.txt
    del temp_remote.txt
    
    echo Current remote: %REMOTE_URL%
    
    if not "%REMOTE_URL%"=="" (
        if not "%REMOTE_URL:github.com=%"=="%REMOTE_URL%" (
            if not "%REMOTE_URL:x-access-token=%"=="%REMOTE_URL%" (
                echo Remote already has token
            ) else (
                for /f "tokens=*" %%a in ("%REMOTE_URL%") do set "REMOTE_URL=%%a"
                set "REMOTE_URL=%REMOTE_URL:https://github.com/=%"
                set "REMOTE_URL=%REMOTE_URL:.git=%"
                set "NEW_URL=https://x-access-token:%GIT_TOKEN%@github.com/%REMOTE_URL%.git"
                git remote set-url origin "%NEW_URL%"
                echo [OK] Updated remote URL with token
            )
        )
    )
) else (
    echo Skipping remote URL update (no token)
)
echo.

echo [7] Pushing to origin/main...
git push origin main
if errorlevel 1 (
    echo [ERROR] Push failed!
    echo.
    echo Troubleshooting:
    echo 1. Check if GitHub token is set correctly
    echo 2. Check if you have push permission
    echo 3. Check network connection
) else (
    echo [SUCCESS] Pushed successfully!
)
echo.

echo ============================================================
echo Manual push complete!
echo ============================================================
pause

