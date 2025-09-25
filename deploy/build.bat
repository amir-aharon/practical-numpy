@echo off
echo 🚀 Practical NumPy Executable Builder
echo ====================================

echo.
echo 🔍 Checking Python installation...
python --version
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo.
echo 🔨 Building executable...
python deploy/build_executable.py

echo.
echo ✅ Build process complete!
pause
