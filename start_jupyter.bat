@echo off
REM Change to the directory where this script is located
cd /d "%~dp0"
REM Launch Jupyter Notebook using Python from PATH
python -m notebook
pause