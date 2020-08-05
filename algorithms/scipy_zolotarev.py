# see https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html
# this uses scipy's "zolotarev" method

from numpy import tan, pi
from scipy.stats import levy_stable

levy_stable.pdf_default_method = "zolotarev"


def pdf(x, alpha, beta):
    x += beta * tan(pi * alpha / 2)
    return levy_stable.pdf(x, alpha, beta)


def cdf(x, alpha, beta):
    # cdf computation is the same as the "best" method
    x += beta * tan(pi * alpha / 2)
    return levy_stable.cdf(x, alpha, beta)
