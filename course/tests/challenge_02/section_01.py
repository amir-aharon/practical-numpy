import numpy as np
from course.tests.utils import format_output
from typing import Dict, Any, Tuple

def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
    get_item_rc = ns["get_item_rc"]
    get_first_row_last_col = ns["get_first_row_last_col"]
    set_border_zeros = ns["set_border_zeros"]
    corners = ns["corners"]

    ok = True
    results = []

    # --- Single item by row/col ---
    a = np.arange(9).reshape(3,3)
    val = get_item_rc(a, 1, 2)  # expect element at row=1,col=2 = 5
    checks = [
        (np.isscalar(val), "get_item_rc: returns a scalar"),
        (val == 5, "get_item_rc: correct value (a[1,2]=5)"),
    ]
    results.append(("Single item by row/col", checks, val))

    # --- First row & last column ---
    a = np.arange(12).reshape(3,4)
    row0, col_last = get_first_row_last_col(a)
    checks = [
        (row0.shape == (4,), "first_row_last_col: row0 shape (4,)"),
        (np.array_equal(row0, a[0]), "first_row_last_col: row0 matches"),
        (col_last.shape == (3,), "first_row_last_col: col_last shape (3,)"),
        (np.array_equal(col_last, a[:, -1]), "first_row_last_col: col_last matches"),
    ]
    # pack both row0 & col_last into string for output
    results.append(("First row and last column", checks, f"row0={row0}, col_last={col_last}"))

    # --- Border zeros ---
    a = np.arange(25).reshape(5,5).copy()
    out = set_border_zeros(a)
    checks = [
        (out is a, "set_border_zeros: modifies in place"),
        (np.all(out[0] == 0), "set_border_zeros: top row zeros"),
        (np.all(out[-1] == 0), "set_border_zeros: bottom row zeros"),
        (np.all(out[:,0] == 0), "set_border_zeros: left col zeros"),
        (np.all(out[:,-1] == 0), "set_border_zeros: right col zeros"),
    ]
    results.append(("Set border to zeros", checks, out))

    # --- Corners ---
    a = np.arange(1,10).reshape(3,3)
    out = corners(a)
    checks = [
        (out.shape == (4,), "corners: shape (4,)"),
        (np.array_equal(out, [1,3,7,9]), "corners: matches [top-left,top-right,bottom-left,bottom-right]"),
    ]
    results.append(("Extract corners", checks, out))

    # ---- reporting ----
    report_lines = ["Section 2.1 tests:"]
    for title, checks, arr in results:
        report_lines.append(f"\n--- {title} ---")
        for good, name in checks:
            mark = "✅" if good else "❌"
            report_lines.append(f"{mark} {name}")
            ok &= bool(good)
        report_lines.append("Output:")
        report_lines.append(str(arr))

    report = "\n".join(report_lines)
    return ok, report
