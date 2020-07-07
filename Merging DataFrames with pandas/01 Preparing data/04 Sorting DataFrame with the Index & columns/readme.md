## Sorting DataFrame with the Index & columns

It is often useful to rearrange the sequence of the rows of a DataFrame by *sorting*. You don't have to implement these yourself; the principal methods for doing this are `.sort_index()` and` .sort_values()`.

In this exercise, you'll use these methods with a DataFrame of temperature values indexed by month names. You'll sort the rows alphabetically using the Index and numerically using a column. Notice, for this data, the original ordering is probably most useful and intuitive: the purpose here is for you to understand what the sorting methods do.

<hr>

**Instructions**
* Read `'monthly_max_temp.csv'` into a DataFrame called weather1 with `'Month'` as the index.
* Sort the index of `weather1` in alphabetical order using the `.sort_index()` method and store the result in `weather2`.
* Sort the index of `weather1` in *reverse* alphabetical order by specifying the additional keyword argument `ascending=False` inside `.sort_index()`.
* Use the `.sort_values()` method to sort `weather1` in increasing numerical order according to the *values* of the column `'Max TemperatureF'`.

## Script
```
# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv', index_col='Month')

# Print the head of weather1
print(weather1.head())

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather2.sort_index(ascending=False)

# Print the head of weather3
print(weather3.head())

# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF')

# Print the head of weather4
print(weather4.head())
```

## Output
```
<script.py> output:
           Max TemperatureF
    Month
    Jan                  68
    Feb                  60
    Mar                  68
    Apr                  84
    May                  88
           Max TemperatureF
    Month
    Apr                  84
    Aug                  86
    Dec                  68
    Feb                  60
    Jan                  68
           Max TemperatureF
    Month
    Sep                  90
    Oct                  84
    Nov                  72
    May                  88
    Mar                  68
           Max TemperatureF
    Month
    Feb                  60
    Jan                  68
    Mar                  68
    Dec                  68
    Nov                  72
```