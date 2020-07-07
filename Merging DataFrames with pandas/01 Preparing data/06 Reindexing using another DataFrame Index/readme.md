## Reindexing using another DataFrame Index

Another common technique is to reindex a DataFrame using the Index of another DataFrame. The DataFrame `.reindex()` method can accept the Index of a DataFrame or Series as input. You can access the Index of a DataFrame with its `.index` attribute.

The [Baby Names Dataset](https://www.data.gov/developers/baby-names-dataset/) from data.gov summarizes counts of names (with genders) from births registered in the US since 1881. In this exercise, you will start with two baby-names DataFrames `names_1981` and `names_1881` loaded for you.

The DataFrames `names_1981` and `names_1881` both have a MultiIndex with levels `name` and `gender` giving unique labels to counts in each row. If you're interested in seeing how the MultiIndexes were set up, `names_1981` and `names_1881` were read in using the following commands:


> ```
> names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'], index_col=(0,1))
> names_1881 = pd.read_csv('names1881.csv', header=None, names=['name','gender','count'], index_col=(0,1))
> ```
>
As you can see by looking at their shapes, which have been printed in the IPython Shell, the DataFrame corresponding to 1981 births is much larger, reflecting the greater diversity of names in 1981 as compared to 1881.

Your job here is to use the DataFrame `.reindex()` and `.dropna()` methods to make a DataFrame `common_names` counting names from 1881 that were still popular in 1981.

<hr>

**Instructions**
* Create a new DataFrame `common_names` by reindexing `names_1981` using the `index` attribute of the DataFrame `names_1881` of older names.
* Print the shape of the new `common_names` DataFrame. This has been done for you. It should be the same as that of `names_1881`.
* Drop the rows of `common_names` that have null counts using the `.dropna()` method. These rows correspond to names that fell out of fashion between 1881 & 1981.
* Print the shape of the reassigned `common_names` DataFrame. This has been done for you, so hit 'Submit Answer' to see the result!

## Script
```
# Import pandas
import pandas as pd

# Reindex names_1981 with index of names_1881: common_names
common_names = names_1981.reindex(names_1881.index)

# Print shape of common_names
print(common_names.shape)

# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)
```

## Output
```
<script.py> output:
    (1935, 1)
    (1587, 1)
```