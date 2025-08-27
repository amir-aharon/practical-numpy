import numpy as np
from tests.utils import pretty, pretty_bool

def run_all(ns):
    make_eye4 = ns["make_eye4"]
    make_band_main_and_upper = ns["make_band_main_and_upper"]
    make_tril_mask5_exclusive = ns["make_tril_mask5_exclusive"]

    ok = True
    results = []

    # --- Identity 4x4 ---
    eye4 = make_eye4()
    checks = [
        (eye4.shape == (4,4), "eye4: shape (4,4)"),
        (np.all(eye4.diagonal() == 1), "eye4: diagonal ones"),
        (np.count_nonzero(eye4) == 4, "eye4: only 4 ones"),
    ]
    results.append(("Identity matrix (4x4)", checks, pretty(eye4)))

    # --- Banded matrix (main=1, upper=3) ---
    band = make_band_main_and_upper()
    i, j = np.indices((4,4))
    main = (i == j)
    upper = (j == i + 1)
    other = ~(main | upper)
    checks = [
        (band.shape == (4,4), "band: shape (4,4)"),
        (np.all(band[main] == 1), "band: main diag=1"),
        (np.all(band[upper] == 3), "band: upper diag=3"),
        (np.all(band[other] == 0), "band: elsewhere 0"),
    ]
    results.append(("Banded matrix (diag=1, upper=3)", checks, pretty(band)))

    # --- Strict lower-tri mask (5x5) ---
    mask = make_tril_mask5_exclusive()
    i5, j5 = np.indices((5,5))
    checks = [
        (mask.shape == (5,5) and mask.dtype == bool, "mask: shape (5,5), dtype=bool"),
        (np.all(mask[i5 <= j5] == False), "mask: diag+above False"),
        (np.all(mask[i5 > j5] == True), "mask: below True"),
    ]
    # special: boolean pretty
    results.append(("Strict lower-triangular mask (5x5)", checks, "see below"))
    mask_str = []
    chars = {True: "T", False: "F"}
    for row in mask:
        mask_str.append(" ".join(chars[v] for v in row))

    # ---- reporting ----
    report_lines = ["Section 3 tests:"]
    for idx, (title, checks, arr) in enumerate(results):
        report_lines.append(f"\n--- {title} ---")
        for good, name in checks:
            mark = "✅" if good else "❌"
            report_lines.append(f"{mark} {name}")
            ok &= bool(good)
        report_lines.append("Output:")
        if idx == 2:  # mask case
            report_lines.extend(mask_str)
        else:
            report_lines.append(str(arr))

    report = "\n".join(report_lines)
    return ok, report
