# Even more aliasing

Let's practice your newfound aliasing skills some more before moving on!

**Recall**: SQL assumes that if you divide an integer by an integer, you want to get an integer back.

This means that the following will erroneously result in `400.0`:

> SELECT 45 / 10 * 100.0;

This is because `45 / 10` evaluates to an integer (`4`), and not a decimal number like we would expect.

So when you're dividing make sure at least one of your numbers has a decimal place:

> SELECT 45 * 100.0 / 10;

The above now gives the correct answer of `450.0` since the numerator (`45 * 100.0`) of the division is now a decimal!

<hr>

**Instructions**
* Get the percentage of `people` who are no longer alive. Alias the result as `percentage_dead`. Remember to use `100.0` and not `100`!
* Get the number of years between the newest film and oldest film. Alias the result as difference.
* Get the number of decades the `films` table covers. Alias the result as `number_of_decades`. The top half of your fraction should be enclosed in parentheses.


## query.sql
```
SELECT COUNT(deathdate) * 100.0 / COUNT(*) AS percentage_dead FROM people
SELECT MAX(release_year) - MIN(release_year) AS difference FROM films
SELECT (MAX(release_year) - MIN(release_year)) / 10.0 AS number_of_decades FROM films
```