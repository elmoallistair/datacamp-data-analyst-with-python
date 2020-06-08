## Driving right (2)

The code in the previous example worked fine, but you actually unnecessarily created a new variable `dr`. You can achieve the same result without this intermediate variable. Put the code that computes `dr` straight into the square brackets that select observations from `cars`.

<hr>

**Instructions**
* Convert the code on the right to a one-liner that calculates the variable `sel` as before.

## Script
```
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

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