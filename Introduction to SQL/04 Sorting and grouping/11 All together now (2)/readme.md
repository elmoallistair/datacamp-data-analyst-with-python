# All together now (2)

Great work! Now try another large query. This time, all in one go!

Remember, if you only want to return a certain number of results, you can use the `LIMIT` keyword to limit the number of rows returned

<hr>

**Instructions**
* Get the country, average budget, and average gross take of countries that have made more than 10 films. Order the result by country name, and limit the number of results displayed to 5. You should alias the averages as `avg_budget` and `avg_gross` respectively.


## query.sql
```
-- select country, average budget, average gross
SELECT country, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
-- from the films table
FROM films
-- group by country
GROUP BY country
-- where the country has more than 10 titles
HAVING COUNT(country) > 10
-- order by country
ORDER BY country
-- limit to only show 5 results
LIMIT 5;
```