## Filtering rows

This chapter builds on the first by teaching you how to filter tables for rows satisfying some criteria of interest. You'll learn how to use basic comparison operators, combine multiple criteria, match patterns in text, and much more.

<br>

### Simple filtering of numeric values

```
SELECT * FROM films WHERE release_year = 2016
SELECT COUNT(*) FROM films WHERE release_year < 2000
SELECT title, release_year FROM films WHERE release_year > 2000
```

### Simple filtering of text

```
SELECT * FROM films WHERE language = 'French'
SELECT name, birthdate FROM people WHERE birthdate = '1974-11-11'
SELECT COUNT(*) FROM films WHERE language = 'Hindi'
SELECT * FROM films WHERE certification = 'R'
```

### WHERE AND

```
SELECT title, release_year FROM films WHERE language='Spanish' AND release_year < 2000
SELECT * FROM films WHERE language='Spanish' AND release_year > 2000
SELECT * FROM films WHERE language='Spanish' AND release_year > 2000 AND release_year < 2010
```

### WHERE AND OR (2)

```
SELECT title, release_year FROM films WHERE release_year BETWEEN 1990 AND 1999
SELECT * FROM films WHERE release_year BETWEEN 1990 AND 1999 AND (language = 'French' OR language = 'Spanish')
SELECT * FROM films WHERE release_year BETWEEN 1990 AND 1999 AND (language = 'French' OR language = 'Spanish') AND gross > 2000000
```

### BETWEEN (2)

```
SELECT title, release_year FROM films
WHERE release_year BETWEEN 1990 AND 2000
AND budget > 100000000
AND (language = 'Spanish' OR language = 'French')
```

### WHERE IN

```
SELECT title, release_year FROM films WHERE release_year IN (1990,2000) AND duration > 120
SELECT title, language FROM films WHERE language IN ('English','Spanish','French')
SELECT title, certification FROM films WHERE certification IN ('NC-17','R')
```

### NULL and IS NULL

```
SELECT name FROM people WHERE deathdate IS NULL
SELECT title FROM films WHERE budget IS NULL
SELECT COUNT(*) FROM films WHERE language IS NULL
```

### LIKE and NOT LIKE

```
SELECT name FROM people WHERE name LIKE 'B%'
SELECT name FROM people WHERE name LIKE '_r%'
SELECT name FROM people WHERE name NOT LIKE 'A%'
```