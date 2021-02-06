## Aggregate Functions

This chapter teaches you how to use aggregate functions to summarize data and gain useful insights. You'll also learn about arithmetic in SQL and how to use aliases to make your results more readable.

<br>

### Aggregate functions

```
SELECT SUM(duration) FROM films
SELECT AVG(duration) FROM films
SELECT MIN(duration) FROM films
SELECT MAX(duration) FROM films
```

### Aggregate functions practice

```
SELECT SUM(gross) FROM films
SELECT AVG(gross) FROM films
SELECT MIN(gross) FROM films
SELECT MAX(gross) FROM films
```

### Combining aggregate functions with WHERE

```
SELECT SUM(gross) FROM films WHERE release_year >= 2000
SELECT AVG(gross) FROM films WHERE title LIKE 'A%'
SELECT MIN(gross) FROM films WHERE release_year = 1994
SELECT MAX(gross) FROM films WHERE release_year BETWEEN 2000 AND 2012
```

### It's AS simple AS aliasing

```
SELECT title, gross - budget AS net_profit FROM films
SELECT title, duration/60.0 AS duration_hours FROM films
SELECT AVG(duration) / 60.0 AS avg_duration_hours FROM films
```

### Even more aliasing

```
SELECT COUNT(deathdate) * 100.0 / COUNT(*) AS percentage_dead FROM people
SELECT MAX(release_year) - MIN(release_year) AS difference FROM films
SELECT (MAX(release_year) - MIN(release_year)) / 10.0 AS number_of_decades FROM films
```