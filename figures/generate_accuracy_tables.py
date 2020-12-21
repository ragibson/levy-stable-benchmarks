from benchmarks.import_stable_tables import import_nolan_quantiles, import_stable_tables
from benchmarks.table_computations import test_accuracy_against_table
import numpy as np
import sys

if __name__ == "__main__":
    try:
        cdf_methods = [simple_quadrature, simple_monte_carlo, larger_monte_carlo, scipy_best, pylevy_miotto]
        cdf_method_names = ["simple_quadrature", "simple_monte_carlo", "larger_monte_carlo", "scipy_best",
                            "pylevy_miotto"]

        pdf_methods = [simple_quadrature, scipy_best, scipy_zolotarev, scipy_quadrature, pylevy_miotto]
        pdf_method_names = ["simple_quadrature", "scipy_best", "scipy_zolotarev", "scipy_quadrature", "pylevy_miotto"]
    except NameError as e:
        print(f"Your environment is missing method setup: {e}", file=sys.stderr)
        raise

    cdf_tables = [import_stable_tables("data/cdf_table.dat"),
                  import_stable_tables("data/cdf_quantile_table.dat", expect_quantiles=True),
                  import_nolan_quantiles()]
    pdf_tables = [import_stable_tables("data/pdf_table.dat"),
                  import_stable_tables("data/pdf_quantile_table.dat", single_queries=True,
                                       num_values_expected=len(cdf_tables[1])),
                  import_stable_tables("data/nolan_pdf_quantile.dat", single_queries=True,
                                       num_values_expected=len(cdf_tables[2]))]

    for density_function in ["CDF", "PDF"]:
        methods = cdf_methods if density_function == "CDF" else pdf_methods
        method_names = cdf_method_names if density_function == "CDF" else pdf_method_names
        tables = cdf_tables if density_function == "CDF" else pdf_tables

        for i, table in enumerate(tables):
            for use_absolute_tolerances in [True, False]:
                if density_function == "CDF":
                    if use_absolute_tolerances:
                        tol_range = (-2, -5)  # CDF absolute tolerances: 1E-2 to 1E-5
                    else:
                        tol_range = (-1, -4)  # CDF relative tolerances: 1E-1 to 1E-4
                else:
                    if use_absolute_tolerances:
                        tol_range = (-4, -7)  # PDF absolute tolerances: 1E-4 to 1E-7
                    else:
                        tol_range = (-1, -4)  # PDF relative tolerances: 1E-1 to 1E-4

                print(f"## {density_function} table {i}, absolute tolerances? {use_absolute_tolerances}\n")

                tolerances = [10 ** tol_exp for tol_exp in range(tol_range[0], tol_range[1] - 1, -1)]
                tolerance_label = "<b>Absolute</b> Tolerance" if use_absolute_tolerances else "<b>Relative</b> Tolerance"
                tolerances_header = "".join(f"<td>{f'{tol:.0E}'.replace('0', '')}</td>" for tol in tolerances)
                print("<table>\n"
                      f"  <tr><td></td><td colspan=\"4\">{tolerance_label}</td></tr>\n"
                      f"  <tr><td>Method</td>{tolerances_header}</tr>")
                for method, name in zip(methods, method_names):
                    print("  <tr>\n"
                          f"    <td>{name}</td>")
                    accuracies = [
                        test_accuracy_against_table(method.cdf if density_function == "CDF" else method.pdf,
                                                    table, tol=tol, tol_is_absolute=use_absolute_tolerances)
                        for tol in tolerances
                    ]
                    print("    " + "".join(f"<td>{np.floor(1000 * accuracy) / 10:.1f}%</td>"
                                           for accuracy in accuracies))
                    print("  </tr>")
                print(r"</table>")
