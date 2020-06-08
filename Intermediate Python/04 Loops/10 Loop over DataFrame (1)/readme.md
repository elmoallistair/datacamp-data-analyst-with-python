# Loop over DataFrame (1)

Iterating over a Pandas DataFrame is typically done with the `iterrows()` method. Used in a `for` loop, every observation is iterated over and on every iteration the row label and actual row contents are available:

> ```
> for lab, row in brics.iterrows() :
>     ...
> ```

In this and the following exercises you will be working on the `cars` DataFrame. It contains information on the cars per capita and whether people drive right or left for seven countries in the world.

<hr>

**Instructions**
* Write a `for` loop that iterates over the rows of `cars` and on each iteration perform two `print()` calls: one to print out the row label and one to print out all of the rows contents.

## Script
```
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)
```

## Output
```
<script.py> output:
    US
    cars_per_cap              809
    country         United States
    drives_right             True
    Name: US, dtype: object
    AUS
    cars_per_cap          731
    country         Australia
    drives_right        False
    Name: AUS, dtype: object
    JPN
    cars_per_cap      588
    country         Japan
    drives_right    False
    Name: JPN, dtype: object
    IN
    cars_per_cap       18
    country         India
    drives_right    False
    Name: IN, dtype: object
    RU
    cars_per_cap       200
    country         Russia
    drives_right      True
    Name: RU, dtype: object
    MOR
    cars_per_cap         70
    country         Morocco
    drives_right       True
    Name: MOR, dtype: object
    EG
    cars_per_cap       45
    country         Egypt
    drives_right     True
    Name: EG, dtype: object
```