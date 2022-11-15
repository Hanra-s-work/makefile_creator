@REM The general compiler for the windows system
echo off
color 0A
cls
set CWD="%CD%"
echo "This program uses the python dependency pyinstaller"
echo "If you do not have it, please run 'pip install -U pyinstaller' in an command prompt with administrator rights to install it"
echo "Please terminate this script if you do not have it"
echo "! Warning:"
echo "! This script is meant to be run from the folder where it is located."
echo "! If you are not in the folder where this script is located, please terminate this script."
echo "! If you are in the folder where this script is located, please continue."
pause
if not "%1" == "" {
    cmd/c compile_program.bat %1
} else {
    cmd/c compile_program.bat makator.exe
}
cd %CWD%
cmd/c update_folders.bat
cd %CWD%
