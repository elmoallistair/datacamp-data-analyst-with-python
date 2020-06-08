## Random float

Randomness has many uses in science, art, statistics, cryptography, gaming, gambling, and other fields. You're going to use randomness to simulate a game.

All the functionality you need is contained in the `random` package, a sub-package of `numpy`. In this exercise, you'll be using two functions from this package:

* `seed()`: sets the random seed, so that your results are reproducible between simulations. As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.
* `rand()`: if you don't specify any arguments, it generates a random float between zero and one.

<hr>

**Instructions**
* Import `numpy` as `np`.
* Use `seed()` to set the seed; as an argument, pass 123.
* Generate your first random float with` rand()` and print it out.

## Script
```
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())
```

## Output
```
<script.py> output:
    0.6964691855978616
```