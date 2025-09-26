import numpy as np
from course.tests.utils import pretty
from typing import Dict, Any, Tuple

def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
    get_every_other_row = ns["get_every_other_row"]
    reverse_columns = ns["reverse_columns"]
    extract_center_block = ns["extract_center_block"]
    get_3d_slice = ns["get_3d_slice"]

    ok = True
    results = []

    # --- Every other row ---
    test_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    arr = get_every_other_row(test_array)
    checks = [
        (arr.ndim == 2, "every_other_row: 2D array"),
        (arr.shape[0] == 2, "every_other_row: 2 rows"),
        (arr.shape[1] == 4, "every_other_row: 4 columns"),
        (np.array_equal(arr[0], test_array[0]), "every_other_row: first row matches"),
        (np.array_equal(arr[1], test_array[2]), "every_other_row: second row matches row 2"),
    ]
    results.append(("Every other row", checks, pretty(arr)))

    # --- Reverse columns ---
    arr = reverse_columns(test_array)
    checks = [
        (arr.ndim == 2, "reverse_columns: 2D array"),
        (arr.shape == test_array.shape, "reverse_columns: same shape"),
        (np.array_equal(arr[:, 0], test_array[:, -1]), "reverse_columns: first col is last"),
        (np.array_equal(arr[:, -1], test_array[:, 0]), "reverse_columns: last col is first"),
    ]
    results.append(("Reverse columns", checks, pretty(arr)))

    # --- Center block extraction ---
    test_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
    arr = extract_center_block(test_array, 2)
    checks = [
        (arr.ndim == 2, "center_block: 2D array"),
        (arr.shape == (2, 2), "center_block: shape (2, 2)"),
        (arr[0, 0] == 7, "center_block: top-left correct"),
        (arr[0, 1] == 8, "center_block: top-right correct"),
        (arr[1, 0] == 12, "center_block: bottom-left correct"),
        (arr[1, 1] == 13, "center_block: bottom-right correct"),
    ]
    results.append(("Center block extraction", checks, pretty(arr)))

    # --- 3D slicing ---
    test_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
    arr = get_3d_slice(test_3d, 'xy')
    checks = [
        (arr.ndim == 2, "3d_slice: 2D array"),
        (arr.shape == (2, 2), "3d_slice: shape (2, 2)"),
        (np.array_equal(arr, test_3d[1]), "3d_slice: xy plane correct"),
    ]
    results.append(("3D slicing (xy plane)", checks, pretty(arr)))

    # ---- reporting ----
    report_lines = ["Section 2 tests:"]
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
