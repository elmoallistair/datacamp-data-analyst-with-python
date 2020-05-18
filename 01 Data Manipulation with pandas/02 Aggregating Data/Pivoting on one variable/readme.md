## Pivoting on one variable

Pivot tables are the standard way of aggregating data in spreadsheets. In pandas, pivot tables are essentially just another way of performing grouped calculations. That is, the `.pivot_table()` method is just an alternative to `.groupby()`.

In this exercise, you'll perform calculations using `.pivot_table()` to replicate the calculations you performed in the last lesson using `.groupby()`.

`sales` is available and `pandas` is imported as `pd`.

**Instructions 1/3**

> * Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type.
>
> **script.py**
> ```
> # Pivot for mean weekly_sales for each store type
> mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")
>
> # Print mean_sales_by_type
> print(mean_sales_by_type)
> ```
>
> **Output**
> ```
>       weekly_sales
> type
> A        23674.667
> B        25696.678
> ```

**Instructions 2/3**

* Get the mean and median (using NumPy functions) of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type.

> **script.py**
> ```
> # Import NumPy as np
> import numpy as np
>
> # Pivot for mean and median weekly_sales for each store type
> mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])
>
> # Print mean_med_sales_by_type
> print(mean_med_sales_by_type)
> ```
>
> **Output**
> ```
>              mean       median
>      weekly_sales weekly_sales
> type
> A       23674.667     11943.92
> B       25696.678     13336.08
> ```

**Instructions 3/3**

* Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday.

> **script.py**
> ```
> # Pivot for mean weekly_sales by store type and holiday
> mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")
> 
> # Print mean_sales_by_type_holiday
> print(mean_sales_by_type_holiday)
> ```
> 
> **Output**
> ```
> is_holiday      False    True
> type
> A           23768.584  590.045
> B           25751.981  810.705
> ```