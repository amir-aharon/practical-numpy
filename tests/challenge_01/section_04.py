import numpy as np
from tests.utils import pretty
from typing import Dict, Any, Tuple

def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
    make_reshape_2d_to_1d = ns["make_reshape_2d_to_1d"]
    make_reshape_1d_to_3d = ns["make_reshape_1d_to_3d"]
    make_transpose_2x3 = ns["make_transpose_2x3"]

    ok = True
    results = []

    # --- 2D to 1D reshape ---
    arr = make_reshape_2d_to_1d()
    checks = [
        (arr.ndim == 1, "reshape_2d_to_1d: 1D array"),
        (arr.size == 12, "reshape_2d_to_1d: size 12"),
        (arr[0] == 0 and arr[-1] == 11, "reshape_2d_to_1d: first=0, last=11"),
    ]
    results.append(("2D to 1D reshape", checks, pretty(arr)))

    # --- 1D to 3D reshape ---
    arr = make_reshape_1d_to_3d()
    checks = [
        (arr.ndim == 3, "reshape_1d_to_3d: 3D array"),
        (arr.shape == (2, 3, 2), "reshape_1d_to_3d: shape (2,3,2)"),
        (arr[0, 0, 0] == 0 and arr[-1, -1, -1] == 11, "reshape_1d_to_3d: first=0, last=11"),
    ]
    results.append(("1D to 3D reshape", checks, pretty(arr)))

    # --- Transpose 2x3 ---
    arr = make_transpose_2x3()
    checks = [
        (arr.ndim == 2, "transpose_2x3: 2D array"),
        (arr.shape == (3, 2), "transpose_2x3: shape (3,2)"),
        (arr[0, 0] == 0 and arr[2, 1] == 5, "transpose_2x3: correct values"),
    ]
    results.append(("Transpose 2x3", checks, pretty(arr)))

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
