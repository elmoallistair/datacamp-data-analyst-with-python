# Create query to get temperature and precipitation by month
query = """
SELECT month, 
       MAX(tmax), 
       MIN(tmin),
       SUM(prcp)
  FROM weather 
 GROUP BY month;
"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)