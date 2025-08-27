import numpy as np
from tests.utils import pretty

def run_all(ns):
    make_vstack_rows_2x3 = ns["make_vstack_rows_2x3"]
    make_hstack_cols_3x2 = ns["make_hstack_cols_3x2"]
    make_stack_depth_2x2x2 = ns["make_stack_depth_2x2x2"]
    make_split_1d_5_equal = ns["make_split_1d_5_equal"]

    ok = True
    results = []

    # --- Vertical stack (rows) ---
    out = make_vstack_rows_2x3()
    checks = [
        (out.shape == (2,3), "vstack: shape (2,3)"),
        (np.array_equal(out[0], [1,2,3]), "vstack: first row [1,2,3]"),
        (np.array_equal(out[1], [4,5,6]), "vstack: second row [4,5,6]"),
    ]
    results.append(("Vertical stack (rows)", checks, pretty(out)))

    # --- Horizontal stack (columns) ---
    out = make_hstack_cols_3x2()
    checks = [
        (out.shape == (3,2), "hstack: shape (3,2)"),
        (np.array_equal(out[:,0], [1,2,3]), "hstack: first column [1,2,3]"),
        (np.array_equal(out[:,1], [10,20,30]), "hstack: second column [10,20,30]"),
    ]
    results.append(("Horizontal stack (columns)", checks, pretty(out)))

    # --- Stack along depth ---
    out = make_stack_depth_2x2x2()
    A = np.array([[1,0],[0,1]])
    B = np.full((2,2), 2)
    checks = [
        (out.shape == (2,2,2), "depth-stack: shape (2,2,2)"),
        (np.array_equal(out[:,:,0], A), "depth-stack: slice 0 == A"),
        (np.array_equal(out[:,:,1], B), "depth-stack: slice 1 == B"),
    ]
    results.append(("Stack along depth (2x2x2)", checks, pretty(out)))

    # --- Split 1D into 5 equal chunks ---
    chunks = make_split_1d_5_equal()
    checks = [
        (isinstance(chunks, tuple) and len(chunks) == 5, "split: returns tuple of length 5"),
        all(c.shape == (4,) for c in chunks),
        "split: each chunk length 4",
        (np.array_equal(np.concatenate(chunks), np.arange(20)), "split: recombine → 0..19"),
    ]
    # unify checks into consistent style
    checks = [
        (isinstance(chunks, tuple) and len(chunks) == 5, "split: tuple of 5 chunks"),
        (all(c.shape == (4,) for c in chunks), "split: each chunk has length 4"),
        (np.array_equal(np.concatenate(chunks), np.arange(20)), "split: concatenation is 0..19"),
    ]
    results.append(("Split 1D array into 5 equal chunks", checks, str(chunks)))

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
