## loc and iloc (1)

With `loc` and `iloc` you can do practically any data selection operation on DataFrames you can think of. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. `iloc` is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

Try out the following commands in the IPython Shell to experiment with loc and iloc to select observations. Each pair of commands here gives the same result.

> `cars.loc['RU']`\
> `cars.iloc[4]`
>
> `cars.loc[['RU']]`\
> `cars.iloc[[4]]`
>
> `cars.loc[['RU', 'AUS']]`\
> `cars.iloc[[4, 1]]`

As before, code is included that imports the cars data as a Pandas DataFrame.

<hr>

**Instructions**
* Use `loc` or `iloc` to select the observation corresponding to Japan as a Series. The label of this row is `JPN`, the index is `2`. Make sure to print the resulting Series.
* Use `loc` or `iloc` to select the observations for Australia and Egypt as a DataFrame. You can find out about the labels/indexes of these rows by inspecting `cars` in the IPython Shell. Make sure to print the resulting DataFrame.

## Script
```
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])
```

## Output
```
<script.py> output:
    cars_per_cap      588
    country         Japan
    drives_right    False
    Name: JPN, dtype: object
         cars_per_cap    country  drives_right
    AUS           731  Australia         False
    EG             45      Egypt          True
```