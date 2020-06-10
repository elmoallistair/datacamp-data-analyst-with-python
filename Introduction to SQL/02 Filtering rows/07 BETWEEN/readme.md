# BETWEEN

As you've learned, you can use the following query to get titles of all films released in and between 1994 and 2000:

> SELECT title\
> FROM films\
> WHERE release_year >= 1994\
> AND release_year <= 2000;

Checking for ranges like this is very common, so in SQL the **BETWEEN** keyword provides a useful shorthand for filtering values within a specified range. This query is equivalent to the one above:

> SELECT title\
> FROM films\
> WHERE release_year\
> BETWEEN 1994 AND 2000;

It's important to remember that **BETWEEN** is inclusive, meaning the beginning and end values are included in the results!

<hr>

What does the **BETWEEN** keyword do?

**Possible Answers**
* Filter numeric values
* Filter text values
* Filter values in a specified list
* Filter values in a specified range

**Answer**
> Filter values in a specified range