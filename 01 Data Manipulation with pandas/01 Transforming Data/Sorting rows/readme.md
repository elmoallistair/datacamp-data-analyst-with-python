## Sorting rows

Finding interested bits of data in a DataFrame is often easier if you change the order of the rows. You can sort the rows by passing a column name to .sort_values().

In cases where rows have the same value (this is common if you sort on a categorical variable), you may wish to break the ties by sorting on another column. You can sort on multiple columns in this way by passing a list of column names.

| Sort on ...      | Syntax                                   |
|------------------|------------------------------------------|
| One column       | `df.sort_values("breed")`                |
| Multiple columns | `df.sort_values(["breed", "weight_kg"])` |

By combining `.sort_values()` with `.head()`, you can answer questions in the form, "What are the top cases where...?".

`homelessness` is available and `pandas` is loaded as `pd`.

> **Instructions (1/3)**
> * Sort `homelessness` by the number of homeless individuals, from smallest to largest, and save this as `homelessness_ind`.
> * Print the head of the sorted DataFrame.
>
> **script.py**
> ```
> # Sort homelessness by individual
> homelessness_ind = homelessness.sort_values("individuals")
>
> # Print the top few rows
> print(homelessness_ind.head())
> ```
>
> **Output**
> ```
>                 region         state  individuals  family_members  state_pop
> 50            Mountain       Wyoming        434.0           205.0     577601
> 34  West North Central  North Dakota        467.0            75.0     758080
> 7       South Atlantic      Delaware        708.0           374.0     965479
> 39         New England  Rhode Island        747.0           354.0    1058287
> 45         New England       Vermont        780.0           511.0     624358
> ```

> **Instructions (2/3)**
> * Sort `homelessness` by the number of homeless family members in descending order, and save this as `homelessness_fam`.
> * Print the head of the sorted DataFrame.
>
> **script.py**
> ```
> # Sort homelessness by descending family members
> homelessness_fam = homelessness.sort_values("family_members", ascending=False)
>
> # Print the top few rows
> print(homelessness_fam.head())
> ```
>
> **Output**
> ```
>                 region          state  individuals  family_members  state_pop
> 32        Mid-Atlantic       New York      39827.0         52070.0   19530351
> 4              Pacific     California     109008.0         20964.0   39461588
> 21         New England  Massachusetts       6811.0         13257.0    6882635
> 9       South Atlantic        Florida      21443.0          9587.0   21244317
> 43  West South Central          Texas      19199.0          6111.0   28628666
> ```

> **Instructions (3/3)**
> * Sort `homelessness` first by region (ascending), and then by number of family members (descending). Save this as `homelessness_reg_fam`.
> * Print the head of the sorted DataFrame.
>
> **script.py**
> ```
> # Sort homelessness by region, then descending family members
> homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])
>
> # Print the top few rows
> print(homelessness_reg_fam.head())
> ```
>
> **Output**
> ```
>                 region      state  individuals  family_members  state_pop
> 13  East North Central   Illinois       6752.0          3891.0   12723071
> 35  East North Central       Ohio       6929.0          3320.0   11676341
> 22  East North Central   Michigan       5209.0          3142.0    9984072
> 49  East North Central  Wisconsin       2740.0          2167.0    5807406
> 14  East North Central    Indiana       3776.0          1482.0    6695497
> ```