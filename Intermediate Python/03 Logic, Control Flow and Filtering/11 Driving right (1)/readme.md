## Driving right (1)

Remember that `cars` dataset, containing the cars per 1000 people (`cars_per_cap`) and whether people drive right (`drives_right`) for different countries (`country`)? The code that imports this data in CSV format into Python as a DataFrame is available on the right.

In the video, you saw a step-by-step approach to filter observations from a DataFrame based on boolean arrays. Let's start simple and try to find all observations in `cars` where `drives_right` is `True`.

`drives_right` is a boolean column, so you'll have to extract it as a Series and then use this boolean Series to select observations from `cars`.

<hr>

**Instructions**
* Extract the `drives_right` column as a *Pandas Series* and store it as `dr`.
* Use `dr`, a boolean Series, to subset the `cars` DataFrame. Store the resulting selection in sel.
* Print `sel`, and assert that `drives_right` is `True` for all observations.

## Script
```
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)
```

## Output
```
<script.py> output:
         cars_per_cap        country  drives_right
    US            809  United States          True
    RU            200         Russia          True
    MOR            70        Morocco          True
    EG             45          Egypt          True
```