# see https://github.com/josemiotto/pylevy
from levy import levy


def pdf(x, alpha, beta):
    return levy(x, alpha=alpha, beta=beta, cdf=False)


def cdf(x, alpha, beta):
    return levy(x, alpha=alpha, beta=beta, cdf=True)
