# Introduction to NULL and IS NULL

In SQL, `NULL` represents a missing or unknown value. You can check for `NULL` values using the expression `IS NULL`. For example, to count the number of missing birth dates in the `people` table:

> SELECT COUNT(*)
> FROM people
> WHERE birthdate IS NULL;

As you can see, `IS NULL` is useful when combined with `WHERE` to figure out what data you're missing.

Sometimes, you'll want to filter out missing values so you only get results which are not `NULL`. To do this, you can use the `IS NOT NULL` operator.

For example, this query gives the names of all people whose birth dates are not missing in the people table.

> SELECT name
> FROM people
> WHERE birthdate IS NOT NULL;

<hr>

What does `NULL` represent?

**Possible Answers**
* A corrupt entry
* A missing value
* An empty string
* An invalid value

**Answer**
> A missing value