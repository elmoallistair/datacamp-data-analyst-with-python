# GROUP BY practice

As you've just seen, combining aggregate functions with `GROUP BY` can yield some powerful results!

A word of warning: SQL will return an error if you try to `SELECT` a field that is not in your `GROUP BY` clause without using it to calculate some kind of value about the entire group.

Note that you can combine `GROUP BY` with `ORDER BY` to group your results, calculate something about them, and then order your results. For example,

> SELECT sex, count(*)\
> FROM employees\
> GROUP BY sex\
> ORDER BY count DESC;

might return something like

| sex    | count |
|--------|-------|
| male   | 15    |
| female | 19    |


because there are more females at our company than males. Note also that `ORDER BY` always goes after `GROUP BY`. Let's try some exercises!

<hr>

**Instructions**
* Get the release year and count of films released in each year.
* Get the release year and average duration of all films, grouped by release year.
* Get the release year and largest budget for all films, grouped by release year.
* Get the IMDB score and count of film reviews grouped by IMDB score in the reviews table.

## query.sql
```
SELECT release_year, COUNT(*) FROM films GROUP BY release_year;
SELECT release_year, AVG(duration) FROM films GROUP BY release_year;
SELECT release_year, MAX(budget) FROM films GROUP BY release_year;
SELECT imdb_score, COUNT(*) FROM reviews GROUP BY imdb_score;
```