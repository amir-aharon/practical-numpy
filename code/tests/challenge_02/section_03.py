import numpy as np
from tests.utils import pretty
from typing import Dict, Any, Tuple

def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
    select_positive_elements = ns["select_positive_elements"]
    mask_above_threshold = ns["mask_above_threshold"]
    select_even_rows_odd_cols = ns["select_even_rows_odd_cols"]
    replace_negative_with_zero = ns["replace_negative_with_zero"]

    ok = True
    results = []

    # --- Select positive elements ---
    test_array = np.array([-3, -1, 0, 2, 4, -5, 6])
    arr = select_positive_elements(test_array)
    checks = [
        (arr.ndim == 1, "positive_elements: 1D array"),
        (arr.size == 3, "positive_elements: 3 positive values"),
        (np.all(arr > 0), "positive_elements: all values positive"),
        (2 in arr and 4 in arr and 6 in arr, "positive_elements: contains expected values"),
    ]
    results.append(("Select positive elements", checks, pretty(arr)))

    # --- Threshold mask ---
    test_array = np.array([[1, 5, 3], [7, 2, 9], [4, 6, 8]])
    mask = mask_above_threshold(test_array, 5)
    checks = [
        (mask.dtype == bool, "threshold_mask: boolean dtype"),
        (mask.shape == test_array.shape, "threshold_mask: same shape"),
        (np.sum(mask) == 4, "threshold_mask: 4 elements above 5"),
        (mask[1, 2] == True, "threshold_mask: 9 is above 5"),
        (mask[0, 0] == False, "threshold_mask: 1 is not above 5"),
    ]
    results.append(("Threshold mask (>5)", checks, pretty(mask)))

    # --- Even rows, odd columns ---
    test_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    arr = select_even_rows_odd_cols(test_array)
    checks = [
        (arr.ndim == 1, "even_odd: 1D array"),
        (arr.size == 2, "even_odd: 2 elements (rows 0,2; cols 1,3)"),
        (2 in arr, "even_odd: contains element from row 0, col 1"),
        (12 in arr, "even_odd: contains element from row 2, col 3"),
    ]
    results.append(("Even rows, odd columns", checks, pretty(arr)))

    # --- Replace negatives with zero ---
    test_array = np.array([[-1, 2, -3], [4, -5, 6]])
    original_id = id(test_array)
    arr = replace_negative_with_zero(test_array)
    checks = [
        (id(arr) == original_id, "replace_negatives: modifies in place"),
        (arr[0, 0] == 0, "replace_negatives: -1 replaced with 0"),
        (arr[0, 2] == 0, "replace_negatives: -3 replaced with 0"),
        (arr[1, 1] == 0, "replace_negatives: -5 replaced with 0"),
        (arr[0, 1] == 2, "replace_negatives: positive values unchanged"),
        (arr[1, 2] == 6, "replace_negatives: positive values unchanged"),
    ]
    results.append(("Replace negatives with zero", checks, pretty(arr)))

    # ---- reporting ----
    report_lines = ["Section 3 tests:"]
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
