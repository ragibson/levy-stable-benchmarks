# see https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html
# this uses scipy's "best" method

from scipy.stats import levy_stable


# this is the default method for scipy
# levy_stable.pdf_default_method = "best"

def pdf(x, alpha, beta):
    return levy_stable.pdf(x, alpha, beta)


def cdf(x, alpha, beta):
    return levy_stable.cdf(x, alpha, beta)
