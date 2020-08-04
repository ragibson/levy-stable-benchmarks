from scipy.integrate import quad
from numpy import exp, abs, inf, pi, cos, tan, log


def pdf(x, alpha, beta, tol=1e-8, limit=10 ** 3):
    if beta == 0.0:
        res, error = quad(lambda t: exp(-abs(t) ** alpha), 0, inf, epsabs=tol, limit=limit,
                          weight="cos", wvar=x)
        return res / pi
    elif alpha == 1.0:
        phi_constant = -2 * beta / pi

        def f_int(t):
            u = abs(t) ** alpha
            return exp(-u) * cos(u * phi_constant * log(abs(t)) - x * t)
    else:
        phi_constant = beta * tan(pi * alpha / 2)

        def f_int(t):
            u = abs(t) ** alpha
            return exp(-u) * cos(u * phi_constant - x * t)

    res, error = quad(f_int, 0, inf, epsabs=tol, limit=limit)
    return res / pi


def cdf(x, alpha, beta):
    raise NotImplementedError("cdf is not implemented")
