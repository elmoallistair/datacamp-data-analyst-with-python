## Reading DataFrames from multiple files in a loop

As you saw in the video, loading data from multiple files into DataFrames is more efficient in a *loop* or a *list comprehension*.

Notice that this approach is not restricted to working with CSV files. That is, even if your data comes in other formats, as long as pandas has a suitable data import function, you can apply a loop or comprehension to generate a list of DataFrames imported from the source files.

Here, you'll continue working with [The Guardian's Olympic medal dataset](https://www.theguardian.com/sport/datablog/2012/jun/25/olympic-medal-winner-list-data).

<hr>

**Instructions**
* Create a list of file names called `filenames` with three strings `'Gold.csv'`, `'Silver.csv'`, & `'Bronze.csv'`. This has been done for you.
* Use a `for` loop to create another list called `dataframes` containing the three DataFrames loaded from `filenames`:
    * Iterate over `filenames`.
    * Read each CSV file in `filenames` into a DataFrame and append it to `dataframes` by using `pd.read_csv()` inside a call to `.append()`.
* Print the first 5 rows of the first DataFrame of the list `dataframes`. This has been done for you, so hit 'Submit Answer' to see the results.

## Script
```
# Import pandas
import pandas as pd

# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv(filename))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())
```

## Output
```
<script.py> output:
       NOC         Country   Total
    0  USA   United States  2088.0
    1  URS    Soviet Union   838.0
    2  GBR  United Kingdom   498.0
    3  FRA          France   378.0
    4  GER         Germany   407.0
```