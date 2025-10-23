@echo off
cd /d "%~dp0"

REM --- Find Python ---
where python >nul 2>nul || py -3 -V >nul 2>nul
if errorlevel 1 (
  echo [ERROR] Python not found. Install Python 3.10+ and add to PATH.
  pause
  exit /b 1
)
set "PY=python"
where python >nul 2>nul || set "PY=py -3"

REM --- Create venv if not exists ---
if not exist ".venv\Scripts\python.exe" (
  echo Creating virtual environment...
  %PY% -m venv .venv || (echo Failed to create venv & pause & exit /b 1)
)

REM --- Activate venv ---
call ".venv\Scripts\activate.bat" || (echo Failed to activate venv & pause & exit /b 1)

REM --- Upgrade pip & install requirements ---
python -m pip install --upgrade pip >nul
if exist "requirements.txt" (
  echo Installing dependencies...
  pip install -r requirements.txt || (echo Install failed & pause & exit /b 1)
)

REM --- Run the app ---
echo.
echo Starting app.py...
python -u app.py

pause