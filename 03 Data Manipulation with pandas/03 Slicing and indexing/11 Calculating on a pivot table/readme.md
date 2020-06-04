## Calculating on a pivot table

Pivot tables are filled with summary statistics, but they are only a first step to finding something insightful. Often you'll need to perform further calculations on them. A common thing to do is to find the rows or columns where a highest or lowest value occurs.

Recall from Chapter 1 that you can easily subset a Series or DataFrame to find rows of interest using a logical condition inside of square brackets. For example: `series[series > value]`.

`pandas` is loaded as `pd` and the DataFrame `temp_by_country_city_vs_year` is available.

<hr>

**Instructions**
* Calculate the mean temperature for each year, assigning to `mean_temp_by_year`.
* Filter `mean_temp_by_year` for the year that had the highest mean temperature.
* Calculate the mean temperature for each city (across columns), assigning to `mean_temp_by_city`.
* Filter `mean_temp_by_city` for the city that had the lowest mean temperature.

## Script
```
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
```

## Output
```
year
2013    20.312
dtype: float64
country  city
China    Harbin    4.877
dtype: float64
```