# see https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html
# this uses scipy's "best" method (which is the default)

from numpy import tan, pi
from scipy.stats import levy_stable


def pdf(x, alpha, beta):
    levy_stable.pdf_default_method = "best"
    x += beta * tan(pi * alpha / 2)
    return levy_stable.pdf(x, alpha, beta)


def cdf(x, alpha, beta):
    x += beta * tan(pi * alpha / 2)
    return levy_stable.cdf(x, alpha, beta)
