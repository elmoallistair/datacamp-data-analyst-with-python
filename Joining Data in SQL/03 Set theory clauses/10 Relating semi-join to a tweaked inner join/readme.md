## Relating semi-join to a tweaked inner join

Let's revisit the code from the previous exercise, which retrieves languages spoken in the Middle East.

```
SELECT DISTINCT name
FROM languages
WHERE code IN
  (SELECT code
   FROM countries
   WHERE region = 'Middle East')
ORDER BY name;
```

Sometimes problems solved with semi-joins can also be solved using an inner join.

```
SELECT languages.name AS language
FROM languages
INNER JOIN countries
ON languages.code = countries.code
WHERE region = 'Middle East'
ORDER BY language;
```

This inner join isn't quite right. What is missing from this second code block to get it to match with the correct answer produced by the first block?

**Possible Answers**

* `HAVING` instead of `WHERE`
* `DISTINCT`
* `UNIQUE`

