from algorithms.our_monte_carlo import pdf, cdf
from benchmarks.test_accuracy_against_table import test_accuracy_against_table
from benchmarks.import_stable_tables import import_nolan_quantiles
from time import time

table = import_nolan_quantiles()
start_time = time()
acc = test_accuracy_against_table(cdf, table, tol=1e-2, show_progress=True)
duration = time() - start_time
print(f"Accuracy: {100 * acc:.1f}% in {duration:.1f} s")

# Preliminary CDF results (tol=1e-2):
# scipy_best 1.5.2       -- Accuracy: 62.6% in 106.4 s
# our_monte_carlo        -- Accuracy: 60.7% in 4.6 s
