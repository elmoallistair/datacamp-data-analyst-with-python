-- 3. Select fields with aliases
SELECT c.code AS country_code,  c.name, e.year, e.inflation_rate
FROM countries AS c
  -- 1. Join to economies (alias e)
  INNER JOIN economies AS e
    -- 2. Match on code
    ON c.code = e.code;