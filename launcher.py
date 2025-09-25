import sys
import shutil
import subprocess
import json
from pathlib import Path


def resource_path(relative_path: str) -> Path:
    """
    Resolve a path that works both in dev mode and in a PyInstaller bundle.
    """
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    return base / relative_path


def ensure_resources(storage_dir: Path):
    """
    Copy everything from bundled code/ into storage_dir.
    """
    storage_dir.mkdir(parents=True, exist_ok=True)
    code_src = resource_path("code")
    for item in code_src.rglob("*"):
        rel_path = item.relative_to(code_src)
        dst = storage_dir / rel_path
        if item.is_file() and not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(item, dst)


def ensure_kernel():
    """
    Write a minimal kernel spec that points to the bundled Python.
    """
    kernel_dir = Path.home() / ".local/share/jupyter/kernels/practical-numpy"
    kernel_dir.mkdir(parents=True, exist_ok=True)

    spec = {
        "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
        "display_name": "Practical NumPy",
        "language": "python",
    }

    with open(kernel_dir / "kernel.json", "w") as f:
        json.dump(spec, f, indent=2)


def main():
    storage_dir = Path.home() / "PracticalNumPy_Notebooks"

    # copy notebooks + tests
    ensure_resources(storage_dir)

    # make sure kernel exists
    ensure_kernel()

    # find first notebook
    notebooks = sorted(storage_dir.glob("*.ipynb"))
    default_nb = notebooks[0].name if notebooks else ""

    # launch Jupyter
    cmd = [
        "jupyter", "notebook",
        "--notebook-dir", str(storage_dir),
    ]
    if default_nb:
        cmd.append(f"--NotebookApp.default_url=/notebooks/{default_nb}")

    subprocess.run(cmd)


if __name__ == "__main__":
    main()
