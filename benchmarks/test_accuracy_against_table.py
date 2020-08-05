from math import isclose
from tqdm import tqdm

_ASSUMED_TABLE_ACCURACY = 1e-10


def test_accuracy_against_table(f, table, tol, show_progress=False):
    if show_progress:
        table = tqdm(table)

    num_successes = 0
    for alpha, beta, x, p in table:
        if isclose(p, f(x, alpha=alpha, beta=beta), rel_tol=tol, abs_tol=_ASSUMED_TABLE_ACCURACY):
            num_successes += 1
    return num_successes / len(table)
