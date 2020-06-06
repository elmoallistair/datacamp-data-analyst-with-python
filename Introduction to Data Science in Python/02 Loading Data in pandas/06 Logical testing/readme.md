## Logical testing

Let's practice writing logical statements and displaying the output.

Recall that we use the following operators:

* `==` tests that two values are equal.
* `!=` tests that two values are not equal.
* `>` and `<` test that greater than or less than, respectively.
* `>=` and `<=` test greater than or equal to or less than or equal to, respectively.

<hr>

**Instructions 1/3**
* The variable `height_inches` represents the height of a suspect. Is `height_inches` greater than `70` inches?

**Instructions 2/3**
* The variable `plate1` represents a license plate number of a suspect. Is it equal to `FRQ123`?

**Instructions 3/3**
* The variable `fur_color` represents the color of Bayes' fur. Check that `fur_color` is not equal to `"brown"`.


## Script
```
# Is height_inches greater than 70 inches?
print(height_inches > 70)

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")

# Is fur_color not equal to "brown"?
print(fur_color != "brown")
```

## Output
```
<script.py> output:
    False
    True
    True
```