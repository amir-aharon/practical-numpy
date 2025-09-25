#!/usr/bin/env python3
"""
Build script for Practical NumPy executable
This script handles the complete build process including dependency checking
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path

def check_dependencies():
    """Check if all required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    required_packages = ['pyinstaller', 'jupyter', 'numpy']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package}")
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        
        for package in missing_packages:
            try:
                # Try system python3 first, then fallback to sys.executable
                python_cmd = 'python3' if os.path.exists('/usr/bin/python3') else sys.executable
                subprocess.run([python_cmd, '-m', 'pip', 'install', package], 
                             check=True, capture_output=True)
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to install {package}: {e}")
                print(f"   Try installing manually: {python_cmd} -m pip install {package}")
                return False
    
    return True

def clean_build():
    """Clean previous build artifacts"""
    print("🧹 Cleaning previous builds...")
    
    dirs_to_clean = ['build', 'dist', '__pycache__']
    files_to_clean = ['*.spec']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"🗑️  Removed {dir_name}/")
    
    # Clean .spec files
    for spec_file in Path('.').glob('*.spec'):
        spec_file.unlink()
        print(f"🗑️  Removed {spec_file}")

def build_executable():
    print("📦 Building executable...")

    code_dir = Path("code")
    if not code_dir.exists():
        print(f"❌ Error: {code_dir} not found!")
        return False

    sep = ';' if os.name == 'nt' else ':'
    cmd = [
        'pyinstaller',
        '--onefile',
        '--name', 'PracticalNumPy',
        '--add-data', f'code{sep}code',
        '--hidden-import', 'jupyter',
        '--hidden-import', 'IPython',
        '--hidden-import', 'tornado',
        '--hidden-import', 'zmq',
        '--console',
        './deploy/deploy.py'
    ]


    try:
        subprocess.run(cmd, check=True, text=True)  # let output stream for easier debug
        print("✅ Build successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False


def main():
    print("🚀 Practical NumPy Executable Builder")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        print("❌ Dependency check failed. Please install missing packages manually.")
        sys.exit(1)
    
    # Clean previous builds
    clean_build()
    
    # Build executable
    if build_executable():
        print("\n🎉 Build completed successfully!")
        print("📁 Executable location: dist/PracticalNumPy.exe (Windows) or dist/PracticalNumPy (Linux/Mac)")
        print("\n🚀 To run the course:")
        if os.name == 'nt':  # Windows
            print("   dist\\PracticalNumPy.exe")
        else:  # Linux/Mac
            print("   ./dist/PracticalNumPy")
    else:
        print("\n❌ Build failed. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
