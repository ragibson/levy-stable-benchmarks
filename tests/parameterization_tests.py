from algorithms import (pylevy_miotto,
                        scipy_best, scipy_quadrature, scipy_zolotarev,
                        simple_quadrature, simple_monte_carlo)
from scipy.optimize import minimize_scalar
import unittest


def make_test(pdf=None, cdf=None, decimal_places_tolerance=10, is_known_bug_func=None):
    if is_known_bug_func is None:
        is_known_bug_func = lambda alpha, beta: False

    class TestParameterizationConsistency(unittest.TestCase):
        alpha_testing_grid = [0.5, 1.0, 1.5, 2.0]
        beta_testing_grid = [-1.0, -0.5, 0.0, 0.5, 1.0]

        @staticmethod
        def compute_mode(func):
            return minimize_scalar(lambda x: -func(x)).x

        @staticmethod
        def compute_median_from_cdf(func):
            res = minimize_scalar(lambda x: abs(1 / 2 - func(x)))
            print(res)
            return minimize_scalar(lambda x: abs(1 / 2 - func(x))).x

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
            print(f"testing median alpha={alpha}, beta={beta} (correct)")
            correct_median = self.compute_median_from_cdf(lambda x: simple_quadrature.cdf(x, alpha=alpha, beta=beta))
            print(f"testing median alpha={alpha}, beta={beta} (func)")
            median = self.compute_median_from_cdf(lambda x: cdf(x, alpha=alpha, beta=beta))

            print(
                f"Simple_quadrature found median={correct_median} CDF={simple_quadrature.cdf(correct_median, alpha=alpha, beta=beta)}")
            print(f"func found median={median} CDF={cdf(median, alpha=alpha, beta=beta)}")

            self.assertAlmostEqual(correct_median, median, places=decimal_places_tolerance,
                                   msg=f"medians differ for alpha={alpha}, beta={beta}")

        def check_similar_pdf_scales(self, alpha, beta):
            correct_neg1 = simple_quadrature.pdf(-1, alpha=alpha, beta=beta)
            correct_pos1 = simple_quadrature.pdf(1, alpha=alpha, beta=beta)

            neg1 = pdf(-1, alpha=alpha, beta=beta)
            pos1 = pdf(1, alpha=alpha, beta=beta)

            self.assertAlmostEqual(correct_neg1, neg1, places=decimal_places_tolerance,
                                   msg=f"scales (pdf at -1) differ for alpha={alpha}, beta={beta}")
            self.assertAlmostEqual(correct_pos1, pos1, places=decimal_places_tolerance,
                                   msg=f"scales (pdf at +1) differ for alpha={alpha}, beta={beta}")

        def check_similar_cdf_scales(self, alpha, beta):
            correct_neg1 = simple_quadrature.cdf(-1, alpha=alpha, beta=beta)
            correct_pos1 = simple_quadrature.cdf(1, alpha=alpha, beta=beta)

            neg1 = cdf(-1, alpha=alpha, beta=beta)
            pos1 = cdf(1, alpha=alpha, beta=beta)

            self.assertAlmostEqual(correct_neg1, neg1, places=decimal_places_tolerance,
                                   msg=f"scales (cdf at -1) differ for alpha={alpha}, beta={beta}")
            self.assertAlmostEqual(correct_pos1, pos1, places=decimal_places_tolerance,
                                   msg=f"scales (pdf at +1) differ for alpha={alpha}, beta={beta}")

        def test_modes(self):
            if pdf is None:
                return

            for alpha in self.alpha_testing_grid:
                for beta in self.beta_testing_grid:
                    if is_known_bug_func(alpha, beta):
                        continue
                    self.check_similar_pdf_modes(alpha, beta)

        def test_medians(self):
            if cdf is None:
                return

            for alpha in self.alpha_testing_grid:
                for beta in self.beta_testing_grid:
                    if is_known_bug_func(alpha, beta):
                        continue
                    self.check_similar_cdf_medians(alpha, beta)

        def test_pdf_scales(self):
            if pdf is None:
                return

            for alpha in self.alpha_testing_grid:
                for beta in self.beta_testing_grid:
                    if is_known_bug_func(alpha, beta):
                        continue
                    self.check_similar_pdf_scales(alpha, beta)

        def test_cdf_scales(self):
            if cdf is None:
                return

            for alpha in self.alpha_testing_grid:
                for beta in self.beta_testing_grid:
                    if is_known_bug_func(alpha, beta):
                        continue
                    self.check_similar_cdf_scales(alpha, beta)

    return TestParameterizationConsistency


class TestScipyQuadrature(make_test(pdf=scipy_quadrature.pdf, cdf=None,
                                    decimal_places_tolerance=6,
                                    is_known_bug_func=lambda alpha, beta: alpha == 1.0 and beta != 0.0)):
    pass


if __name__ == "__main__":
    unittest.main()
