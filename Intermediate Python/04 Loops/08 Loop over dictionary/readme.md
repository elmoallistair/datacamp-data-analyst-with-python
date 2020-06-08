## Loop over dictionary

In Python 3, you need the `items()` method to loop over a dictionary:

> ```
> world = { "afghanistan":30.55,
>           "albania":2.77,
>           "algeria":39.21 }
>
> for key, value in world.items() :
>     print(key + " -- " + str(value))
> ```

Remember the `europe` dictionary that contained the names of some European countries as key and their capitals as corresponding value? Go ahead and write a loop to iterate over it!

<hr>

**Instructions**
* Write a `for` loop that goes through each key:value pair of `europe`. On each iteration, `"the capital of x is y"` should be printed out, where x is the key and y is the value of the pair.

## Script
```
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna'}

# Iterate over europe
for key, value in europe.items():
    print("the capital of {} is {}".format(key, str(value)))
```

## Output
```
<script.py> output:
    the capital of germany is berlin
    the capital of austria is vienna
    the capital of poland is warsaw
    the capital of spain is madrid
    the capital of norway is oslo
    the capital of italy is rome
    the capital of france is paris
```