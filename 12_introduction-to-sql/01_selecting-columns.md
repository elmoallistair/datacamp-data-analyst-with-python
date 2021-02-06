## Selecting columns

This chapter provides a brief introduction to working with relational databases. You'll learn about their structure, how to talk about them using database lingo, and how to begin an analysis using simple SQL commands to select and summarize columns from database tables.

<br>

### Onboarding | Errors

```
SELECT name AS result FROM people;
```

### Onboarding | Bullet Exercises

```
SELECT 'SQL is cool!'
AS result;
```

### SELECTing single columns

```
SELECT title FROM films
SELECT release_year FROM films
SELECT name FROM people
```

### SELECTing multiple columns

```
SELECT title FROM films;
SELECT title, release_year FROM films
SELECT title, release_year, country FROM films;
SELECT * FROM films;
```

### SELECT DISTINCT

```
SELECT DISTINCT(country) FROM films
SELECT DISTINCT(certification) FROM films
SELECT DISTINCT(role) FROM roles
```

### Practice with COUNT

```
SELECT COUNT(*) FROM people
SELECT COUNT(birthdate) FROM people
SELECT COUNT(DISTINCT(birthdate)) FROM people
SELECT COUNT(DISTINCT(language)) FROM films
SELECT COUNT(DISTINCT(country)) FROM films
```