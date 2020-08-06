# levy-stable-benchmarks

## CDF accuracy percentages

### CDF table (-100 <= x <= 100)

<table>
  <tr>
    <td></td><td colspan="4">Relative Tolerance</td><td>Average Time Per Call</td>
  </tr>
  <tr>
    <td>Method</td><td>1E-1</td><td>1E-2</td><td>1E-3</td><td>1E-4</td>
  </tr>
  <tr>
    <td>`simple_monte_carlo`</td>
    <td>92.7%</td><td>69.4%</td><td>52.1%</td><td>34.8%</td>
    <td>170 us</td>
  </tr>
  <tr>
    <td>`simple_quadrature`</td>
    <td>100.0%</td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>`pylevy_miotto`</td>
    <td>85.1%</td><td>69.4%</td><td></td><td></td>
    <td>1.32 ms</td>
  </tr>
  <tr>
    <td>`scipy_best`</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>`pystable_jones`</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

### Quantile table (0.001 <= p <= 0.999)

<table>
  <tr>
    <td></td><td colspan="4">Relative Tolerance</td><td>Average Time Per Call</td>
  </tr>
  <tr>
    <td>Method</td><td>1E-1</td><td>1E-2</td><td>1E-3</td><td>1E-4</td>
  </tr>
  <tr>
    <td>`simple_monte_carlo`</td>
    <td>97.8%</td><td>96.6%</td><td>56.6%</td><td>10.1%</td>
    <td>171 us</td>
  </tr>
  <tr>
    <td>`simple_quadrature`</td>
    <td>98.6%</td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
  <td>`pylevy_miotto`</td>
    <td>90.8%</td><td>80.8%</td><td></td><td></td>
    <td>1.34 ms</td>
  </tr>
  <tr>
    <td>`scipy_best`</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>`pystable_jones`</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

### Nolan Quantile table (0.00001 <= p <= 0.99999)

<table>
  <tr>
    <td></td><td colspan="4">Relative Tolerance</td><td>Average Time Per Call</td>
  </tr>
  <tr>
    <td>Method</td><td>1E-1</td><td>1E-2</td><td>1E-3</td><td>1E-4</td>
  </tr>
  <tr>
    <td>`simple_monte_carlo`</td>
    <td>92.3%</td><td>81.9%</td><td>54.3%</td><td>23.3%</td>
    <td>963 us</td>
  </tr>
  <tr>
    <td>`simple_quadrature`</td>
    <td>94.1%</td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
  <td>`pylevy_miotto`</td>
    <td>85.9%</td><td>78.3%</td><td></td><td></td>
    <td>1.31 ms</td>
  </tr>
  <tr>
    <td>`scipy_best`</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>`pystable_jones`</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>

## PDF accuracy percentages

### PDF table (-100 <= x <= 100)

<table>
  <tr>
    <td></td><td colspan="4">Relative Tolerance</td><td>Average Time Per Call</td>
  </tr>
  <tr>
    <td>Method</td><td>1E-1</td><td>1E-2</td><td>1E-3</td><td>1E-4</td>
  </tr>
  <tr>
    <td>`simple_monte_carlo`</td>
    <td>64.7%</td><td>16.5%</td><td>5.7%</td><td>4.7%</td>
    <td>172 us</td>
  </tr>
  <tr>
    <td>`simple_quadrature`</td>
    <td>100.0%</td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>`pylevy_miotto`</td>
    <td>83.8%</td><td>51.9%</td><td></td><td></td>
    <td>1.32 ms</td>
  </tr>
  <tr>
    <td>`scipy_best`</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>`scipy_quadrature`</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>`scipy_zolotarev`</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
  <tr>
    <td>`pystable_jones`</td>
    <td></td><td></td><td></td><td></td>
    <td></td>
  </tr>
</table>
