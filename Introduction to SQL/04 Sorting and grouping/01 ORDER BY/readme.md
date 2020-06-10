# ORDER BY

Congratulations on making it this far! You now know how to select and filter your results.

In this chapter you'll learn how to sort and group your results to gain further insight. Let's go!

In SQL, the `ORDER BY` keyword is used to sort results in ascending or descending order according to the values of one or more columns.

By default `ORDER BY` will sort in ascending order. If you want to sort the results in descending order, you can use the `DESC` keyword. For example,

> SELECT title\
> FROM films\
> ORDER BY release_year DESC;

gives you the titles of films sorted by release year, from newest to oldest.

<hr>

How do you think `ORDER BY` sorts a column of text values by default?

**Possible Answers**
* Alphabetically (A-Z)
* Reverse alphabetically (Z-A)
* There's no natural ordering to text data
* By number of characters (fewest to most)

**Answer**
> Alphabetically (A-Z)