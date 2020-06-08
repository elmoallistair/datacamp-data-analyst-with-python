## Add conditionals

The `while` loop that corrects the `offset` is a good start, but what if `offset` is negative? You can try to run the following code where `offset` is initialized to `-6`:

> ```
> # Initialize offset
> offset = -6
>
> # Code the while loop
> while offset != 0 :
>     print("correcting...")
>     offset = offset - 1
>     print(offset)
> ```

but your session `will` be disconnected. The while loop will never stop running, because `offset` will be further decreased on every run. `offset != 0` will never become `False` and the `while` loop continues forever.

Fix things by putting an `if-else` statement inside the `while` loop. If your code is still taking too long to run, you probably made a mistake!

<hr>

**Instructions**
* **Inside** the while loop, complete the `if-else` statement:
    * If `offset` is greater than zero, you should decrease `offset` by 1.
    * Else, you should increase `offset` by 1.
* If you've coded things correctly, hitting Submit Answer should work this time.

*If your code is still taking too long to run (or your session is expiring), you probably made a mistake. Check your code and make sure that the statement `offset != 0` will eventually evaluate to `FALSE`!*

## Script
```
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset -= 1
    else :
      offset += 1
    print(offset)
```

## Output
```
<script.py> output:
    correcting...
    -5
    correcting...
    -4
    correcting...
    -3
    correcting...
    -2
    correcting...
    -1
    correcting...
    0
```