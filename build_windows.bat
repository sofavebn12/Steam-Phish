@echo off
setlocal

REM Build a Windows .exe using PyInstaller. Run from repository root on Windows.

python -m venv .venv
call .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

pyinstaller --noconsole --onefile --name SteamPhish src/main.py

echo Build complete. Check the dist folder for SteamPhish.exe
