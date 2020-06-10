## SELECT DISTINCT

Often your results will include many duplicate values. If you want to select all the unique values from a column, you can use the `DISTINCT` keyword.

This might be useful if, for example, you're interested in knowing which languages are represented in the `films` table:

> SELECT DISTINCT language\
> FROM films;

Remember, you can check out the data in the tables by clicking on the tabs to the right under the editor!

<hr>

**Instructions**
* Get all the unique countries represented in the `films` table.
* Get all the different film certifications from the ``films`` table.
* Get the different types of film roles from the `roles` table.

## query.sql
```
SELECT DISTINCT(country) FROM films
SELECT DISTINCT(certification) FROM films
SELECT DISTINCT(role) FROM roles
```