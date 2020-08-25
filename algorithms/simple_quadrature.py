from scipy.integrate import quad
from numpy import exp, inf, pi, cos, sin, tan, log


def _indefinite_trig_weighted_quad(f, epsabs, limit, weight, wvar):
    """Integrates f(t)*weight(t*wvar) from 0 to infinity while handling some scipy issues/bugs."""
    # scipy handles inf incorrectly, so we filter out t == 0. See https://github.com/scipy/scipy/issues/12662
    f_int = lambda t: f(t) if t > 0 else 0

    res, error = quad(f_int, 0, inf, epsabs=epsabs, limit=limit, weight=weight, wvar=wvar)

    # need to check incorrect weighted integration results. See https://github.com/scipy/scipy/issues/12684
    # previously attempted (res == 0.0 or error == 0.0 or res > 1e307 or abs(res) < error)

    return res, error


def pdf(x, alpha, beta, tol=1e-12, limit=10 ** 3):
    if alpha == 1.0:
        phi_constant = -2 * beta / pi
        res1, error1 = _indefinite_trig_weighted_quad(lambda t: exp(-t) * cos(t * phi_constant * log(t)),
                                                      epsabs=tol, limit=limit, weight="cos", wvar=x)
        res2, error2 = _indefinite_trig_weighted_quad(lambda t: exp(-t) * sin(t * phi_constant * log(t)),
                                                      epsabs=tol, limit=limit, weight="sin", wvar=x)
        res = (res1 + res2) / pi
    else:
        phi_constant = beta * tan(pi * alpha / 2)

        # TODO: I don't like this check, but it avoids catastrophic cancellation in these extreme cases
        #   This is an analytic result, but you should probably reformulate to avoid this. In any case, this does not
        #   significantly improve accuracy AND does not fix the issue when x is _very_ close to -phi_constant
        if alpha < 1.0 and beta == 1.0 and x < -phi_constant:
            return 0.0  # abrupt change at abs(beta) == 1.0 means the CDF is 0.0 here
        if alpha < 1.0 and beta == -1.0 and x > -phi_constant:
            return 0.0  # abrupt change at abs(beta) == 1.0 means the CDF is 1.0 here (so PDF is 0.0)

        res1, error1 = _indefinite_trig_weighted_quad(lambda t: exp(-t ** alpha) * cos(t ** alpha * phi_constant),
                                                      epsabs=tol, limit=limit, weight="cos", wvar=x + phi_constant)
        res2, error2 = _indefinite_trig_weighted_quad(lambda t: exp(-t ** alpha) * sin(t ** alpha * phi_constant),
                                                      epsabs=tol, limit=limit, weight="sin", wvar=x + phi_constant)
        res = (res1 + res2) / pi

    return max(res, 0)


def cdf(x, alpha, beta, tol=1e-12, limit=10 ** 3):
    if alpha == 1.0:
        phi_constant = -2 * beta / pi
        res1, error1 = _indefinite_trig_weighted_quad(lambda t: exp(-t) * cos(t * phi_constant * log(t)) / t,
                                                      epsabs=tol, limit=limit, weight="sin", wvar=x)
        res2, error2 = _indefinite_trig_weighted_quad(lambda t: exp(-t) * sin(t * phi_constant * log(t)) / t,
                                                      epsabs=tol, limit=limit, weight="cos", wvar=x)
        res = (pi / 2 + res1 - res2) / pi
    else:
        phi_constant = beta * tan(pi * alpha / 2)

        # TODO: I don't like this check, but it avoids catastrophic cancellation in these extreme cases
        #   This is an analytic result, but you should probably reformulate to avoid this. In any case, this does not
        #   significantly improve accuracy AND does not fix the issue when x is _very_ close to -phi_constant
        if alpha < 1.0 and beta == 1.0 and x < -phi_constant:
            return 0.0  # abrupt change at abs(beta) == 1.0 means the CDF is 0.0 here
        if alpha < 1.0 and beta == -1.0 and x > -phi_constant:
            return 1.0  # abrupt change at abs(beta) == 1.0 means the CDF is 1.0 here

        res1, error1 = _indefinite_trig_weighted_quad(lambda t: exp(-t ** alpha) * cos(t ** alpha * phi_constant) / t,
                                                      epsabs=tol, limit=limit, weight="sin", wvar=x + phi_constant)
        res2, error2 = _indefinite_trig_weighted_quad(lambda t: exp(-t ** alpha) * sin(t ** alpha * phi_constant) / t,
                                                      epsabs=tol, limit=limit, weight="cos", wvar=x + phi_constant)
        res = (pi / 2 + res1 - res2) / pi

    return max(res, 0)
