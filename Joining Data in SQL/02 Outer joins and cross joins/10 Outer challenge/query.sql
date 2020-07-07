-- Select fields
SELECT c.name AS country, region, life_expectancy AS life_exp
-- From countries (alias as c)
FROM countries AS c
  -- Join to populations (alias as p)
  JOIN populations as p
    -- Match on country code
    ON c.code = p.country_code
-- Focus on 2010
WHERE year = 2010
-- Order by life_exp
ORDER BY life_expectancy
-- Limit to 5 records
LIMIT 5;