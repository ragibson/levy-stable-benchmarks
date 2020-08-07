class PrecomputedTableAlgorithm:
    def __init__(self, pdf_table=None, cdf_table=None):
        self.pdf_table = pdf_table
        self.cdf_table = cdf_table

    def pdf(self, x, alpha, beta):
        if self.pdf_table is None:
            return 0
        return self.pdf_table[(x, alpha, beta)]

    def cdf(self, x, alpha, beta):
        if self.cdf_table is None:
            return 0
        return self.cdf_table[(x, alpha, beta)]


def pdf(x, alpha, beta):
    raise NotImplementedError("No table specified. Use the PrecomputedTableAlgorithm class.")


def cdf(x, alpha, beta):
    raise NotImplementedError("No table specified. Use the PrecomputedTableAlgorithm class.")
