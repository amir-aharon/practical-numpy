import numpy as np

def pretty(a, max_rows=6, max_cols=12, decimals=3):
    """Print arrays in a compact, friendly way."""
    arr = np.array(a)
    with np.printoptions(precision=decimals, suppress=True):
        txt = np.array2string(
            arr,
            max_line_width=100,
            threshold=max_rows * max_cols,
            edgeitems=min(max_rows, max_cols),
        )
    return txt

def pretty_bool(a):
    """Print boolean arrays with T/F characters."""
    chars = {True: "T", False: "F"}
    res = ''
    for row in a:
        res += " ".join(chars[v] for v in row) + '\n'
    return res
