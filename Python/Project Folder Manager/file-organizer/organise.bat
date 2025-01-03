@echo off
set THIS_PATH=%~dp0
python "%THIS_PATH%src\main.py" . *.url
echo Done!
pause