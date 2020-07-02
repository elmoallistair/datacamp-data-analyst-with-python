# Unstack the 'arrest_rate' Series into a DataFrame
print(arrest_rate.unstack)

# Create the same DataFrame using a pivot table
print(ri_weather.pivot_table(index='violation', columns='rating', values='is_arrested'))