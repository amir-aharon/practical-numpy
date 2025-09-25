APP_NAME=launcher
SPEC_FILE=launcher.spec

.PHONY: build run clean dev

# Build executable with PyInstaller
build:
	pyinstaller $(SPEC_FILE)

# Run the frozen app
run: build
	./dist/$(APP_NAME)

# Run directly with Python (dev mode)
dev:
	python launcher.py

# Clean build artifacts
clean:
	rm -rf build dist __pycache__ *.spec
