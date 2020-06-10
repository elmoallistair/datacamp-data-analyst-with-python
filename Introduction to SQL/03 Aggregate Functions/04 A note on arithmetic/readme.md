# A note on arithmetic

In addition to using aggregate functions, you can perform basic arithmetic with symbols like `+`, `-`, `*`, and `/`.

So, for example, this gives a result of `12`:

> SELECT (4 * 3);

However, the following gives a result of `1`:

> SELECT (4 / 3);

What's going on here?

SQL assumes that if you divide an integer by an integer, you want to get an integer back. So be careful when dividing!

If you want more precision when dividing, you can add decimal places to your numbers. For example,

> SELECT (4.0 / 3.0) AS result;

gives you the result you would expect: `1.333`.

<hr>

What is the result of `SELECT (10 / 3)`;?

**Possible Answers**
* 2.333
* 3.333
* 3
* 3.0

**Answer**
> 3