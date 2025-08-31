import numpy as np
from tests.utils import pretty
from typing import Dict, Any, Tuple

def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
    make_stack_horizontal = ns["make_stack_horizontal"]
    make_stack_vertical = ns["make_stack_vertical"]
    make_split_2_equal = ns["make_split_2_equal"]
    make_split_3_parts = ns["make_split_3_parts"]

    ok = True
    results = []

    # --- Horizontal stack ---
    arr = make_stack_horizontal()
    checks = [
        (arr.ndim == 2, "stack_h: 2D array"),
        (arr.shape == (2, 4), "stack_h: shape (2,4)"),
        (np.array_equal(arr[:, :2], [[1, 2], [3, 4]]), "stack_h: left half correct"),
        (np.array_equal(arr[:, 2:], [[5, 6], [7, 8]]), "stack_h: right half correct"),
    ]
    results.append(("Horizontal stack", checks, pretty(arr)))

    # --- Vertical stack ---
    arr = make_stack_vertical()
    checks = [
        (arr.ndim == 2, "stack_v: 2D array"),
        (arr.shape == (4, 2), "stack_v: shape (4,2)"),
        (np.array_equal(arr[:2], [[1, 2], [3, 4]]), "stack_v: top half correct"),
        (np.array_equal(arr[2:], [[5, 6], [7, 8]]), "stack_v: bottom half correct"),
    ]
    results.append(("Vertical stack", checks, pretty(arr)))

    # --- Split into 2 equal parts ---
    arr = make_split_2_equal()
    checks = [
        (len(arr) == 2, "split_2: 2 arrays"),
        (arr[0].shape == (2, 2), "split_2: first array shape (2,2)"),
        (arr[1].shape == (2, 2), "split_2: second array shape (2,2)"),
        (np.array_equal(arr[0], [[1, 2], [3, 4]]), "split_2: first array correct"),
        (np.array_equal(arr[1], [[5, 6], [7, 8]]), "split_2: second array correct"),
    ]
    results.append(("Split into 2 equal parts", checks, arr))

    # --- Split into 3 parts ---
    arr = make_split_3_parts()
    checks = [
        (len(arr) == 3, "split_3: 3 arrays"),
        (arr[0].shape == (1, 2), "split_3: first array shape (1,2)"),
        (arr[1].shape == (1, 2), "split_3: second array shape (1,2)"),
        (arr[2].shape == (1, 2), "split_3: third array shape (1,2)"),
        (np.array_equal(arr[0], [[1, 2]]), "split_3: first array correct"),
        (np.array_equal(arr[1], [[3, 4]]), "split_3: second array correct"),
        (np.array_equal(arr[2], [[5, 6]]), "split_3: third array correct"),
    ]
    results.append(("Split into 3 parts", checks, arr))

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
