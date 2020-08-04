from bisect import bisect
from functools import lru_cache
from scipy.stats import levy_stable


@lru_cache(maxsize=None)
def sorted_levy_stable_rvs(alpha, beta, size=10 ** 4):
    # TODO: use method of https://en.wikipedia.org/wiki/Stable_distribution#Simulation_of_stable_variables directly
    rvs = levy_stable.rvs(alpha=alpha, beta=beta, size=size)
    return sorted(rvs.tolist())


def pdf(x, alpha, beta):
    raise NotImplementedError("pdf is not implemented")


def cdf(x, alpha, beta):
    rvs = sorted_levy_stable_rvs(alpha, beta)
    return bisect(rvs, x) / len(rvs)
