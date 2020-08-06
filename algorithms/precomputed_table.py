_PDF_CDF_TABLE = {}


def set_table(table):
    _PDF_CDF_TABLE = table


def pdf(x, alpha, beta):
    return _PDF_CDF_TABLE[(x, alpha, beta)]


def cdf(x, alpha, beta):
    return _PDF_CDF_TABLE[(x, alpha, beta)]
