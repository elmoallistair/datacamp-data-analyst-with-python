## Cars per capita (1)

Let's stick to the `cars` data some more. This time you want to find out which countries have a high *cars per capita* figure. In other words, in which countries do many people have a car, or maybe multiple cars.

Similar to the previous example, you'll want to build up a boolean Series, that you can then use to subset the `cars` DataFrame to select certain observations. If you want to do this in a one-liner, that's perfectly fine!

<hr>

**Instructions**
* Select the `cars_per_cap` column from `cars` as a Pandas Series and store it as `cpc`.
* Use `cpc` in combination with a comparison operator and `500`. You want to end up with a boolean Series that's `True` if the corresponding country has a `cars_per_cap` of more than `500` and `False` otherwise. Store this boolean Series as `many_cars`.
* Use `many_cars` to subset `cars`, similar to what you did before. Store the result as `car_maniac`.
* Print out `car_maniac` to see if you got it right.

## Script
```
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
many_cars = cars['cars_per_cap'] > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)
```

## Output
```
<script.py> output:
         cars_per_cap        country  drives_right
    US            809  United States          True
    AUS           731      Australia         False
    JPN           588          Japan         False
```