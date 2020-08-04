def import_nolan_quantiles(filename="data/quantile.dat"):
    """Imports Nolan's table of stable quantities as a list of (alpha, beta, x, p) tuples.

    The table is available from http://fs2.american.edu/jpnolan/www/stable/stable.html"""

    with open(filename, "r") as file:
        lines = file.readlines()

        # we return rows [alpha, beta, x, p] such that Levy-stable CDF(x, alpha, beta) = p
        data_list = []
        for line_idx, line in enumerate(lines):
            if "alpha=" in line:  # start of quantile block
                # Nolan's table alpha values are
                #   2.0, 1.95
                #   1.9 to 0.1  (step 0.1)
                split_alpha_header = line.split()
                assert len(split_alpha_header) == 2
                alpha = float(split_alpha_header[1])

                # Nolan's table column format is
                #   p  beta=0.0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0
                # There are 171 p-values for each value of alpha
                #   0.00001 to 0.00010  (step 0.00001)
                #   0.0001 to 0.0010    (step 0.0001)
                #   0.001 to 0.010      (step 0.001)
                #   0.01 to 0.10        (step 0.005)
                #   0.10 to 0.90        (step 0.01)
                #   and upper tail similar to lower tail
                for row_offset in range(3, 174):
                    table_row = lines[line_idx + row_offset].split()
                    assert len(table_row) == 12

                    p = float(table_row[0])
                    for beta_idx, x in enumerate(table_row[1:]):
                        x = float(x)
                        beta = beta_idx / 10  # from 0.0 to 1.0 (step 0.1)
                        data_list.append((alpha, beta, x, p))

        assert len(data_list) == 22 * 11 * 171  # 22 alpha values, 11 beta values, 171 p-values
        return data_list
