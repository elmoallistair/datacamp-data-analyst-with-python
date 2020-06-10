## SELECTing multiple columns

Well done! Now you know how to select single columns.

In the real world, you will often want to select multiple columns. Luckily, SQL makes this really easy. To select multiple columns from a table, simply separate the column names with commas!

For example, this query selects two columns, `name` and `birthdate`, from the `people` table:

> SELECT name, birthdate\
> FROM people;

Sometimes, you may want to select all columns from a table. Typing out every column name would be a pain, so there's a handy shortcut:

> SELECT *\
> FROM people;

If you only want to return a certain number of results, you can use the `LIMIT` keyword to limit the number of rows returned:

> SELECT *\
> FROM people\
> LIMIT 10;

Before getting started with the instructions below, check out the column names in the `films` table by clicking on the `films` tab to the right!

<hr>

**Instructions**
* Get the title of every film from the `films` table.
* Get the title and release year for every film.
* Get the title, release year and country for every film.
* Get all columns from the `films` table.

## query.sql
```
SELECT title FROM films;
SELECT title, release_year FROM films
SELECT title, release_year, country FROM films;
SELECT * FROM films;
```