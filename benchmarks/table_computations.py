from benchmarks.import_stable_tables import import_nolan_quantiles, import_stable_tables
from math import isclose
from multiprocessing import Pool
from time import time
from tqdm import tqdm

_ASSUMED_TABLE_ACCURACY = 1e-10


def test_accuracy_against_table(f, table, tol, tol_is_absolute=False, show_progress=False):
    abs_tol = tol if tol_is_absolute else _ASSUMED_TABLE_ACCURACY

    if show_progress:
        table = tqdm(table)

    num_successes = 0
    for alpha, beta, x, p in table:
        if isclose(p, f(x, alpha=alpha, beta=beta), rel_tol=tol, abs_tol=abs_tol):
            num_successes += 1
    return num_successes / len(table)


def precompute_table(f, table, show_progress=False, single_threaded=False):
    precomputed_table = {}

    if single_threaded:
        if show_progress:
            table = tqdm(table)

        for alpha, beta, x, p in table:
            precomputed_table[(x, alpha, beta)] = f(x, alpha, beta)
    else:
        args = [(x, alpha, beta) for alpha, beta, x, p in table]
        if show_progress:
            args = tqdm(args)

        with Pool() as pool:
            results = pool.starmap(f, args)

            for arg, result in zip(args, results):
                precomputed_table[arg] = result

    return precomputed_table


def test_all_accuracies(pdf, cdf, tol, tol_is_absolute=False, show_progress=False):
    cdf_tables = [import_stable_tables("data/cdf_table.dat"),
                  import_stable_tables("data/cdf_quantile_table.dat", expect_quantiles=True),
                  import_nolan_quantiles()]
    pdf_tables = [import_stable_tables("data/pdf_table.dat"),
                  import_stable_tables("data/pdf_quantile_table.dat", single_queries=True,
                                       num_values_expected=len(cdf_tables[1])),
                  import_stable_tables("data/nolan_pdf_quantile.dat", single_queries=True,
                                       num_values_expected=len(cdf_tables[2]))]
    tables = cdf_tables + pdf_tables
    descriptions = ["CDF table", "CDF quantile table", "Nolan CDF quantiles",
                    "PDF table", "PDF quantile table", "Nolan PDF quantiles"]
    funcs = [cdf, cdf, cdf, pdf, pdf, pdf]

    for table, description, func in zip(tables, descriptions, funcs):
        start_time = time()
        acc = test_accuracy_against_table(func, table, tol=tol, tol_is_absolute=tol_is_absolute,
                                          show_progress=show_progress)
        duration = time() - start_time
        per_call = duration / len(table)
        print(f"{description} accuracy: {100 * acc}% in {duration:.1f} s")
        print(f"Avg duration: "
              f"{per_call / 1e-6 if per_call < 1e-3 else per_call / 1e-3 if per_call < 1 else per_call:.2f} "
              f"{'us' if per_call < 1e-3 else 'ms' if per_call < 1 else 's'}")
