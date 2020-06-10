# LIKE and NOT LIKE

As you've seen, the `WHERE` clause can be used to filter text data. However, so far you've only been able to filter by specifying the exact text you're interested in. In the real world, often you'll want to search for a pattern rather than a specific text string.

In SQL, the `LIKE` operator can be used in a `WHERE` clause to search for a pattern in a column. To accomplish this, you use something called a *wildcard* as a placeholder for some other values. There are two wildcards you can use with `LIKE`:

The `%` wildcard will match zero, one, or many characters in text. For example, the following query matches companies like `'Data'`, `'DataC'` `'DataCamp'`, `'DataMind'`, and so on:

> SELECT name\
> FROM companies\
> WHERE name LIKE 'Data%';

The `_` wildcard will match a *single* character. For example, the following query matches companies like `'DataCamp'`, `'DataComp'`, and so on:

> SELECT name\
> FROM companies\
> WHERE name LIKE 'DataC_mp';

You can also use the `NOT LIKE` operator to find records that don't match the pattern you specify.

<hr>

**Instructions**
* Get the names of all people whose names begin with 'B'. The pattern you need is `'B%'`.
* Get the names of people whose names have 'r' as the second letter. The pattern you need is `'_r%'`.
* Get the names of people whose names don't start with A. The pattern you need is 'A%'.

## query.sql
```
SELECT name FROM people WHERE name LIKE 'B%'
SELECT name FROM people WHERE name LIKE '_r%'
SELECT name FROM people WHERE name NOT LIKE 'A%'
```