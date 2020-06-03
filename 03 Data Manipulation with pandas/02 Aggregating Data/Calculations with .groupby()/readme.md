## Calculations with .groupby()

The `.groupby()` method makes life much easier. In this exercise, you'll perform the same calculations as last time, except you'll use the `.groupby()` method. You'll also perform calculations on data grouped by two variables to see if sales differs by store type depending on if it's a holiday week or not.

`sales` is available and `pandas` is loaded as `pd`.

**Instructions 1/2**

* Group sales by `"type"`, take the sum of `"weekly_sales"`, and store as `sales_by_type`.
* Calculate the proportion of sales at each store type by dividing by the sum of `sales_by_type`. Assign to `sales_propn_by_type`.

> **script.py**
> ```
> # Group by type; calc total weekly sales
> sales_by_type = sales.groupby("type")["weekly_sales"].sum()
> 
> # Get proportion for each type
> sales_propn_by_type = sales_by_type[["A", "B"]] / sales_by_type.sum()
> print(sales_propn_by_type)
> ```
> 
> **Output**
> ```
> type
> A    0.91
> B    0.09
> Name: weekly_sales, dtype: float64
> ```

**Instructions 1/2**

* Group sales by `"type"` and `"is_holiday"`, take the sum of `weekly_sales`, and store as `sales_by_holiday_type`.

> **script.py**
> ```
> # From previous step
> sales_by_type = sales.groupby("type")["weekly_sales"].sum()
>
> # Group by type and is_holiday; calc total weekly sales
> sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
> print(sales_by_type_is_holiday)
> ```
>
> **Output**
> ```
> type  is_holiday
> A     False         2.337e+08
>       True          2.360e+04
> B     False         2.318e+07
>       True          1.621e+03
> Name: weekly_sales, dtype: float64
> ```