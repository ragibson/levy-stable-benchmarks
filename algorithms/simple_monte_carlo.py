from bisect import bisect
from functools import lru_cache
from numpy import arctan, tan, sin, cos, pi, log
from numpy.random import uniform, exponential

U = uniform(-pi / 2, pi / 2, size=10 ** 6)
W = exponential(size=10 ** 6)


@lru_cache(maxsize=25)
def sorted_levy_stable_rvs(alpha, beta):
    zeta = -beta * tan(pi * alpha / 2)
    xi = arctan(-zeta) / alpha if alpha != 1 else pi / 2

    if alpha == 1:
        rvs = ((pi / 2 + beta * U) * tan(U) - beta * log((pi * W * cos(U) / 2) / (pi / 2 + beta * U))) / xi
    else:
        rvs = (1 + zeta ** 2) ** (1 / (2 * alpha)) * sin(alpha * (U + xi)) / cos(U) ** (1 / alpha) * \
              (cos(U - alpha * (U + xi)) / W) ** ((1 - alpha) / alpha)

    rvs += zeta
    rvs.sort()
    return rvs


def pdf(x, alpha, beta):
    # TODO: is there a good way to do this?
    return cdf(x + 0.5, alpha, beta) - cdf(x - 0.5, alpha, beta)


def cdf(x, alpha, beta):
    rvs = sorted_levy_stable_rvs(alpha, beta)
    return bisect(rvs, x) / len(rvs)