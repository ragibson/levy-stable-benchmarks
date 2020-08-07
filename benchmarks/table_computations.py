from math import isclose
from multiprocessing import Pool
from tqdm import tqdm

_ASSUMED_TABLE_ACCURACY = 1e-10


def test_accuracy_against_table(f, table, tol, absolute_tolerance=False, show_progress=False):
    abs_tol = tol if absolute_tolerance else _ASSUMED_TABLE_ACCURACY

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
