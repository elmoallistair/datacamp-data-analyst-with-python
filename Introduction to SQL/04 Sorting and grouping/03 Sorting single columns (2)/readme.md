# Sorting single columns (2)

Let's get some more practice with `ORDER BY`!

<hr>

**Instructions**
* Get the title of films released in 2000 or 2012, in the order they were released.
* Get all details for all films except those released in 2015 and order them by duration.
* Get the title and gross earnings for movies which begin with the letter 'M' and order the results alphabetically.

## query.sql
```
SELECT title FROM films WHERE release_year IN (2000, 2012) ORDER BY release_year
SELECT * FROM films WHERE release_year <> 2015 ORDER BY duration
SELECT title, gross FROM films WHERE title LIKE 'M%' ORDER BY title
```