@echo off
REM Script untuk setup Gemini API Key di Windows
echo ========================================
echo Setup Gemini API Key
echo ========================================
echo.
echo Langkah-langkah:
echo 1. Dapatkan API key dari: https://aistudio.google.com/app/apikey
echo 2. Copy API key Anda
echo 3. Jalankan perintah di bawah ini di Command Prompt:
echo.
echo    set GEMINI_API_KEY=your-api-key-here
echo.
echo 4. Atau untuk permanent, set di System Environment Variables
echo.
echo ========================================
echo.
echo Cek status saat ini:
python -c "import os; key = os.getenv('GEMINI_API_KEY'); print('API Key:', 'SET' if key else 'NOT SET')"
echo.
echo ========================================
echo.
echo Setelah set API key, jalankan: python test_gemini.py
echo.
pause

