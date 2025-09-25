import os
import sys
import subprocess
from pathlib import Path

def main():
    # Resolve the base directory (PyInstaller temp dir or local dev path)
    BASE = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    CODE_DIR = BASE / "code"
    TESTS_DIR = CODE_DIR / "tests"

    # Make sure cwd is the code/ directory so Jupyter shows all notebooks
    os.chdir(CODE_DIR)

    # Extend PYTHONPATH so that `import tests` works in notebooks
    path_sep = ';' if os.name == 'nt' else ':'
    extra_paths = [str(CODE_DIR), str(TESTS_DIR)]
    env = os.environ.copy()
    env["PYTHONPATH"] = (
        (env.get("PYTHONPATH", "") + (path_sep if env.get("PYTHONPATH") else "")) + path_sep.join(extra_paths)
    )

    # Launch Jupyter notebook server rooted at code/
    cmd = [
        "jupyter", "notebook",
        "--notebook-dir", str(CODE_DIR)
    ]
    subprocess.run(cmd, env=env)

if __name__ == "__main__":
    main()
