## Multiple grouped summaries

Earlier in this chapter you saw that the `.agg()` method is useful to compute multiple statistics on multiple variables. It also works with grouped data. NumPy, which is imported as `np`, has many different summary statistics functions, including:

* `np.min()`
* `np.max()`
* `np.mean()`
* `np.median()`

`sales` is available and `pandas` is imported as `pd`.

<hr>

**Instructions**

* Import NumPy with the alias `np`.
* Get the min, max, mean, and median of `weekly_sales` for each store type using `.groupby()` and `.agg().` Store this as `sales_stats`. Make sure to use `numpy` functions!
* Get the min, max, mean, and median of `unemployment` and `fuel_price_usd_per_l` for each store type. Store this as `unemp_fuel_stats`.


## Script
```
# Import NumPy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")["unemployment", "fuel_price_usd_per_l"].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)
```

## Output
```
        amin       amax       mean    median
type
A    -1098.0  293966.05  23674.667  11943.92
B     -798.0  232558.51  25696.678  13336.

     unemployment                      fuel_price_usd_per_l
             amin   amax   mean median                 amin   amax   mean median
type
A           3.879  8.992  7.973  8.067                0.664  1.107  0.745  0.735
B           7.170  9.765  9.279  9.199                0.760  1.108  0.806  0.803
```