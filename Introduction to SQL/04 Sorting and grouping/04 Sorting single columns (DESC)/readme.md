# Sorting single columns (DESC)

To order results in *descending* order, you can put the keyword `DESC` after your `ORDER BY`. For example, to get all the names in the `people` table, in reverse alphabetical order:

> SELECT name\
> FROM people\
> ORDER BY name DESC;

Now practice using `ORDER BY` with `DESC` to sort single columns in descending order!

<hr>

**Instructions**
* Get the IMDB score and film ID for every film from the reviews table, sorted from highest to lowest score.
* Get the title for every film, in reverse order.
* Get the title and duration for every film, in order of longest duration to shortest.

## query.sql
```
SELECT imdb_score, film_id FROM reviews ORDER BY imdb_score DESC
SELECT title FROM films ORDER BY title DESC
SELECT title, duration FROM films ORDER BY duration DESC
```