## Load a DataFrame

A ransom note was left at the scene of Bayes' kidnapping. Eventually, we'll want to analyze the frequency with which each letter occurs in the note, to help us identify the kidnapper. For now, we just need to load the data from `ransom.csv` into Python.

We'll load the data into a DataFrame, a special *data type* from the `pandas` module. It represents spreadsheet-like data (something with rows and columns).

We can create a DataFrame from a CSV (comma-separated value) file by using the function `pd.read_csv`.

<hr>

**Instructions**
* Use `pd.read_csv` to load data from a CSV file called `ransom.csv`. This file represents the frequency of each letter in the ransom note for Bayes.

## Script
```
# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)
```

## Output
```
<script.py> output:
        letter_index letter  frequency
    0              1      A       7.38
    1              2      B       1.09
    2              3      C       2.46
    3              4      D       4.10
    4              5      E      12.84
    5              6      F       1.37
    6              7      G       1.09
    7              8      H       3.55
    8              9      I       7.65
    9             10      J       0.00
    10            11      K       3.01
    11            12      L       3.28
    12            13      M       2.46
    13            14      N       7.38
    14            15      O       6.83
    15            16      P       7.65
    16            17      Q       0.00
    17            18      R       4.92
    18            19      S       4.10
    19            20      T       6.28
    20            21      U       4.37
    21            22      V       1.09
    22            23      W       2.46
    23            24      X       0.00
    24            25      Y       4.64
    25            26      Z       0.00
```