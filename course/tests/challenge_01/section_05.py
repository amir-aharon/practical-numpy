import numpy as np
from course.tests.utils import pretty
from typing import Dict, Any, Tuple

def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
    make_vstack_rows_2x3 = ns["make_vstack_rows_2x3"]
    make_hstack_cols_3x2 = ns["make_hstack_cols_3x2"]
    make_stack_depth_2x2x2 = ns["make_stack_depth_2x2x2"]
    make_split_1d_5_equal = ns["make_split_1d_5_equal"]

    ok = True
    results = []

    # --- Vertical stack rows ---
    arr = make_vstack_rows_2x3()
    checks = [
        (arr.ndim == 2, "vstack: 2D array"),
        (arr.shape == (2, 3), "vstack: shape (2,3)"),
        (np.array_equal(arr[0], [1, 2, 3]), "vstack: first row [1,2,3]"),
        (np.array_equal(arr[1], [4, 5, 6]), "vstack: second row [4,5,6]"),
    ]
    results.append(("Vertical stack (rows)", checks, pretty(arr)))

    # --- Horizontal stack columns ---
    arr = make_hstack_cols_3x2()
    checks = [
        (arr.ndim == 2, "hstack: 2D array"),
        (arr.shape == (3, 2), "hstack: shape (3,2)"),
        (np.array_equal(arr[:, 0], [1, 2, 3]), "hstack: first column [1,2,3]"),
        (np.array_equal(arr[:, 1], [10, 20, 30]), "hstack: second column [10,20,30]"),
    ]
    results.append(("Horizontal stack (columns)", checks, pretty(arr)))

    # --- Stack along depth ---
    arr = make_stack_depth_2x2x2()
    checks = [
        (arr.ndim == 3, "depth: 3D array"),
        (arr.shape == (2, 2, 2), "depth: shape (2,2,2)"),
        (np.array_equal(arr[:, :, 0], [[1, 0], [0, 1]]), "depth: first slice is identity"),
        (np.array_equal(arr[:, :, 1], [[2, 2], [2, 2]]), "depth: second slice is all 2s"),
    ]
    results.append(("Stack along depth", checks, pretty(arr)))

    # --- Split 1D into 5 equal parts ---
    parts = make_split_1d_5_equal()
    checks = [
        (isinstance(parts, tuple), "split: returns tuple"),
        (len(parts) == 5, "split: 5 chunks"),
        (all(p.ndim == 1 for p in parts), "split: all 1D arrays"),
        (all(p.size == 4 for p in parts), "split: each chunk size 4"),
        (np.array_equal(parts[0], [0, 1, 2, 3]), "split: first chunk [0,1,2,3]"),
        (np.array_equal(parts[1], [4, 5, 6, 7]), "split: second chunk [4,5,6,7]"),
        (np.array_equal(parts[4], [16, 17, 18, 19]), "split: last chunk [16,17,18,19]"),
    ]
    results.append(("Split 1D into 5 equal parts", checks, parts))

    # ---- reporting ----
    report_lines = ["Section 5 tests:"]
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
