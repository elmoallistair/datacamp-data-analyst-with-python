## Read data with a time index

Pandas DataFrame objects can have an index that denotes time. This is useful because Matplotlib recognizes that these measurements represent time and labels the values on the axis accordingly.

In this exercise, you will read data from a CSV file called `climate_change.csv` that contains measurements of CO2 levels and temperatures made on the 6th of every month from 1958 until 2016. You will use Pandas' `read_csv` function.

To designate the index as a `DateTimeIndex`, you will use the `parse_dates` and `index_col` key-word arguments both to parse this column as a variable that contains dates and also to designate it as the index for this DataFrame.

*By the way, if you haven't downloaded it already, check out the [Matplotlib Cheat Sheet](https://datacamp-community-prod.s3.amazonaws.com/28b8210c-60cc-4f13-b0b4-5b4f2ad4790b). It includes an overview of the most important concepts, functions and methods and might come in handy if you ever need a quick refresher!*

<hr>

**Instructions**
* Import the Pandas library as `pd`.
* Read in the data from a CSV file called `'climate_change.csv'` using `pd.read_csv`.
* Use the `parse_dates` key-word argument to parse the `"date"` column as dates.
* Use the `index_col` key-word argument to set the `"date"` column as the index.

## Script
```
# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates=['date'], index_col='date')
```