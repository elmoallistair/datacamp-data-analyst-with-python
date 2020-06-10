## BETWEEN (2)

Similar to the `WHERE` clause, the `BETWEEN` clause can be used with multiple `AND` and `OR` operators, so you can build up your queries and make them even more powerful!

For example, suppose we have a table called `kids`. We can get the names of all kids between the ages of 2 and 12 from the United States:

> SELECT name\
> FROM kids\
> WHERE age BETWEEN 2 AND 12\
> AND nationality = 'USA';

Take a go at using `BETWEEN` with `AND` on the films data to get the title and release year of all Spanish language films released between 1990 and 2000 (inclusive) with budgets over $100 million. We have broken the problem into smaller steps so that you can build the query as you go along!

<hr>

**Instructions**
* Get the title and release year of all films released between 1990 and 2000 (inclusive).
* Now, build on your previous query to select only films that have budgets over $100 million.
* Now restrict the query to only return Spanish language films.
* Finally, modify to your previous query to include all Spanish language *or* French language films with the same criteria as before. Don't forget your parentheses!

## query.sql
```
SELECT title, release_year FROM films
WHERE release_year BETWEEN 1990 AND 2000
AND budget > 100000000
AND (language = 'Spanish' OR language = 'French')
````