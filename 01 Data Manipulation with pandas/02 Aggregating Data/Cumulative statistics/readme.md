## Cumulative statistics

Cumulative statistics can also be helpful in tracking summary statistics over time. In this exercise, you'll calculate the cumulative sum and cumulative max of a department's weekly sales, which will allow you to identify what the total sales were so far as well as what the highest weekly sales were so far.

A DataFrame called `sales_1_1` has been created for you, which contains the sales data for department 1 of store 1. `pandas` is loaded as `pd`.

<hr>

**Instructions**

* Sort the rows of sales_1_1 by the date column in ascending order.
* Get the cumulative sum of weekly_sales and add it as a new column of sales_1_1 called cum_weekly_sales.
* Get the cumulative maximum of weekly_sales, and add it as a column called cum_max_sales.
* Print the date, weekly_sales, cum_weekly_sales, and cum_max_sales columns.

> **script.py**
> ```
> # Sort sales_1_1 by date
> sales_1_1 = sales_1_1.sort_values("date")
>
> # Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
> sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()
>
> # Get the cumulative max of weekly_sales, add as cum_max_sales col
> sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()
>
> # See the columns you calculated
> print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
> ```
>
> **Output**
> ```
>          date  weekly_sales  cum_weekly_sales  cum_max_sales
> 0  2010-02-05      24924.50          24924.50       24924.50
> 1  2010-03-05      21827.90          46752.40       24924.50
> 2  2010-04-02      57258.43         104010.83       57258.43
> 3  2010-05-07      17413.94         121424.77       57258.43
> 4  2010-06-04      17558.09         138982.86       57258.43
> 5  2010-07-02      16333.14         155316.00       57258.43
> 6  2010-08-06      17508.41         172824.41       57258.43
> 7  2010-09-03      16241.78         189066.19       57258.43
> 8  2010-10-01      20094.19         209160.38       57258.43
> 9  2010-11-05      34238.88         243399.26       57258.43
> 10 2010-12-03      22517.56         265916.82       57258.43
> 11 2011-01-07      15984.24         281901.06       57258.43
> ```