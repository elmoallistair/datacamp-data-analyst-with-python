## Removing missing values

Now that you know there are some missing values in your DataFrame, you have a few options to deal with them. One way is to remove them from the dataset completely. In this exercise, you'll remove missing values by removing all rows that contain missing values.

`pandas` has been imported as `pd` and `avocados_2016` is available.

<hr>

**Instructions**
* Remove the rows of `avocados_2016` that contain missing values and store the remaining rows in `avocados_complete`.
* Verify that all missing values have been removed from `avocados_complete`. Calculate each columns has any NAs, and print.

## Script
```
# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())
```

## Output
```
<script.py> output:
    date               False
    avg_price          False
    total_sold         False
    small_sold         False
    large_sold         False
    xl_sold            False
    total_bags_sold    False
    small_bags_sold    False
    large_bags_sold    False
    xl_bags_sold       False
    dtype: bool
```