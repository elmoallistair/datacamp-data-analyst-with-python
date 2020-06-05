## Subsetting rows by categorical variables

Subsetting data based on a categorical variable often involves using the "or" operator (`|`) to select rows from multiple categories. This can get tedious when you want all states in one of three different regions, for example. Instead, use the `.isin()` method, which will allow you to tackle this problem by writing one condition instead of three separate ones.

```
colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]
```

`homelessness` is available and `pandas` is loaded as `pd`.

<hr>

**Instructions 1/2**

Filter `homelessness` for cases where the USA census region is "South Atlantic" or it is "Mid-Atlantic", assigning to `south_mid_atlantic`. *View the printed result*.

**Instructions 2/2**

Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness. View the printed result.

## Script
```
# Subset for rows in South Atlantic or Mid-Atlantic regions
regions = ["South Atlantic", "Mid-Atlantic"]
south_mid_atlantic = homelessness[(homelessness["region"].isin(regions))]

# See the result
print(south_mid_atlantic)
```
```
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[(homelessness["state"].isin(canu))]

# See the result
print(mojave_homelessness)
```

## Output
```
            region                 state  individuals  family_members  state_pop
7   South Atlantic              Delaware        708.0           374.0     965479
8   South Atlantic  District of Columbia       3770.0          3134.0     701547
9   South Atlantic               Florida      21443.0          9587.0   21244317
10  South Atlantic               Georgia       6943.0          2556.0   10511131
20  South Atlantic              Maryland       4914.0          2230.0    6035802
30    Mid-Atlantic            New Jersey       6048.0          3350.0    8886025
32    Mid-Atlantic              New York      39827.0         52070.0   19530351
33  South Atlantic        North Carolina       6451.0          2817.0   10381615
38    Mid-Atlantic          Pennsylvania       8163.0          5349.0   12800922
40  South Atlantic        South Carolina       3082.0           851.0    5084156
46  South Atlantic              Virginia       3928.0          2047.0    8501286
48  South Atlantic         West Virginia       1021.0           222.0    1804291
```
```
      region       state  individuals  family_members  state_pop
2   Mountain     Arizona       7259.0          2606.0    7158024
4    Pacific  California     109008.0         20964.0   39461588
28  Mountain      Nevada       7058.0           486.0    3027341
44  Mountain        Utah       1904.0           972.0    3153550
```