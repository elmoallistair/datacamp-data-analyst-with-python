## Loop over a list

Have another look at the `for` loop that Hugo showed in the video:

> ```
> fam = [1.73, 1.68, 1.71, 1.89]
> for height in fam :
>     print(height)
> ```

As usual, you simply have to indent the code with 4 spaces to tell Python which code should be executed in the `for` loop.

The `areas` variable, containing the area of different rooms in your house, is already defined.

<hr>

**Instructions**
* Write a `for` loop that iterates over all elements of the `areas` list and prints out every element separately.

## Script
```
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for element in areas:
    print(element)
```

## Output
```
<script.py> output:
    11.25
    18.0
    20.0
    10.75
    9.5
```