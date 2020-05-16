## Inspecting a DataFrame

When you get a new DataFrame to work with, the first thing you need to do is explore it and see what it contains. There are several useful methods and attributes for this.

* `.head()` returns the first few rows (the “head” of the DataFrame.
* `.info()` shows information on each of the columns, such as the data type and number of missing values.
* `.shape` returns the number of rows and columns of the DataFrame.
* `.describe()` calculates a few summary statistics for each column.

`homelessness` is a DataFrame containing estimates of homelessness in each U.S. state in 2018. The individual column is the number of homeless `individuals` not part of a family with children. The `family_members` column is the number of homeless individuals part of a family with children. The `state_pop` column is the state's total population.

`pandas` is imported for you.

<hr>

**Instructions**
* Print the head of the homelessness data
* Print information about homelessness
* Print the shape of homelessness
* Print a description of homelessness

**script.py**
```
# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())
```

**Output**
```
               region       state  individuals  family_members  state_pop
0  East South Central     Alabama       2570.0           864.0    4887681
1             Pacific      Alaska       1434.0           582.0     735139
2            Mountain     Arizona       7259.0          2606.0    7158024
3  West South Central    Arkansas       2280.0           432.0    3009733
4             Pacific  California     109008.0         20964.0   39461588
```