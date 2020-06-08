## Compare arrays

Out of the box, you can also use comparison operators with Numpy arrays.

Remember `areas`, the list of area measurements for different rooms in your house from *Introduction to Python*? This time there's two Numpy arrays: `my_house` and `your_house`. They both contain the areas for the kitchen, living room, bedroom and bathroom in the same order, so you can compare them.

<hr>

**Instructions**

Using comparison operators, generate boolean arrays that answer the following questions:

* Which areas in `my_house` are greater than or equal to `18`?
* You can also compare two Numpy arrays element-wise. Which areas in `my_house` are smaller than the ones in `your_house`?
* Make sure to wrap both commands in a `print()` statement so that you can inspect the output!


## Script
```
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house <= your_house)
```

## Print
```
<script.py> output:
    [ True  True False False]
    [False  True  True False]
```