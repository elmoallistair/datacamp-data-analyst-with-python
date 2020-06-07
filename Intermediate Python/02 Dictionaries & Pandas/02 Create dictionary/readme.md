## Create dictionary

The `countries` and `capitals` lists are again available in the script. It's your job to convert this data to a dictionary where the country names are the keys and the capitals are the corresponding values. As a refresher, here is a recipe for creating a dictionary:

> ```
> my_dict = {
>    "key1":"value1",
>    "key2":"value2",
> }
> ```

In this recipe, both the keys and the values are strings. This will also be the case for this exercise.

<hr>

**Instructions**
* With the strings in `countries` and `capitals`, create a dictionary called `europe` with 4 key:value pairs. Beware of capitalization! Make sure you use lowercase characters everywhere.
* Print out `europe` to see if the result is what you expected.

## Script
```
# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = { 'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print europe
print(europe)
```

## Output
```
<script.py> output:
    {'spain': 'madrid', 'norway': 'oslo', 'france': 'paris', 'germany': 'berlin'}
```