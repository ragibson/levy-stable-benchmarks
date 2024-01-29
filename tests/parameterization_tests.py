from algorithms import (pylevy_miotto,
                        scipy_piecewise, scipy_dni,
                        simple_quadrature, simple_monte_carlo)
from scipy.optimize import minimize_scalar
import numpy as np
import unittest

np.random.seed(0)
simple_monte_carlo.set_monte_carlo_size(10 ** 7)


def make_test(pdf=None, cdf=None, decimal_places_tolerance=10, is_known_bug_cdf=None, is_known_bug_pdf=None):
    if is_known_bug_cdf is None:
        is_known_bug_cdf = lambda alpha, beta: False

    if is_known_bug_pdf is None:
        is_known_bug_pdf = lambda alpha, beta: False

    class TestParameterizationConsistency(unittest.TestCase):
        alpha_testing_grid = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
        beta_testing_grid = [-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0]

        @staticmethod
        def compute_mode(func):
            return minimize_scalar(lambda x: -func(x)).x

        @staticmethod
        def compute_median_from_cdf(func):
            res = minimize_scalar(lambda x: abs(1 / 2 - func(x)))
            print(res)
            return res.x

        def check_similar_pdf_modes(self, alpha, beta):
            # we assume our simple_quadrature is accurate here
            # at the very least, it can be used as a consistent benchmark
            correct_mode = self.compute_mode(lambda x: simple_quadrature.pdf(x, alpha=alpha, beta=beta))
            mode = self.compute_mode(lambda x: pdf(x, alpha=alpha, beta=beta))

            self.assertAlmostEqual(correct_mode, mode, places=decimal_places_tolerance,
                                   msg=f"modes differ for alpha={alpha}, beta={beta}")

        def check_similar_cdf_medians(self, alpha, beta):
            # we assume our simple_quadrature is accurate here
            # at the very least, it can be used as a consistent benchmark
            correct_median = self.compute_median_from_cdf(lambda x: simple_quadrature.cdf(x, alpha=alpha, beta=beta))
            median = self.compute_median_from_cdf(lambda x: cdf(x, alpha=alpha, beta=beta))

            self.assertAlmostEqual(correct_median, median, places=decimal_places_tolerance,
                                   msg=f"medians differ for alpha={alpha}, beta={beta}")

        def check_similar_pdf_scales(self, alpha, beta):
            correct_neg2 = simple_quadrature.pdf(-2, alpha=alpha, beta=beta)
            correct_pos2 = simple_quadrature.pdf(2, alpha=alpha, beta=beta)

            neg2 = pdf(-2, alpha=alpha, beta=beta)
            pos2 = pdf(2, alpha=alpha, beta=beta)

            self.assertAlmostEqual(correct_neg2, neg2, places=decimal_places_tolerance,
                                   msg=f"scales (pdf at -2) differ for alpha={alpha}, beta={beta}")
            self.assertAlmostEqual(correct_pos2, pos2, places=decimal_places_tolerance,
                                   msg=f"scales (pdf at +2) differ for alpha={alpha}, beta={beta}")

        def check_similar_cdf_scales(self, alpha, beta):
            correct_neg2 = simple_quadrature.cdf(-2, alpha=alpha, beta=beta)
            correct_pos2 = simple_quadrature.cdf(2, alpha=alpha, beta=beta)

            neg2 = cdf(-2, alpha=alpha, beta=beta)
            pos2 = cdf(2, alpha=alpha, beta=beta)

            self.assertAlmostEqual(correct_neg2, neg2, places=decimal_places_tolerance,
                                   msg=f"scales (cdf at -2) differ for alpha={alpha}, beta={beta}")
            self.assertAlmostEqual(correct_pos2, pos2, places=decimal_places_tolerance,
                                   msg=f"scales (pdf at +2) differ for alpha={alpha}, beta={beta}")

        def test_modes(self):
            if pdf is None:
                return

            for alpha in self.alpha_testing_grid:
                for beta in self.beta_testing_grid:
                    if is_known_bug_pdf(alpha, beta):
                        continue
                    if alpha == 2.0 or beta in {-1.0, 0.0, 1.0}:
                        # TODO: simple_quadrature seems to have some minor difficulties for extreme alpha/beta
                        #   since we're using it as our consistent benchmark, we just skip them here
                        continue
                    self.check_similar_pdf_modes(alpha, beta)

        def test_medians(self):
            if cdf is None:
                return

            for alpha in self.alpha_testing_grid:
                for beta in self.beta_testing_grid:
                    if is_known_bug_cdf(alpha, beta):
                        continue
                    if alpha == 2.0 or beta in {-1.0, 0.0, 1.0}:
                        # TODO: simple_quadrature seems to have some minor difficulties for extreme alpha/beta
                        #   since we're using it as our consistent benchmark, we just skip them here
                        continue
                    self.check_similar_cdf_medians(alpha, beta)

        def test_pdf_scales(self):
            if pdf is None:
                return

            for alpha in self.alpha_testing_grid:
                for beta in self.beta_testing_grid:
                    if is_known_bug_pdf(alpha, beta):
                        continue
                    self.check_similar_pdf_scales(alpha, beta)

        def test_cdf_scales(self):
            if cdf is None:
                return

            for alpha in self.alpha_testing_grid:
                for beta in self.beta_testing_grid:
                    if is_known_bug_cdf(alpha, beta):
                        continue
                    self.check_similar_cdf_scales(alpha, beta)

    return TestParameterizationConsistency


class TestPylevyMiotto(make_test(pdf=pylevy_miotto.pdf, cdf=pylevy_miotto.cdf,
                                 decimal_places_tolerance=2,
                                 is_known_bug_pdf=lambda alpha, beta: alpha < 0.5,
                                 is_known_bug_cdf=lambda alpha, beta: alpha < 0.5)):
    # alpha < 0.5 is not implemented in this library (they round to alpha = 0.5 in this case)
    # it is also fairly inaccurate in general, note the tolerance of 2 decimal places here
    pass


class TestScipyPiecewise(make_test(pdf=scipy_piecewise.pdf, cdf=scipy_piecewise.cdf,
                                   decimal_places_tolerance=7,
                                   is_known_bug_pdf=lambda alpha, beta: alpha <= 0.5 or alpha == 2.0)):
    # scipy_piecewise can be pretty inaccurate for the same PDF regions as DNI, so we omit them
    # similarly, extreme alpha/beta values seem to have slight CDF inaccuracies
    pass


class TestScipyDNI(make_test(pdf=scipy_dni.pdf, cdf=None,
                             decimal_places_tolerance=2,
                             is_known_bug_pdf=lambda alpha, beta: alpha < 2.0 or abs(beta) == 1.0)):
    # scipy_dni fails catastrophically relatively often, but is otherwise pretty accurate
    # this method basically has to be manually checked and does indeed align well
    pass


class TestSimpleMonteCarlo(make_test(pdf=None, cdf=simple_monte_carlo.cdf,
                                     decimal_places_tolerance=2)):
    # simple_monte_carlo is (intentionally) not very accurate, note the tolerance of 2 decimal places here
    pass


class TestSimpleQuadrature(make_test(pdf=simple_quadrature.pdf, cdf=simple_quadrature.cdf,
                                     decimal_places_tolerance=10)):
    pass


if __name__ == "__main__":
    unittest.main()
