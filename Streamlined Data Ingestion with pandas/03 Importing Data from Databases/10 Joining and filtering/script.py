# Query to get water leak calls and daily precipitation
query = """
SELECT hpd311calls.*, weather.prcp
    FROM hpd311calls
    JOIN weather
    ON hpd311calls.created_date = weather.date
    WHERE hpd311calls.complaint_type = 'WATER LEAK';"""

# Load query results into the leak_calls data frame
leak_calls = pd.read_sql(query, engine)

# View the data frame
print(leak_calls.head())