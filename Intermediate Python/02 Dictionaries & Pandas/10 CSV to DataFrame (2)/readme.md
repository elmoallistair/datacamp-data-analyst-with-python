## CSV to DataFrame (2)

Your `read_csv()` call to import the CSV data didn't generate an error, but the output is not entirely what we wanted. The row labels were imported as another column without a name.

Remember `index_col`, an argument of `read_csv()`, that you can use to specify which column in the CSV file should be used as a row label? Well, that's exactly what you need here!

Python code that solves the previous exercise is already included; can you make the appropriate changes to fix the data import?

<hr>

**Instructions**
* Run the code with *Run Code* and assert that the first column should actually be used as row labels.
* Specify the `index_col` argument inside `pd.read_csv()`: set it to `0`, so that the first column is used as row labels.
* Has the printout of `cars` improved now?

## Script
```
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)
```

## Output
```
<script.py> output:
         cars_per_cap        country  drives_right
    US            809  United States          True
    AUS           731      Australia         False
    JPN           588          Japan         False
    IN             18          India         False
    RU            200         Russia          True
    MOR            70        Morocco          True
    EG             45          Egypt          True
```