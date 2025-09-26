import numpy as np
from course.tests.utils import pretty
from typing import Dict, Any, Tuple

def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
    make_eye4 = ns["make_eye4"]
    make_band_main_and_upper = ns["make_band_main_and_upper"]
    make_tril_mask5_exclusive = ns["make_tril_mask5_exclusive"]

    ok = True
    results = []

    # --- Identity 4x4 ---
    arr = make_eye4()
    checks = [
        (arr.shape == (4,4), "eye4: shape (4,4)"),
        (arr.dtype in [np.int32, np.int64, np.float32, np.float64], "eye4: numeric dtype"),
        (np.all(np.diag(arr) == 1), "eye4: diagonal is 1"),
        (np.count_nonzero(arr) == 4, "eye4: exactly 4 non-zero elements"),
    ]
    results.append(("Identity 4x4", checks, pretty(arr)))

    # --- Banded (main=1, upper=3) ---
    arr = make_band_main_and_upper()
    checks = [
        (arr.shape == (4,4), "band: shape (4,4)"),
        (arr.dtype in [np.int32, np.int64, np.float32, np.float64], "band: numeric dtype"),
        (np.all(np.diag(arr) == 1), "band: main diagonal is 1"),
        (np.all(np.diag(arr, k=1) == 3), "band: upper diagonal is 3"),
        (np.count_nonzero(arr) == 7, "band: exactly 7 non-zero elements"),
    ]
    results.append(("Banded (main=1, upper=3)", checks, pretty(arr)))

    # --- Strict lower-triangular mask ---
    arr = make_tril_mask5_exclusive()
    checks = [
        (arr.shape == (5,5), "tril: shape (5,5)"),
        (arr.dtype == bool, "tril: boolean dtype"),
        (arr[0,0] == False, "tril: (0,0) is False (on diagonal)"),
        (arr[1,0] == True, "tril: (1,0) is True (below diagonal)"),
        (arr[0,1] == False, "tril: (0,1) is False (above diagonal)"),
    ]
    results.append(("Strict lower-triangular mask", checks, pretty(arr)))

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
