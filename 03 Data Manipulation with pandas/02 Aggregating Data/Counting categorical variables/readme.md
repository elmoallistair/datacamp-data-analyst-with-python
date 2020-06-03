## Counting categorical variables

Counting is a great way to get an overview of your data and to spot curiosities that you might not notice otherwise. In this exercise, you'll count the number of each type of store and the number of each department number.

The `stores` and `departments` DataFrames you created in the last exercise are available and `pandas` is imported as `pd`.

<hr>

**Instructions**

* Count the number of stores of each store type.
* Count the proportion of stores of each store type.
* Count the number of different department numbers, sorting the counts in descending order.
* Count the proportion of different department numbers, sorting the proportions in descending order.

> **script.py**
> ```
> # Count the number of stores of each type
> store_counts = stores["store_type"].value_counts()
> print(store_counts)
> 
> # Get the proportion of stores of each type
> store_props = stores["store_type"].value_counts(normalize=True)
> print(store_props)
> 
> # Count the number of each department number and sort
> dept_counts_sorted = departments["department_num"].value_counts(sort=True)
> print(dept_counts_sorted)
> 
> # Get the proportion of departments of each number and sort
> dept_props_sorted = departments["department_num"].value_counts(sort=True, normalize=True)
> print(dept_props_sorted)
> ```
> 
> **Output**
> ```
> A    11
> B     1
> Name: store_type, dtype: int64
> 
> A    0.917
> B    0.083
> Name: store_type, dtype: float64
> 
> 41    12
> 30    12
> 23    12
> 24    12
> 25    12
>       ..
> 37    10
> 48     8
> 50     6
> 39     4
> 43     2
> Name: department_num, Length: 80, dtype: int64
> 
> 41    0.013
> 30    0.013
> 23    0.013
> 24    0.013
> 25    0.013
>       ...
> 37    0.011
> 48    0.009
> 50    0.006
> 39    0.004
> 43    0.002
> Name: department_num, Length: 80, dtype: float64
> ```