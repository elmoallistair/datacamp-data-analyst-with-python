-- 3. Select fields
SELECT code, name
  -- 4. From Countries
  FROM countries
  -- 5. Where continent is Oceania
  WHERE continent = 'Oceania'
  	-- 1. And code not in
  	AND NOT code IN
  	-- 2. Subquery
  	(SELECT code
  	 FROM currencies);