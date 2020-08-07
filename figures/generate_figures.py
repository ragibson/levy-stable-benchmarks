from benchmarks.import_stable_tables import import_nolan_quantiles, import_stable_tables
from benchmarks.table_computations import test_accuracy_against_table
import matplotlib.pyplot as plt
import numpy as np
import sys

if __name__ == "__main__":
    try:
        cdf_methods = [simple_quadrature, simple_monte_carlo, scipy_best, pylevy_miotto]
        cdf_method_names = ["simple_quadrature", "simple_monte_carlo", "scipy_best", "pylevy_miotto"]

        pdf_methods = [simple_quadrature, scipy_best, scipy_zolotarev, scipy_quadrature, pylevy_miotto]
        pdf_method_names = ["simple_quadrature", "scipy_best", "scipy_zolotarev", "scipy_quadrature", "pylevy_miotto"]
    except NameError as e:
        print(f"Your environment is missing method setup: {e}", file=sys.stderr)
        raise

    cdf_tables = [import_stable_tables("data/cdf_table.dat"),
                  import_stable_tables("data/quantile_table.dat", expect_quantiles=True),
                  import_nolan_quantiles()]
    pdf_tables = [import_stable_tables("data/pdf_table.dat")]
    num_plotting_points = 100


    def composite_cdf_accuracy_percentage(func, tol, tol_is_absolute):
        # 1/3rd weighting to each CDF table
        return 100 * np.mean([test_accuracy_against_table(func, table, tol=tol, tol_is_absolute=tol_is_absolute)
                              for table in cdf_tables])


    def composite_pdf_accuracy_percentage(func, tol, tol_is_absolute):
        # there is currently only one PDF table
        assert len(pdf_tables) == 1
        table = pdf_tables[0]
        return 100 * test_accuracy_against_table(func, table, tol, tol_is_absolute=tol_is_absolute)


    for density_function, use_absolute_tolerances in zip(["CDF", "CDF", "PDF", "PDF"], [True, False, True, False]):
        if density_function == "CDF":
            if use_absolute_tolerances:
                tol_range = (-2, -10)  # CDF absolute tolerances: 1E-2 to 1E-10
            else:
                tol_range = (-1, -10)  # CDF relative tolerances: 1E-1 to 1E-10
        else:
            if use_absolute_tolerances:
                tol_range = (-4, -10)  # PDF absolute tolerances: 1E-4 to 1E-10
            else:
                tol_range = (-1, -10)  # PDF relative tolerances: 1E-1 to 1E-10

        methods = cdf_methods if density_function == "CDF" else pdf_methods
        method_names = cdf_method_names if density_function == "CDF" else pdf_method_names

        plt.close()

        for method, name in zip(methods, method_names):
            print(f"working on {name}")
            tols = np.logspace(tol_range[0], tol_range[1], num_plotting_points)
            if density_function == "CDF":
                accuracies = [composite_cdf_accuracy_percentage(method.cdf, tol=tol,
                                                                tol_is_absolute=use_absolute_tolerances)
                              for tol in tols]
            else:
                accuracies = [composite_pdf_accuracy_percentage(method.pdf, tol=tol,
                                                                tol_is_absolute=use_absolute_tolerances)
                              for tol in tols]
            plt.plot(tols, accuracies, label=name)

        plt.xscale("log")
        plt.xticks([10 ** i for i in range(tol_range[1], tol_range[0] + 1)])  # label all powers of 10
        plt.gca().invert_xaxis()  # make tolerances decrease to the right
        plt.legend()
        plt.ylim([70, 101])  # plot 70% to slightly above 100% accuracies
        plt.xlabel("Absolute tolerance" if use_absolute_tolerances else "Relative tolerance")
        plt.ylabel("Composite accuracy percentage")
        plt.title(f"{density_function} {'absolute' if use_absolute_tolerances else 'relative'} "
                  f"accuracy percentages (higher is better)")
        plt.tight_layout()
        plt.savefig(f"figures/{density_function}_{'absolute' if use_absolute_tolerances else 'relative'}"
                    f"_accuracies.pdf")
