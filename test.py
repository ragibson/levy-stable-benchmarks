from benchmarks.test_accuracy_against_table import test_accuracy_against_table
from benchmarks.import_stable_tables import import_nolan_quantiles, import_stable_tables
from time import time


def test(pdf, cdf, tol):
    tables = [import_stable_tables("data/cdf_table.dat"),
              import_stable_tables("data/quantile_table.dat", expect_quantiles=True),
              import_nolan_quantiles(),
              import_stable_tables("data/pdf_table.dat")]
    descriptions = ["CDF table", "Quantile table", "Nolan quantiles", "PDF table"]
    funcs = [cdf, cdf, cdf, pdf]

    for table, description, func in zip(tables, descriptions, funcs):
        start_time = time()
        acc = test_accuracy_against_table(func, table, tol=tol, show_progress=True)
        duration = time() - start_time
        per_call = duration / len(table)
        print(f"{description} accuracy: {100 * acc}% in {duration:.1f} s")
        print(f"Avg duration: "
              f"{per_call / 1e-6 if per_call < 1e-3 else per_call / 1e-3 if per_call < 1 else per_call:.2f} "
              f"{'us' if per_call < 1e-3 else 'ms' if per_call < 1 else 's'}")
