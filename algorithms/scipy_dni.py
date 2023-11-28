# see https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html
# this uses scipy's "dni" method

from numpy import tan, pi
from scipy.stats import levy_stable


def pdf(x, alpha, beta):
    levy_stable.pdf_default_method = "dni"
    if alpha != 1:
        x += beta * tan(pi * alpha / 2)
    return levy_stable.pdf(x, alpha, beta)


def cdf(x, alpha, beta):
    raise NotImplementedError("Setting pdf_default_method does not affect CDF calculation. "
                              "Use scipy_piecewise instead.")
