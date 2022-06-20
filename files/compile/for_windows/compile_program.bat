@REM The script in charge of compiling thz program into a windows executable
echo off
color 0A
cls
set CWD="%CD%"
set DEST="..\.."
set BIN_NAME="makator.exe"
set FILES="makefile_creator.py get.py my_databases.py"
set ICON_PATH="icon/cog.ico"
set ARGS=""
echo "1"
if %1!="" set BIN_NAME=%1
echo "2"
cd %DEST%
echo "Checking for old binaries..."
if exist "%DEST%\%OUTPUT_name%". (
    echo "Deleting old binaries...".
    del "%DEST%\%OUTPUT_name%".
)
echo "Old binaries deleted."
echo "Compiling..."
pyinstaller makefile_creator.py get.py my_databases.py -n %BIN_NAME% -i %ICON_PATH% --onefile
echo "Compilation finished."
echo "Fecthing the binary..."
copy "dist\%BIN_NAME%" "%BIN_NAME%"
echo "Removing unnecessary files..."
del %BIN_NAME%.spec
echo "%BIN_NAME%.spec removed. "
rmdir /S /Q "dist"
echo "Removed the dist folder"
rmdir /S /Q "build"
echo "Removed the build folder"
echo "Unnecessary files removed."
cd %CWD%
