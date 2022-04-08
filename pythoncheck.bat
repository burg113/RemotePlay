::check if python and pip are installed

@echo off

python --version >NUL
if errorlevel 1 (
	echo no python install found
) else (
	echo python is installed
)

pip --version >NUL
if errorlevel 1 (
	echo no pip install found
) else (
	echo pip is installed
)

echo Press any key to exit...
pause >NUL