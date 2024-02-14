@echo off
set fileName=%~nx0
echo Running NFolder...
set nfolder=nfolder.py
set scriptPath=%~dp0
python %scriptPath%%nfolder%