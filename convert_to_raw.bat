@echo off
cd /d "%~dp0"
echo Running conversion script in %CD%
python "%~dp0\convert_to_raw.py"
pause
