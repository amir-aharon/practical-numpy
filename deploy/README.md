# Practical NumPy Executable Deployment

This folder contains scripts to build a standalone executable for the Practical NumPy course.

## 🚀 Quick Start

### Option 1: Automated Build (Recommended)

**Windows:**
```cmd
deploy\build.bat
```

**Linux/Mac:**
```bash
python3 deploy/build_executable.py
```

### Option 2: Manual Build

1. **Install Dependencies:**
   ```bash
   pip install pyinstaller jupyter numpy
   ```

2. **Run Build Script:**
   ```bash
   ./deploy/compile.sh
   ```

3. **Run Executable:**
   - Windows: `dist\PracticalNumPy.exe`
   - Linux/Mac: `./dist/PracticalNumPy`

## 📁 Files

- `deploy.py` - Main launcher script that starts Jupyter with the notebook
- `build_executable.py` - Automated build script with dependency checking
- `compile.sh` - Manual build script using PyInstaller
- `build.bat` - Windows batch file for easy building
- `format.sh` - Cleans notebook metadata and output

## 🔧 Requirements

- Python 3.7+
- pip
- Internet connection (for dependency installation)

## 📦 What Gets Bundled

- `challenges/practical_numpy_01.ipynb` - The main course notebook
- `tests/` - All test files for the course
- All Python dependencies (numpy, jupyter, etc.)

## 🎯 How It Works

1. The executable bundles the notebook and all dependencies
2. When run, it starts a local Jupyter server
3. Automatically opens the notebook in your default browser
4. No need to install Python or any dependencies on the target machine

## 🐛 Troubleshooting

### Build Issues
- Ensure you have Python 3.7+ installed
- Try running in a virtual environment: `python -m venv venv && source venv/bin/activate`
- Check that all files are in the correct locations

### Runtime Issues
- The executable needs to be run from a directory with write permissions
- Firewall might block Jupyter (runs on port 8888)
- Some antivirus software might flag the executable

### Manual Installation
If the executable doesn't work, you can run the course manually:
1. Install Python and Jupyter: `pip install jupyter numpy`
2. Run: `jupyter notebook challenges/practical_numpy_01.ipynb`

## 📝 Notes

- The executable is platform-specific (Windows .exe, Linux binary, etc.)
- File size will be ~100-200MB due to bundled dependencies
- First run might be slower as Jupyter initializes
