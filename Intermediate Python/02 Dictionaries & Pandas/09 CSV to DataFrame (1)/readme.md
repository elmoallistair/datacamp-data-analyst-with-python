## CSV to DataFrame (1)

Putting data in a dictionary and then building a DataFrame works, but it's not very efficient. What if you're dealing with millions of observations? In those cases, the data is typically available as files with a regular structure. One of those file types is the CSV file, which is short for "comma-separated values".

To import CSV data into Python as a Pandas DataFrame you can use `read_csv()`.

Let's explore this function with the same cars data from the previous exercises. This time, however, the data is available in a CSV file, named `cars.csv`. It is available in your current working directory, so the path to the file is simply `'cars.csv'`.

<hr>

**Instructions**
* To import CSV files you still need the `pandas` package: import it as `pd`.
* Use `pd.read_csv()` to import `cars.csv` data as a DataFrame. Store this dataframe as `cars`.
* Print out `cars`. Does everything look OK?

## Script
```
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)
```

## Output
```
<script.py> output:
      Unnamed: 0  cars_per_cap        country  drives_right
    0         US           809  United States          True
    1        AUS           731      Australia         False
    2        JPN           588          Japan         False
    3         IN            18          India         False
    4         RU           200         Russia          True
    5        MOR            70        Morocco          True
    6         EG            45          Egypt          True
```