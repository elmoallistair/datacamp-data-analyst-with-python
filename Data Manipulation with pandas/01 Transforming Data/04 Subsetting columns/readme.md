## Subsetting columns

When working with data, you may not need all of the variables in your dataset. Square-brackets (`[]`) can be used to select only the columns that matter to you in an order that makes sense to you. To select only `"col_a"` of the DataFrame `df`, use

```
df["col_a"]
```

To select `"col_a"` and `"col_b"` of `df`, use

```
df[["col_a", "col_b"]]
```

`homelessness` is available and `pandas` is loaded as `pd`.

<hr>

**Instructions 1/3**

* Create a DataFrame called `individuals` that contains only the `individuals` column of `homelessness`.
* Print the head of the result.

**Instructions 2/3**

* Create a DataFrame called `state_fam` that contains only the `state` and `family_members` columns of `homelessness`, in that order.
* Print the head of the result.

**Instructions 3/3**

* Create a DataFrame called `ind_state` that contains the `individuals` and `state` columns of `homelessness`, in that order.
* Print the head of the result.


## Script
```
# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())
```
```
# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

# Print the head of the result
print(state_fam.head())
```
```
# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(ind_state.head())
```

## Output
```
0      2570.0
1      1434.0
2      7259.0
3      2280.0
4    109008.0
Name: individuals, dtype: float64
```
```
        state  family_members
0     Alabama           864.0
1      Alaska           582.0
2     Arizona          2606.0
3    Arkansas           432.0
4  California         20964.0
```
```
   individuals       state
0       2570.0     Alabama
1       1434.0      Alaska
2       7259.0     Arizona
3       2280.0    Arkansas
4     109008.0  California
```