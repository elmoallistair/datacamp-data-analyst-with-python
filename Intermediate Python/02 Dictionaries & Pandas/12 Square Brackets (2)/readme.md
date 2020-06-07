## Square Brackets (2)

Square brackets can do more than just selecting columns. You can also use them to get rows, or observations, from a DataFrame. The following call selects the first five rows from the cars DataFrame:

> `cars[0:5]`

The result is another DataFrame containing only the rows you specified.

Pay attention: You can only select rows using square brackets if you specify a slice, like `0:4`. Also, you're using the integer indexes of the rows here, not the row labels!

<hr>

**Instructions**
* Select the first 3 observations from `cars` and print them out.
* Select the fourth, fifth and sixth observation, corresponding to row indexes 3, 4 and 5, and print them out.

## Script
```
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])
```

## Output
```
<script.py> output:
         cars_per_cap        country  drives_right
    US            809  United States          True
    AUS           731      Australia         False
    JPN           588          Japan         False
         cars_per_cap  country  drives_right
    IN             18    India         False
    RU            200   Russia          True
    MOR            70  Morocco          True
```