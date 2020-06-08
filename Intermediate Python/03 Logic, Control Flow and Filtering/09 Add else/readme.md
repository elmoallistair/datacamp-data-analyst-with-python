## Add else

On the right, the `if` construct for `room` has been extended with an `else` statement so that "looking around elsewhere." is printed if the condition `room == "kit"` evaluates to `False`.

Can you do a similar thing to add more functionality to the `if` construct for `area`?

<hr>

**Instructions**
* Add an `else` statement to the second control structure so that "pretty small." is printed out if `area > 15` evaluates to `False`.

## Script
```
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else:
    print("pretty small.")
```

## Output
```
<script.py> output:
    looking around in the kitchen.
    pretty small.
```