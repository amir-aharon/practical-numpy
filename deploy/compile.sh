#!/bin/bash

echo "🔨 Building Practical NumPy Executable..."
echo "=========================================="

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.spec

# Create the executable
echo "📦 Creating executable..."
pyinstaller --onefile \
  --name "PracticalNumPy" \
  --add-data "challenges/practical_numpy_01.ipynb:challenges" \
  --add-data "tests:tests" \
  --hidden-import "jupyter" \
  --hidden-import "jupyter.notebook" \
  --hidden-import "jupyter.notebook.notebookapp" \
  --hidden-import "numpy" \
  --hidden-import "IPython" \
  --hidden-import "tornado" \
  --hidden-import "tornado.web" \
  --hidden-import "tornado.ioloop" \
  --hidden-import "tornado.httpserver" \
  --hidden-import "zmq" \
  --console \
  ./deploy/deploy.py

echo "✅ Build complete!"
echo "📁 Executable location: dist/PracticalNumPy.exe (Windows) or dist/PracticalNumPy (Linux/Mac)"
echo ""
echo "🚀 To run: ./dist/PracticalNumPy"
