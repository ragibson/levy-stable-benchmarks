# levy-stable-benchmarks

### ***This is a work in progress. Please come back later, except for limited purposes and/or review.***

Stable distributions (sometimes called Lévy alpha-stable distributions) are
important for modelling data across several disciplines including signal
processing, physics, and finance. Despite this, many Python libraries
provide buggy and/or inaccurate implementations for computing its PDF/CDF.

This repository attempts to define a benchmark to test the accuracy of
such implementations. We also provide some alternative calculation methods.

![accuracy figures](figures/accuracy_figures.png)

Note: the new PDF computations for scipy_quadrature will take several days
to complete. The figure above will be updated then.

# Table of Contents
  * [CDF accuracy percentages](#CDFAccuracy)
  * [PDF accuracy percentages](#PDFAccuracy)
  * [FAQ, notes, and limitations](#FAQ)

<a name = "CDFAccuracy"></a>
## CDF accuracy percentages

### CDF table (-100 <= x <= 100)

<table>
  <tr><td></td><td colspan="4"><b>Absolute</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-2</td><td>1E-3</td><td>1E-4</td><td>1E-5</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>100.0%</td><td>100.0%</td><td>99.6%</td><td>99.4%</td>
    <td></td>
  </tr>
  <tr>
    <td>simple_monte_carlo</td>
    <td>100.0%</td><td>99.9%</td><td>73.6%</td><td>32.2%</td>
    <td></td>
  </tr>
  <tr>
    <td>larger_monte_carlo</td>
    <td>100.0%</td><td>100.0%</td><td>99.6%</td><td>74.1%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>97.8%</td><td>97.4%</td><td>95.4%</td><td>88.4%</td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>83.4%</td><td>77.8%</td><td>68.1%</td><td>56.8%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

<table>
  <tr><td></td><td colspan="4"><b>Relative</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-1</td><td>1E-2</td><td>1E-3</td><td>1E-4</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>99.9%</td><td>99.9%</td><td>99.9%</td><td>99.6%</td>
    <td></td>
  </tr>
  <tr>
    <td>simple_monte_carlo</td>
    <td>96.5%</td><td>77.5%</td><td>56.6%</td><td>38.4%</td>
    <td></td>
  </tr>
  <tr>
    <td>larger_monte_carlo</td>
    <td>99.3%</td><td>97.3%</td><td>80.1%</td><td>56.8%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>89.3%</td><td>88.9%</td><td>88.6%</td><td>88.6%</td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>85.1%</td><td>69.4%</td><td>56.4%</td><td>44.5%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

### CDF quantile table (0.001 <= p <= 0.999)

<table>
  <tr><td></td><td colspan="4"><b>Absolute</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-2</td><td>1E-3</td><td>1E-4</td><td>1E-5</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>99.2%</td><td>99.2%</td><td>99.2%</td><td>99.2%</td>
    <td></td>
  </tr>
  <tr>
    <td>simple_monte_carlo</td>
    <td>100.0%</td><td>99.5%</td><td>35.9%</td><td>3.8%</td>
    <td></td>
  </tr>
  <tr>
    <td>larger_monte_carlo</td>
    <td>100.0%</td><td>100.0%</td><td>99.9%</td><td>30.2%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>97.5%</td><td>97.5%</td><td>97.5%</td><td>97.5%</td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>83.3%</td><td>78.0%</td><td>76.2%</td><td>75.0%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

<table>
  <tr><td></td><td colspan="4"><b>Relative</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-1</td><td>1E-2</td><td>1E-3</td><td>1E-4</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>99.3%</td><td>99.2%</td><td>99.2%</td><td>99.2%</td>
    <td></td>
  </tr>
  <tr>
    <td>simple_monte_carlo</td>
    <td>100.0%</td><td>99.3%</td><td>74.9%</td><td>19.4%</td>
    <td></td>
  </tr>
  <tr>
    <td>larger_monte_carlo</td>
    <td>100.0%</td><td>99.9%</td><td>99.5%</td><td>79.0%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>97.6%</td><td>97.5%</td><td>97.5%</td><td>97.5%</td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>90.8%</td><td>80.8%</td><td>77.5%</td><td>75.7%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

### Nolan CDF quantile table (0.00001 <= p <= 0.99999)

<table>
  <tr><td></td><td colspan="4"><b>Absolute</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-2</td><td>1E-3</td><td>1E-4</td><td>1E-5</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>96.4%</td><td>96.0%</td><td>95.8%</td><td>95.6%</td>
    <td></td>
  </tr>
  <tr>
    <td>simple_monte_carlo</td>
    <td>99.4%</td><td>98.9%</td><td>55.6%</td><td>20.2%</td>
    <td></td>
  </tr>
  <tr>
    <td>larger_monte_carlo</td>
    <td>99.4%</td><td>99.1%</td><td>98.9%</td><td>51.2%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>95.6%</td><td>95.2%</td><td>94.7%</td><td>89.6%</td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>83.0%</td><td>79.2%</td><td>74.9%</td><td>69.7%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

<table>
  <tr><td></td><td colspan="4"><b>Relative</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-1</td><td>1E-2</td><td>1E-3</td><td>1E-4</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>96.5%</td><td>95.9%</td><td>95.8%</td><td>95.6%</td>
    <td></td>
  </tr>
  <tr>
    <td>simple_monte_carlo</td>
    <td>97.1%</td><td>87.5%</td><td>67.2%</td><td>29.4%</td>
    <td></td>
  </tr>
  <tr>
    <td>larger_monte_carlo</td>
    <td>99.4%</td><td>98.0%</td><td>88.3%</td><td>67.8%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>93.4%</td><td>92.7%</td><td>92.5%</td><td>92.3%</td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>85.8%</td><td>78.3%</td><td>73.5%</td><td>67.5%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

<a name = "PDFAccuracy"></a>
## PDF accuracy percentages

### PDF table (-100 <= x <= 100)

<table>
  <tr><td></td><td colspan="4"><b>Absolute</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-4</td><td>1E-5</td><td>1E-6</td><td>1E-7</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>99.9%</td><td>99.9%</td><td>99.9%</td><td>99.9%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>97.4%</td><td>96.4%</td><td>92.5%</td><td>87.1%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_zolotarev</td>
    <td>98.5%</td><td>96.6%</td><td>92.5%</td><td>87.2%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_quadrature</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>90.5%</td><td>79.2%</td><td>66.4%</td><td>36.4%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

<table>
  <tr><td></td><td colspan="4"><b>Relative</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-1</td><td>1E-2</td><td>1E-3</td><td>1E-4</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>100.0%</td><td>100.0%</td><td>100.0%</td><td>99.9%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>86.2%</td><td>86.2%</td><td>86.2%</td><td>86.2%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_zolotarev</td>
    <td>86.2%</td><td>86.2%</td><td>86.2%</td><td>86.2%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_quadrature</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>83.7%</td><td>51.9%</td><td>27.5%</td><td>15.0%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

### PDF quantile table (0.001 <= p <= 0.999)

<table>
  <tr><td></td><td colspan="4"><b>Absolute</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-4</td><td>1E-5</td><td>1E-6</td><td>1E-7</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>99.1%</td><td>99.1%</td><td>99.1%</td><td>98.9%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>97.5%</td><td>97.4%</td><td>97.4%</td><td>97.3%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_zolotarev</td>
    <td>97.5%</td><td>97.5%</td><td>97.4%</td><td>97.3%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_quadrature</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>83.1%</td><td>80.1%</td><td>75.1%</td><td>54.1%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

<table>
  <tr><td></td><td colspan="4"><b>Relative</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-1</td><td>1E-2</td><td>1E-3</td><td>1E-4</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>98.7%</td><td>98.7%</td><td>98.7%</td><td>98.7%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>97.5%</td><td>97.4%</td><td>97.4%</td><td>97.4%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_zolotarev</td>
    <td>97.4%</td><td>97.4%</td><td>97.4%</td><td>97.4%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_quadrature</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>83.8%</td><td>77.5%</td><td>76.2%</td><td>74.1%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

### Nolan PDF quantile table (0.00001 <= p <= 0.99999)

<table>
  <tr><td></td><td colspan="4"><b>Absolute</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-4</td><td>1E-5</td><td>1E-6</td><td>1E-7</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>95.8%</td><td>95.8%</td><td>95.8%</td><td>95.7%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>95.8%</td><td>95.7%</td><td>94.9%</td><td>92.8%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_zolotarev</td>
    <td>96.8%</td><td>96.6%</td><td>95.5%</td><td>93.2%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_quadrature</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>89.1%</td><td>84.1%</td><td>74.9%</td><td>52.1%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

<table>
  <tr><td></td><td colspan="4"><b>Relative</b> Tolerance</td><td>Average Time Per Call</td></tr>
  <tr><td>Method</td><td>1E-1</td><td>1E-2</td><td>1E-3</td><td>1E-4</td><td></td></tr>
  <tr>
    <td>simple_quadrature</td>
    <td>94.7%</td><td>94.7%</td><td>94.7%</td><td>94.7%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_best</td>
    <td>90.8%</td><td>90.8%</td><td>90.8%</td><td>90.8%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_zolotarev</td>
    <td>90.8%</td><td>90.8%</td><td>90.8%</td><td>90.8%</td>
    <td></td>
  </tr>
  <tr>
    <td>scipy_quadrature</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>pylevy_miotto</td>
    <td>86.7%</td><td>78.2%</td><td>68.9%</td><td>61.4%</td>
    <td></td>
  </tr>
  <tr>
    <td>pystable_jones</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

<a name = "FAQ"></a>
## FAQ: notes and limitations

TODO: table of contents for FAQ?

##### How are "accuracy percentage" and "composite accuracy" defined?

"Accuracy percentage" is the percentage of tabulated values computed to the
desired tolerance.

When listed above, the accuracy percentages are truncated (not rounded), so a
method will only have 100.0% accuracy if it is within the specified tolerance
on *all* the test cases.

"Composite accuracy" is the average accuracy percentage on all the PDF or CDF
tables. There are three tables each for PDF and CDF, so ~33% of the weighting
goes to each.

##### Where did these PDF/CDF tables come from? Are they accurate?

TODO: Nolan quantile table may have some inaccuracies, but this needs more testing to verify

##### What are some known limitations of this benchmark?

TODO: beta < 0 implementation is assumed correct (by symmetry)

TODO: behavior **very** far out (p < 0.00001) into the tails is not tested, but this is probably a minor concern in practice

##### Why is the range of tested absolute tolerances different for CDF vs. PDF?

##### Where can I find the libraries tested?

There are six methods tested here. See the links below and the code in [algorithms](algorithms).

 * Our simple methods
   * [**simple_quadrature**](algorithms/simple_quadrature.py): direct numerical integration (TODO: derivations?)
   * [**simple_monte_carlo**](algorithms/simple_monte_carlo.py): monte carlo scheme based on the [Chambers-Mallows-Stuck method of simulating stable random variables](https://doi.org/10.1080%2F01621459.1976.10480344)
   * **larger_monte_carlo**: same as simple_monte_carlo, but with a sample size of 100 million
 * Scipy's methods (tested on version 1.5.2)
   * [**scipy_best**](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html) with `pdf_default_method = "best"`
   * [**scipy_zolotarev**](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html) with `pdf_default_method = "zolotarev"`
   * [**scipy_quadrature**](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html) with `pdf_default_method = "quadrature"`
 * [**pylevy_miotto**](https://github.com/josemiotto/pylevy) (tested on commit [64c525f](https://github.com/josemiotto/pylevy/tree/64c525f273d00d89cbbe531a6557b17b74d18f88))
 * TODO: pystable_jones?

##### The literature is very inconsistent/fragmented with respect to parameterizing stable distributions. Are you sure the libraries are actually consistent in their calculations here?

TODO: Mark Veillette says this well:

> One of the most frustrating issues in dealing with alpha-stable distribtuions is that its parameterization is not consistent across the literature (there are over half a dozen parameterizations). [...] The most common way to specify a parameterization is to look at the characteristic function of the alpha-stable random variable.
>
> One further annoyance is that the names of the 4 parameters are also inconsistent. [...] The letters alpha and beta are used almost everywhere you look, while the other two parameters are almost always different.

TODO: see our [tests to prove our transformations are good](tests/parameterization_tests.py)

##### pylevy_miotto appears somewhat accurate in practice. Why does it perform so poorly in this benchmark?

TODO: pylevy_miotto parameter limitations and implementation bugs

##### simple_quadrature seems very accurate. Is this always the case?

TODO: simple_quadrature limitations and potential hybrid scheme, should probably add the derivation for the integrands (or find our strategy in the literature somewhere)

##### simple_monte_carlo appears far slower in practice than listed here. Why?

##### These methods vary greatly in their speed. What is a "good" average time per call? 

TODO: highly domain specific, include machine specs, etc.

TODO: Nolan claims to have

> code to quickly approximate stable densities.  This routine is much faster than the regular density calculations: approximately 1 million density evaluations/second can be performed on a 1 GHz Pentium.

This appears to suggest that an average time per call of <1 us (!) is "easily" feasible on modern hardware. However, this is several orders of magnitude faster than any of the methods tested here.

##### Some of the methods only appear in the PDF or CDF tests. Why?

##### I know of a Python library that is missing from this benchmark. Can you add it?

TODO: please raise an issue and I'll try to add it.