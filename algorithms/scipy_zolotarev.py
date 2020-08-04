# see https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html
# this uses scipy's "zolotarev" method

from scipy.stats import levy_stable

levy_stable.pdf_default_method = "zolotarev"


def pdf(x, alpha, beta):
    return levy_stable.pdf(x, alpha, beta)


def cdf(x, alpha, beta):
    # cdf computation is the same as the "best" method
    return levy_stable.cdf(x, alpha, beta)
