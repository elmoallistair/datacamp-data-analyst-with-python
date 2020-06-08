## Loop over Numpy array

If you're dealing with a 1D Numpy array, looping over all elements can be as simple as:

> ```
> for x in my_array :
>     ...
> ```

If you're dealing with a 2D Numpy array, it's more complicated. A 2D array is built up of multiple 1D arrays. To explicitly iterate over all separate elements of a multi-dimensional array, you'll need this syntax:

> ```
> for x in np.nditer(my_array) :
>     ...
> ```

Two Numpy arrays that you might recognize from the intro course are available in your Python session: `np_height`, a Numpy array containing the heights of Major League Baseball players, and `np_baseball`, a 2D Numpy array that contains both the heights (first column) and weights (second column) of those players.

<hr>

**Instructions**
* Import the `numpy` package under the local alias `np`.
* Write a `for` loop that iterates over all elements in `np_height` and prints out `"x inches"` for each element, where x is the value in the array.
* Write a `for` loop that visits every element of the `np_baseball` array and prints it out.

## Script
```
# Import numpy as np
import numpy as np

# For loop over np_height
for n in np_height:
    print('{} inches'.format(n))

# For loop over np_baseball
for n in np.nditer(np_baseball):
    print(n)
```