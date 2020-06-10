# HAVING a great time

In SQL, aggregate functions can't be used in `WHERE` clauses. For example, the following query is invalid:

> SELECT release_year\
> FROM films\
> GROUP BY release_year\
> WHERE COUNT(title) > 10;

This means that if you want to filter based on the result of an aggregate function, you need another way! That's where the `HAVING` clause comes in. For example,

> SELECT release_year\
> FROM films\
> GROUP BY release_year\
> HAVING COUNT(title) > 10;

shows only those years in which more than 10 films were released.

<hr>

In how many different years were more than 200 movies released?

**Possible Answers**
* 2
* 13
* 44
* 63

**Answer**
> 13