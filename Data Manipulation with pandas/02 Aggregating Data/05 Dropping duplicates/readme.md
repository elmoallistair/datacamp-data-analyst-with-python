## Dropping duplicates

Removing duplicates is an essential skill to get accurate counts, because often you don't want to count the same thing multiple times. In this exercise, you'll create some new DataFrames using unique values from `sales`.

`sales` is available and `pandas` is imported as `pd`.

<hr>

**Instructions**

* Remove rows of `sales` with duplicate pairs of `store` and `type` and save as `store_types` and print the head.
* Remove rows of `sales` with duplicate pairs of `store` and `department` and save as `store_depts` and print the head.
* Subset the rows that are holiday weeks, and drop the duplicate `dates`, saving as `holiday_dates`.
Select the date column of `holiday_dates`, and print.

## Script
```
# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset = ["store", "type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset = ["store", "department"])
print(store_depts.head())

# Subset the rows that are holiday weeks and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset = "date")

# Print date col of holiday_dates
print(holiday_dates)
```

## Output
```
      store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
0         1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
901       2    A           1 2010-02-05      35034.06       False          4.550                 0.679         8.324
1798      4    A           1 2010-02-05      38724.42       False          6.533                 0.686         8.623
2699      6    A           1 2010-02-05      25619.00       False          4.683                 0.679         7.259
3593     10    B           1 2010-02-05      40212.84       False         12.411                 0.782         9.765
    store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
0       1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
12      1    A           2 2010-02-05      50605.27       False          5.728                 0.679         8.106
24      1    A           3 2010-02-05      13740.12       False          5.728                 0.679         8.106
36      1    A           4 2010-02-05      39954.04       False          5.728                 0.679         8.106
48      1    A           5 2010-02-05      32229.38       False          5.728                 0.679         8.106
      store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
498       1    A          45 2010-09-10         11.47        True         25.939                 0.678         7.787
691       1    A          77 2011-11-25       1431.00        True         15.633                 0.855         7.866
2315      4    A          47 2010-02-12        498.00        True         -1.756                 0.680         8.623
6735     19    A          39 2012-09-07         13.41        True         22.333                 1.077         8.193
6810     19    A          47 2010-12-31       -449.00        True         -1.861                 0.881         8.067
6815     19    A          47 2012-02-10         15.00        True          0.339                 1.011         7.943
6820     19    A          48 2011-09-09        197.00        True         20.156                 1.038         7.806
```