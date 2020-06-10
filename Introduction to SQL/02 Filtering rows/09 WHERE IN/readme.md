# WHERE IN

As you've seen, `WHERE` is very useful for filtering results. However, if you want to filter based on many conditions, `WHERE` can get unwieldy. For example:

> SELECT name\
> FROM kids\
> WHERE age = 2\
> OR age = 4\
> OR age = 6\
> OR age = 8\
> OR age = 10;

Enter the `IN` operator! The `IN` operator allows you to specify multiple values in a `WHERE` clause, making it easier and quicker to specify multiple `OR` conditions! Neat, right?

So, the above example would become simply:

> SELECT name\
> FROM kids\
> WHERE age IN (2, 4, 6, 8, 10);

Try using the `IN` operator yourself!

<hr>

**Instructions**
* Get the title and release year of all films released in 1990 or 2000 that were longer than two hours. Remember, duration is in minutes!
* Get the title and language of all films which were in English, Spanish, or French.
* Get the title and certification of all films with an NC-17 or R certification.

## query.sql
```
SELECT title, release_year FROM films WHERE release_year IN (1990,2000) AND duration > 120
SELECT title, language FROM films WHERE language IN ('English','Spanish','French')
SELECT title, certification FROM films WHERE certification IN ('NC-17','R')
```