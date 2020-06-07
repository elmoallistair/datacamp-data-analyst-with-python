## Motivation for dictionaries

To see why dictionaries are useful, have a look at the two lists defined on the right. `countries` contains the names of some European countries. `capitals` lists the corresponding names of their capital.

<hr>

**Instructions**

* Use the `index()` method on `countries` to find the index of `'germany'`. Store this index as `ind_ger`.
* Use `ind_ger` to access the capital of Germany from the `capitals` list. Print it out.

## Script
```
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index('germany')

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])
```

## Output
```
<script.py> output:
    berlin
```