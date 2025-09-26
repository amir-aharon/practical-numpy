import numpy as np
from course.tests.utils import pretty
from typing import Dict, Any, Tuple

def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
    make_zeros_int16_3x2 = ns["make_zeros_int16_3x2"]
    make_full_pi_float32_2x3 = ns["make_full_pi_float32_2x3"]
    make_int8_range_neg5_to_4 = ns["make_int8_range_neg5_to_4"]

    ok = True
    results = []

    # --- Zeros (3x2 int16) ---
    z = make_zeros_int16_3x2()
    checks = [
        (z.shape == (3,2), "zeros: shape (3,2)"),
        (z.dtype == np.int16, "zeros: dtype int16"),
        (np.count_nonzero(z) == 0, "zeros: all 0"),
    ]
    results.append(("Zeros int16 (3x2)", checks, pretty(z)))

    # --- Full of π (2x3 float32) ---
    pi_mat = make_full_pi_float32_2x3()
    checks = [
        (pi_mat.shape == (2,3), "pi: shape (2,3)"),
        (pi_mat.dtype == np.float32, "pi: dtype float32"),
        (np.allclose(pi_mat, np.float32(np.pi)), "pi: values equal π"),
    ]
    results.append(("Full of π float32 (2x3)", checks, pretty(pi_mat)))

    # --- Int8 range -5..4 ---
    r = make_int8_range_neg5_to_4()
    checks = [
        (r.shape == (10,), "range: length 10"),
        (r.dtype == np.int8, "range: dtype int8"),
        (r[0] == -5 and r[-1] == 4, "range: endpoints -5 and 4"),
        (np.all(r[1:] - r[:-1] == 1), "range: consecutive +1"),
    ]
    results.append(("Range -5..4 int8", checks, pretty(r)))

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
