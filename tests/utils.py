from typing import Any
import numpy as np

def pretty(a: Any, max_rows: int = 6, max_cols: int = 12, decimals: int = 3) -> np.ndarray:
    """Print arrays in a compact, friendly way (for manual use)."""
    arr = np.array(a)
    with np.printoptions(precision=decimals, suppress=True):
        txt = np.array2string(
            arr,
            max_line_width=100,
            threshold=max_rows * max_cols,
            edgeitems=min(max_rows, max_cols),
        )
    # print(txt)
    return arr

def pretty_bool(a: np.ndarray) -> str:
    """Print boolean arrays with T/F characters (for masks)."""
    output = ""
    chars = {True: "T", False: "F"}
    for row in a:
        # print(" ".join(chars[v] for v in row))
        output += " ".join(chars[v] for v in row) + "\n"
    return output

def format_output(obj: Any) -> str:
    """
    Format any object for test reporting:
    - np.ndarray → full array string (no truncation)
    - others → str(obj)
    """
    if isinstance(obj, np.ndarray):
        return np.array2string(obj, threshold=np.inf)
    return str(obj)
