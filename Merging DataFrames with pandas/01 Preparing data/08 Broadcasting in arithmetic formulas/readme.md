## Broadcasting in arithmetic formulas

In this exercise, you'll work with weather data pulled from [wunderground.com](https://www.wunderground.com/). The DataFrame `weather` has been pre-loaded along with `pandas` as `pd`. It has 365 rows (observed each day of the year 2013 in Pittsburgh, PA) and 22 columns reflecting different weather measurements each day.

You'll subset a collection of columns related to temperature measurements in degrees Fahrenheit, convert them to degrees Celsius, and relabel the columns of the new DataFrame to reflect the change of units.

Remember, ordinary arithmetic operators (like `+`, `-`, `*`, and `/`) broadcast scalar values to conforming DataFrames when combining scalars & DataFrames in arithmetic expressions. Broadcasting also works with pandas Series and NumPy arrays.

<hr>

**Instructions**
* Create a new DataFrame `temps_f` by extracting the columns `'Min TemperatureF'`, `'Mean TemperatureF'`, & `'Max TemperatureF'` from weather as a new DataFrame `temps_f`. To do this, pass the relevant columns as a list to weather[].
* Create a new DataFrame `temps_c` from `temps_f` using the formula` (temps_f - 32) * 5/9`.
* Rename the columns of `temps_c` to replace `'F'` with `'C'` using the `.str.replace('F', 'C')` method on `temps_c.columns`.
* Print the first 5 rows of DataFrame `temps_c`. This has been done for you, so hit 'Submit Answer' to see the result!

## Script
```
# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather[['Min TemperatureF','Mean TemperatureF','Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5/9

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = temps_c.columns.str.replace('F','C')

# Print first 5 rows of temps_c
print(temps_c.head())
```

## Output
```
<script.py> output:
                Min TemperatureC  Mean TemperatureC  Max TemperatureC
    Date
    2013-01-01         -6.111111          -2.222222          0.000000
    2013-01-02         -8.333333          -6.111111         -3.888889
    2013-01-03         -8.888889          -4.444444          0.000000
    2013-01-04         -2.777778          -2.222222         -1.111111
    2013-01-05         -3.888889          -1.111111          1.111111
```