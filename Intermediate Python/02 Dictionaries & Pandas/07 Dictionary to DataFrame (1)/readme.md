## Dictionary to DataFrame (1)

Pandas is an open source library, providing high-performance, easy-to-use data structures and data analysis tools for Python. Sounds promising!

The DataFrame is one of Pandas' most important data structures. It's basically a way to store tabular data where you can label the rows and the columns. One way to build a DataFrame is from a dictionary.

In the exercises that follow you will be working with vehicle data from different countries. Each observation corresponds to a country and the columns give information about the number of vehicles per capita, whether people drive left or right, and so on.

Three lists are defined in the script:

* `names`, containing the country names for which data is available.
* `dr`, a list with booleans that tells whether people drive left or right in the corresponding country.
* `cpc`, the number of motor vehicles per 1000 people in the corresponding country.

Each dictionary key is a column label and each value is a list which contains the column elements.

<hr>

**Instructions**
* Import `pandas` as `pd`.
* Use the pre-defined lists to create a dictionary called `my_dict`. There should be three key value pairs:
  * key `'country'` and value `names`.
  * key `'drives_right'` and value `dr`.
  * key `'cars_per_cap'` and value `cpc`.
* Use `pd.DataFrame()` to turn your dict into a DataFrame called `cars`.
* Print out `cars` and see how beautiful it is.

## Script
```
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)
```

## Output
```
<script.py> output:
       cars_per_cap        country  drives_right
    0           809  United States          True
    1           731      Australia         False
    2           588          Japan         False
    3            18          India         False
    4           200         Russia          True
    5            70        Morocco          True
    6            45          Egypt          True
```