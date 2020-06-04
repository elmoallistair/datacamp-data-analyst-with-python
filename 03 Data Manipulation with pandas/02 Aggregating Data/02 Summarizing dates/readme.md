## Summarizing dates

Summary statistics can also be calculated on date columns which have values with the data type `datetime64`. Some summary statistics — like mean — don't make a ton of sense on dates, but others are super helpful, for example minimum and maximum, which allow you to see what time range your data covers.

`sales` is available and `pandas` is loaded as `pd`.

<hr>

**Instructions**

* Print the maximum of the date column.
* Print the minimum of the date column.

## Script
```
# Print the maximum of the date column
print(sales["date"].max())

# Print the minimum of the date column
print(sales["date"].min())
```

## Output
```
2012-10-26 00:00:00
2010-02-05 00:00:00
```