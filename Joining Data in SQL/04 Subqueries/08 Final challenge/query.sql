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