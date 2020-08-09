from scipy.integrate import quad
from numpy import exp, inf, pi, cos, sin, tan, log


def pdf(x, alpha, beta, tol=1e-8, limit=10 ** 3):
    if beta == 0.0:
        res, error = quad(lambda t: exp(-t ** alpha), 0, inf,
                          epsabs=tol, limit=limit, weight="cos", wvar=x)
        res = res / pi
    elif alpha == 1.0:
        phi_constant = -2 * beta / pi
        res1, error1 = quad(lambda t: exp(-t) * cos(t * phi_constant * log(t)), 1e-10, inf,
                            epsabs=tol, limit=limit, weight="cos", wvar=x)
        res2, error2 = quad(lambda t: exp(-t) * sin(t * phi_constant * log(t)), 1e-10, inf,
                            epsabs=tol, limit=limit, weight="sin", wvar=x)
        res = (res1 + res2) / pi
    else:
        phi_constant = beta * tan(pi * alpha / 2)
        res1, error1 = quad(lambda t: exp(-t ** alpha) * cos(t ** alpha * phi_constant), 0, inf,
                            epsabs=tol, limit=limit, weight="cos", wvar=x + phi_constant)
        res2, error2 = quad(lambda t: exp(-t ** alpha) * sin(t ** alpha * phi_constant), 0, inf,
                            epsabs=tol, limit=limit, weight="sin", wvar=x + phi_constant)
        res = (res1 + res2) / pi

    # TODO: need to handle error == 0.0 bug in weighted quad(); will probably fallback to unweighted quad
    return max(res, 0)


def cdf(x, alpha, beta, tol=1e-8, limit=10 ** 3):
    if beta == 0.0:
        res, error = quad(lambda t: exp(-t ** alpha) / t if t != 0 else 0, 0, inf,
                          epsabs=tol, limit=limit, weight="sin", wvar=x)
        res = 1 / 2 + res / pi
    elif alpha == 1.0:
        phi_constant = -2 * beta / pi
        res1, error1 = quad(lambda t: exp(-t) * cos(t * phi_constant * log(t)) / t if t != 0 else 0, 0, inf,
                            epsabs=tol, limit=limit, weight="sin", wvar=x)
        res2, error2 = quad(lambda t: exp(-t) * sin(t * phi_constant * log(t)) / t if t != 0 else 0, 0, inf,
                            epsabs=tol, limit=limit, weight="cos", wvar=x)
        res = 1 / 2 + (res1 - res2) / pi
    else:
        phi_constant = beta * tan(pi * alpha / 2)
        res1, error1 = quad(lambda t: exp(-t ** alpha) * cos(t ** alpha * phi_constant) / t if t != 0 else 0, 0, inf,
                            epsabs=tol, limit=limit, weight="sin", wvar=x + phi_constant)
        res2, error2 = quad(lambda t: exp(-t ** alpha) * sin(t ** alpha * phi_constant) / t if t != 0 else 0, 0, inf,
                            epsabs=tol, limit=limit, weight="cos", wvar=x + phi_constant)
        res = 1 / 2 + (res1 - res2) / pi
    return max(res, 0)
