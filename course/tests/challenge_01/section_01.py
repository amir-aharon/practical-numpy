import numpy as np
from course.tests.utils import pretty
from typing import Dict, Any, Tuple

def run_all(ns: Dict[str, Any]) -> Tuple[bool, str]:
    make_odds_10_to_30 = ns["make_odds_10_to_30"]
    make_linspace_unit_interval_101 = ns["make_linspace_unit_interval_101"]
    make_logspace_decades_0_to_3 = ns["make_logspace_decades_0_to_3"]

    ok = True
    results = []

    # --- Odds ---
    arr = make_odds_10_to_30()
    checks = [
        (arr.ndim == 1, "odds: 1D array"),
        (arr.size == 10, "odds: size 10"),
        (arr[0] == 11 and arr[-1] == 29, "odds: first=11, last=29"),
        (np.all(arr % 2 == 1), "odds: all odd"),
    ]
    results.append(("Odds 11..29", checks, pretty(arr)))

    # --- Linspace ---
    x = make_linspace_unit_interval_101()
    checks = [
        (x.shape == (101,), "linspace: length 101"),
        (x.dtype == np.float32, "linspace: dtype float32"),
        (np.isclose(x[0], 0.0) and np.isclose(x[-1], 1.0), "linspace: endpoints 0 and 1"),
    ]
    results.append(("Linspace 0..1 (101 pts)", checks, pretty(x)))

    # --- Logspace ---
    y = make_logspace_decades_0_to_3()
    checks = [
        (y.shape == (4,), "logspace: length 4"),
        (y.dtype == np.float64, "logspace: dtype float64"),
        (np.isclose(y[0], 1.0) and np.isclose(y[-1], 1000.0), "logspace: endpoints 1 and 1000"),
    ]
    results.append(("Logspace 10^0..10^3", checks, pretty(y)))

    # ---- reporting ----
    report_lines = ["Section 1 tests:"]
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
