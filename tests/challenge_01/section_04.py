import numpy as np
from tests.utils import pretty

def run_all(ns):
    make_reshape_c_order = ns["make_reshape_c_order"]
    make_reshape_f_order = ns["make_reshape_f_order"]
    make_frombuffer_uint8 = ns["make_frombuffer_uint8"]

    ok = True
    results = []

    # --- C-order reshape ---
    out = make_reshape_c_order()
    checks = [
        (out.shape == (2,3), "C-order: shape (2,3)"),
        (out.flags["C_CONTIGUOUS"], "C-order: C-contiguous"),
        (np.array_equal(out, [[0,1,2],[3,4,5]]), "C-order: row layout matches"),
    ]
    results.append(("C-order reshape (0..5 → 2x3)", checks, pretty(out)))

    # --- Fortran-order reshape ---
    out = make_reshape_f_order()
    checks = [
        (out.shape == (2,3), "F-order: shape (2,3)"),
        (out.flags["F_CONTIGUOUS"], "F-order: Fortran-contiguous"),
        (np.array_equal(out, [[1,3,5],[2,4,6]]), "F-order: column layout matches"),
    ]
    results.append(("Fortran-order reshape (1..6 → 2x3)", checks, pretty(out)))

    # --- Frombuffer uint8 ---
    out = make_frombuffer_uint8()
    checks = [
        (out.shape == (4,), "frombuffer: length 4"),
        (out.dtype == np.uint8, "frombuffer: dtype uint8"),
        (np.array_equal(out, [1,2,3,4]), "frombuffer: values [1,2,3,4]"),
    ]
    results.append(("From raw bytes (uint8)", checks, pretty(out)))

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
