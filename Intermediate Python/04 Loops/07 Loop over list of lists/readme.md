## Loop over list of lists

Remember the `house` variable from the Intro to Python course? Have a look at its definition on the right. It's basically a list of lists, where each sublist contains the name and area of a room in your house.

It's up to you to build a `for` loop from scratch this time!

<hr>

**Instructions**
* Write a `for` loop that goes through each sublist of `house` and prints out `the x is y sqm`, where x is the name of the room and y is the area of the room.

## Script
```
# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for x,y in enumerate(house):
    print('the {} is {} sqm'.format(house[x][0],house[x][1]))
```

## Output
```
<script.py> output:
    the hallway is 11.25 sqm
    the kitchen is 18.0 sqm
    the living room is 20.0 sqm
    the bedroom is 10.75 sqm
    the bathroom is 9.5 sqm
```