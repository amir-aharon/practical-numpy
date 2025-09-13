import numpy as np
from tests.utils import pretty
from typing import Dict, Any, Tuple

def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
    make_reshape_c_order = ns["make_reshape_c_order"]
    make_reshape_f_order = ns["make_reshape_f_order"]
    make_frombuffer_uint8 = ns["make_frombuffer_uint8"]

    ok = True
    results = []

    # --- C-order reshape ---
    arr = make_reshape_c_order()
    checks = [
        (arr.ndim == 2, "c_order: 2D array"),
        (arr.shape == (2, 3), "c_order: shape (2,3)"),
        (arr.flags.c_contiguous, "c_order: C-contiguous"),
        (arr[0, 0] == 0 and arr[0, 2] == 2, "c_order: first row [0,1,2]"),
        (arr[1, 0] == 3 and arr[1, 2] == 5, "c_order: second row [3,4,5]"),
    ]
    results.append(("C-order reshape", checks, pretty(arr)))

    # --- F-order reshape ---
    arr = make_reshape_f_order()
    checks = [
        (arr.ndim == 2, "f_order: 2D array"),
        (arr.shape == (2, 3), "f_order: shape (2,3)"),
        (arr.flags.f_contiguous, "f_order: F-contiguous"),
        (arr[0, 0] == 1 and arr[1, 0] == 2, "f_order: first column [1,2]"),
        (arr[0, 1] == 3 and arr[1, 1] == 4, "f_order: second column [3,4]"),
        (arr[0, 2] == 5 and arr[1, 2] == 6, "f_order: third column [5,6]"),
    ]
    results.append(("F-order reshape", checks, pretty(arr)))

    # --- From buffer uint8 ---
    arr = make_frombuffer_uint8()
    checks = [
        (arr.ndim == 1, "frombuffer: 1D array"),
        (arr.dtype == np.uint8, "frombuffer: dtype uint8"),
        (arr.size == 4, "frombuffer: size 4"),
        (arr[0] == 1 and arr[1] == 2, "frombuffer: first two values"),
        (arr[2] == 3 and arr[3] == 4, "frombuffer: last two values"),
    ]
    results.append(("From buffer uint8", checks, pretty(arr)))

    # ---- reporting ----
    report_lines = ["Section 4 tests:"]
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
