## Combining DataFrames from multiple data files

In this exercise, you'll *combine* the three DataFrames from earlier exercises - `gold`, `silver`, & `bronze` - into a single DataFrame called `medals`. The approach you'll use here is clumsy. Later on in the course, you'll see various powerful methods that are frequently used in practice for *concatenating or merging* DataFrames.

Remember, the column labels of each DataFrame are `NOC`, `Country`, and `Total`, where `NOC` is a three-letter code for the name of the country and Total is the number of medals of that type won.

<hr>

**Instructions**
* Construct a `copy` of the DataFrame gold called `medals` using the `.copy()` method.
* Create a list called `new_labels` with entries `'NOC'`, `'Country'`, & `'Gold'`. This is the same as the column labels from `gold` with the column label `'Total'` replaced by `'Gold'`.
* Rename the columns of `medals` by assigning `new_labels` to `medals.columns`.
* Create new columns `'Silver'` and `'Bronze'` in medals using `silver['Total']` & `bronze['Total']`.
* Print the top 5 rows of the final DataFrame `medals`. This has been done for you, so hit 'Submit Answer' to see the result!

## Script
```
# Import pandas
import pandas as pd

# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total'].copy()
medals['Bronze'] = bronze['Total'].copy()

# Print the head of medals
print(medals.head())
```

## Output
```
<script.py> output:
       NOC         Country    Gold  Silver  Bronze
    0  USA   United States  2088.0  1195.0  1052.0
    1  URS    Soviet Union   838.0   627.0   584.0
    2  GBR  United Kingdom   498.0   591.0   505.0
    3  FRA          France   378.0   461.0   475.0
    4  GER         Germany   407.0   350.0   454.0
```