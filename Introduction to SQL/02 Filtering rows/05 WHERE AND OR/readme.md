# WHERE AND OR

What if you want to select rows based on multiple conditions where some but not all of the conditions need to be met? For this, SQL has the `OR` operator.

For example, the following returns all films released in either 1994 or 2000:

> SELECT title\
> FROM films\
> WHERE release_year = 1994\
> OR release_year = 2000;

Note that you need to specify the column for every `OR` condition, so the following is invalid:

> SELECT title\
> FROM films\
> WHERE release_year = 1994 OR 2000;

When combining `AND` and `OR`, be sure to enclose the individual clauses in parentheses, like so:

> SELECT title\
> FROM films\
> WHERE (release_year = 1994 OR release_year = 1995)\
> AND (certification = 'PG' OR certification = 'R');

Otherwise, due to SQL's precedence rules, you may not get the results you're expecting!

<hr>

What does the `OR` operator do?

**Possible Answers**
* Display only rows that meet at least **one** of the specified conditions.
* Display only rows that meet **all** of the specified conditions.
* Display only rows that meet **none** of the specified conditions.

**Answer**
> Display only rows that meet at least **one** of the specified conditions.