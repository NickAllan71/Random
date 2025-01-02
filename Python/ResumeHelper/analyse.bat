@echo off
set THIS_PATH=%~dp0
call %THIS_PATH%.venv\Scripts\activate.bat
python %THIS_PATH%python-workspace\src\main.py %1 %2
pause