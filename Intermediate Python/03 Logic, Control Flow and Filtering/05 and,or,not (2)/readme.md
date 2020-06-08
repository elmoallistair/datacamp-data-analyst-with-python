## and, or, not (2)

To see if you completely understood the boolean operators, have a look at the following piece of Python code:

> ```
> x = 8
> y = 9
> not(not(x < 3) and not(y > 14 or y > 10))
> ```

What will the result be if you execute these three commands in the IPython Shell?

*NB: Notice that `not` has a higher priority than `and` and `or`, it is executed first.*

<hr>

**Possible Answers**
* True
* False
* Running these commands will result in an error.

## Answer
> False