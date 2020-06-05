## Mean and median

Summary statistics are exactly what they sound like - they summarize many numbers in one statistic. For example, mean, median, minimum, maximum, and standard deviation are summary statistics. Calculating summary statistics allows you to get a better sense of your data, even if there's a lot of it.

`sales` is available and `pandas` is loaded as `pd`.

<hr>

**Instructions**

* Explore your new DataFrame first by printing the first few rows of the `sales` DataFrame.
* Print information about the columns in `sales`.
* Print the mean of the `weekly_sales` column.
* Print the median of the `weekly_sales` column.

## Script
```
# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())
```

## Output
```
   store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l unemployment
0      1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8106
1      1    A           1 2010-03-05      21827.90       False          8.056                 0.693         8106
2      1    A           1 2010-04-02      57258.43       False         16.817                 0.718         7808
3      1    A           1 2010-05-07      17413.94       False         22.528                 0.749         7808
4      1    A           1 2010-06-04      17558.09       False         27.050                 0.715         7808
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10774 entries, 0 to 10773
Data columns (total 9 columns):
store                   10774 non-null int64
type                    10774 non-null object
department              10774 non-null int32
date                    10774 non-null datetime64[ns]
weekly_sales            10774 non-null float64
is_holiday              10774 non-null bool
temperature_c           10774 non-null float64
fuel_price_usd_per_l    10774 non-null float64
unemployment            10774 non-null float64
dtypes: bool(1), datetime64[ns](1), float64(4), int32(1), int64(1), object(1)
memory usage: 641.9+ KB
None
23843.95014850566
12049.064999999999
```