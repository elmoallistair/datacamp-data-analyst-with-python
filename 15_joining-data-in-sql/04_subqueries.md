## Subqueries

In this closing chapter, you'll learn how to use nested queries and you'll use what you’ve learned in this course to solve three challenge problems.

<br>

### Subquery inside where

```
-- Select fields
SELECT *
  -- From populations
  FROM populations
-- Where life_expectancy is greater than
WHERE life_expectancy >
  -- 1.15 * subquery
  1.15 * (SELECT AVG(life_expectancy)
   FROM populations
   WHERE year = 2015) AND
  year = 2015;
```

### Subquery inside where (2)

```
-- 2. Select fields
SELECT name, country_code, urbanarea_pop
  -- 3. From cities
  FROM cities
-- 4. Where city name in the field of capital cities
WHERE name IN
  -- 1. Subquery
  (SELECT capital
   FROM countries)
ORDER BY urbanarea_pop DESC;
```

### Subquery inside select

```
SELECT countries.name AS country, COUNT(*) AS cities_num
  FROM cities
    INNER JOIN countries
    ON countries.code = cities.country_code
GROUP BY country
ORDER BY cities_num DESC, country
LIMIT 9;

SELECT countries.name AS country,
  (SELECT COUNT(*)
  FROM cities
  WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;
```

### Subquery inside from

```
-- Select fields (with aliases)
SELECT code, COUNT(name) AS lang_num
  -- From languages
  FROM languages
-- Group by code
GROUP BY code;

SELECT local_name, subquery.lang_num
  FROM countries,
  	(SELECT code, COUNT(*) AS lang_num
  	 FROM languages
  	 GROUP BY code) AS subquery
  WHERE countries.code = subquery.code
ORDER BY lang_num DESC;
```

### Advanced subquery

```
-- Select fields
SELECT name, continent, inflation_rate
  -- From countries
  FROM countries
	-- Join to economies
	INNER JOIN economies
	-- Match on code
	ON countries.code = economies.code
  -- Where year is 2015
  WHERE year = 2015
    -- And inflation rate in subquery (alias as subquery)
    AND inflation_rate IN (
        SELECT MAX(inflation_rate) AS max_inf
        FROM (
             SELECT name, continent, inflation_rate
             FROM countries
             INNER JOIN economies
             ON countries.code = economies.code
             WHERE year = 2015) AS subquery
      -- Group by continent
        GROUP BY continent);
```

### Subquery challenge

```
-- Select fields
SELECT code, inflation_rate, unemployment_rate
  -- From economies
  FROM economies
  -- Where year is 2015 and code is not in
  WHERE year=2015 AND code NOT IN
  	-- Subquery
  	(SELECT code
  	 FROM countries
  	 WHERE (gov_form = 'Constitutional Monarchy' OR gov_form LIKE '%Republic%'))
-- Order by inflation rate
ORDER BY inflation_rate;
```

### Final challenge

```
-- Select fields
SELECT DISTINCT c1.name, c2.total_investment, c2.imports
  -- From table (with alias)
  FROM countries AS c1
    -- Join with table (with alias)
    LEFT JOIN economies AS c2
      -- Match on code
      ON (c1.code = c2.code
      -- and code in Subquery
        AND c2.code IN (
          SELECT l.code
          FROM languages AS l
          WHERE official = 'True'
        ) )
  -- Where region and year are correct
  WHERE c1.region = 'Central America' AND c2.year = 2015
-- Order by field
ORDER BY c1.name;
```

### Final challenge (2)

```
-- Select fields
SELECT region, continent, AVG(fertility_rate) AS avg_fert_rate
  -- From left table
  FROM countries AS c
    -- Join to right table
    INNER JOIN populations AS p
      -- Match on join condition
      ON c.code = p.country_code
  -- Where specific records matching some condition
  WHERE year = 2015
-- Group appropriately
GROUP BY region, continent
-- Order appropriately
ORDER BY avg_fert_rate;
```

### Final challenge (3)

```
-- Select fields
SELECT name, country_code, city_proper_pop, metroarea_pop,  
      -- Calculate city_perc
      city_proper_pop / metroarea_pop * 100 AS city_perc
  -- From appropriate table
  FROM cities
  -- Where 
  WHERE name IN
    -- Subquery
    (SELECT capital
     FROM countries
     WHERE ( continent = 'Europe'
        OR continent LIKE '%America'))
       AND metroarea_pop IS NOT NULL
-- Order appropriately
ORDER BY city_perc DESC
-- Limit amount
LIMIT 10;
```