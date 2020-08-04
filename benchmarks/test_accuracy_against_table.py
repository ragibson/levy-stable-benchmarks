from math import isclose
from tqdm import tqdm


def test_accuracy_against_table(f, table, tol, show_progress=False):
    if show_progress:
        table = tqdm(table)

    num_successes = 0
    for alpha, beta, x, p in table:
        if isclose(p, f(x, alpha=alpha, beta=beta), rel_tol=tol, abs_tol=tol):
            num_successes += 1
    return num_successes / len(table)
