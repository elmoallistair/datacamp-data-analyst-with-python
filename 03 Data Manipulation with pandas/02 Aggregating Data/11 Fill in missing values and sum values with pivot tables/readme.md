## Fill in missing values and sum values with pivot tables

The `.pivot_table()` method has several useful arguments, including `fill_value` and `margins`.

* `fill_value` replaces missing values with a real value (known as imputation). What to replace missing values with is a topic big enough to have its own course [(Dealing with Missing Data in Python)](https://www.datacamp.com/courses/dealing-with-missing-data-in-python), but the simplest thing to do is to substitute a dummy value.
* `margins` is a shortcut for when you pivoted by two variables, but also wanted to pivot by each of those variables separately: it gives the row and column totals of the pivot table contents.

In this exercise, you'll practice using these arguments to up your pivot table skills, which will help you crunch numbers more efficiently!

`sales` is available and `pandas` is imported as `pd`.

<hr>

**Instructions 1/2**

Print the mean `weekly_sales` by `department` and `type`, filling in any missing values with `0`.

**Instructions 2/2**

Print the mean `weekly_sales` by `department` and `type`, filling in any missing values with `0` and summing all rows and columns.

## Script
```
# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0))
```
```
# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, aggfunc=sum, margins=True))
```

## Output
```
type                 A           B
department
1            30961.725   44050.627
2            67600.159  112958.527
3            17160.003   30580.655
4            44285.399   51219.654
5            34821.011   63236.875
...                ...         ...
95          123933.787   77082.103
96           21367.043    9528.538
97           28471.267    5828.873
98           12875.423     217.428
99             379.124       0.000

[80 rows x 2 columns]
```
```
type                A          B        All
department
1           4.087e+06  5.286e+05  4.616e+06
2           8.923e+06  1.356e+06  1.028e+07
3           2.265e+06  3.670e+05  2.632e+06
4           5.846e+06  6.146e+05  6.460e+06
5           4.596e+06  7.588e+05  5.355e+06
...               ...        ...        ...
96          2.692e+06  1.143e+05  2.807e+06
97          3.758e+06  6.995e+04  3.828e+06
98          1.700e+06  2.609e+03  1.702e+06
99          4.663e+04  0.000e+00  4.663e+04
All         2.337e+08  2.318e+07  2.569e+08

[81 rows x 3 columns]
```