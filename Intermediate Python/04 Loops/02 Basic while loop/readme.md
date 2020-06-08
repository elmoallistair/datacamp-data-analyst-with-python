## Basic while loop

Below you can find the example from the video where the `error` variable, initially equal to `50.0`, is divided by 4 and printed out on every run:

> ```
> error = 50.0
> while error > 1 :
>     error = error / 4
>     print(error)
> ```

This example will come in handy, because it's time to build a `while` loop yourself! We're going to code a `while` loop that implements a very basic control system for an [inverted pendulum](https://en.wikipedia.org/wiki/Inverted_pendulum). If there's an offset from standing perfectly straight, the `while` loop will incrementally fix this offset.

Note that if your `while` loop takes too long to run, you might have made a mistake. In particular, remember to **indent** the contents of the loop!

<hr>

**Instructions**
* Create the variable `offset` with an initial value of `8`.
* Code a while loop that keeps running as long as `offset` is not equal to `0`. Inside the `while` loop:
    * Print out the sentence `"correcting..."`.
    * Next, decrease the value of offset by 1. You can do this with `offset = offset - 1`.
    * Finally, still within your loop, print out `offset` so you can see how it changes.

## Script
```
# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print('correcting...')
    offset -= 1
    print(offset)
```

## Output
```
<script.py> output:
    correcting...
    7
    correcting...
    6
    correcting...
    5
    correcting...
    4
    correcting...
    3
    correcting...
    2
    correcting...
    1
    correcting...
    0
```