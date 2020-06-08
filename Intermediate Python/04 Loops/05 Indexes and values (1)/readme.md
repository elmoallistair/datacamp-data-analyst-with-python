## Indexes and values (1)

Using a `for` loop to iterate over a list only gives you access to every list element in each run, one after the other. If you also want to access the index information, so where the list element you're iterating over is located, you can use `enumerate()`.

As an example, have a look at how the `for` loop from the video was converted:

> ```
> fam = [1.73, 1.68, 1.71, 1.89]
> for index, height in enumerate(fam) :
>     print("person " + str(index) + ": " + str(height))
> ```

<hr>

**Instructions**
* Adapt the `for` loop in the sample code to use `enumerate()` and use two iterator variables.
* Update the `print()` statement so that on each run, a line of the form `"room x: y"` should be printed, where x is the index of the list element and y is the actual list element, i.e. the area. Make sure to print out this exact string, with the correct spacing.

## Script
```
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for idx, a in enumerate(areas) :
    print("room {}: {}".format(idx,a))
```

## Output
```
<script.py> output:
    room 0: 11.25
    room 1: 18.0
    room 2: 20.0
    room 3: 10.75
    room 4: 9.5
```