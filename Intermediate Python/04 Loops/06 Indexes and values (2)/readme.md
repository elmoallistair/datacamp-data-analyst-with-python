## Indexes and values (2)

For non-programmer folks, `room 0: 11.25` is strange. Wouldn't it be better if the count started at 1?

<hr>

**Instructions**
* Adapt the `print()` function in the `for` loop on the right so that the first printout becomes `"room 1: 11.25"`, the second one `"room 2: 18.0"` and so on.

## Script
```
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))
```

## Output
```
<script.py> output:
    room 1: 11.25
    room 2: 18.0
    room 3: 20.0
    room 4: 10.75
    room 5: 9.5
```