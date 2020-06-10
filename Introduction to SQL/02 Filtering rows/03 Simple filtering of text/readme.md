# Simple filtering of text

Remember, the WHERE clause can also be used to filter text results, such as names or countries.

For example, this query gets the titles of all films which were filmed in China:

> SELECT title\
> FROM films\
> WHERE country = 'China';

Now it's your turn to practice using WHERE with text values!

**Important: in PostgreSQL (the version of SQL we're using), you must use single quotes with `WHERE`.**

<hr>

**Instructions**
* Get all details for all French language films.
* Get the name and birth date of the person born on November 11th, 1974. Remember to use ISO date format ('1974-11-11')!
* Get the number of Hindi language films.
* Get all details for all films with an R certification.

## query.sql
```
SELECT * FROM films WHERE language = 'French'
SELECT name, birthdate FROM people WHERE birthdate = '1974-11-11'
SELECT COUNT(*) FROM films WHERE language = 'Hindi'
SELECT * FROM films WHERE certification = 'R'
```