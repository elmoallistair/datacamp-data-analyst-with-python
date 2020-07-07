## Review inner join using on

Why does the following code result in an error?

```
SELECT c.name AS country, l.name AS language
FROM countries AS c
  INNER JOIN languages AS l;
```

**Possible Answers**

* The `languages` table has more rows than the `countries` table.
* There are multiple languages spoken in many countries.
* `INNER JOIN` requires a specification of the key field (or fields) in each table.
* Join queries may not be followed by a semi-colon.

**Answer**

> `INNER JOIN` requires a specification of the key field (or fields) in each table.