# Sorting single columns

Now that you understand how `ORDER BY` works, give these exercises a go!

<hr>

**Instructions**
* Get the names of people from the `people` table, sorted alphabetically.
* Get the names of people, sorted by birth date.
* Get the birth date and name for every person, in order of when they were born.

## query.sql
```
SELECT name FROM people ORDER BY name
SELECT name FROM people ORDER BY birthdate
SELECT birthdate, name FROM people ORDER BY birthdate
```