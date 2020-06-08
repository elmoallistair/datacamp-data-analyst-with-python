## and, or, not (1)

A boolean is either `1` or `0`, `True` or `False`. With boolean operators such as `and`, `or` and `not`, you can combine these booleans to perform more advanced queries on your data.

In the sample code on the right, two variables are defined: `my_kitchen` and `your_kitchen`, representing areas.

**Instructions**
* Write Python expressions, wrapped in a `print()` function, to check whether:
  * `my_kitchen` is bigger than 10 and smaller than 18.
  * `my_kitchen` is smaller than 14 or bigger than 17.
  * double the area of `my_kitchen` is smaller than triple the area of `your_kitchen`.

## Script
```
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen*2 < your_kitchen*3)
```

## Output
```
<script.py> output:
    False
    True
    True
```