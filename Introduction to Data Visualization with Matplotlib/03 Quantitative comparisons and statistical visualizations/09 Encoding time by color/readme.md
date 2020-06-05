## Encoding time by color

The screen only has two dimensions, but we can encode another dimension in the scatter plot using color. Here, we will visualize the climate_change dataset, plotting a scatter plot of the "co2" column, on the x-axis, against the "relative_temp" column, on the y-axis. We will encode time using the color dimension, with earlier times appearing as darker shades of blue and later times appearing as brighter shades of yellow.

<hr>

**Instructions**

* Using the `ax.scatter` method add a scatter plot of the `"co2"` column (x-axis) against the `"relative_temp"` column.
* Use the `c` key-word argument to pass in the index of the DataFrame as input to color each point according to its date.
* Set the x-axis label to `"CO2 (ppm)"` and the y-axis label to `"Relative temperature (C)"`.

## Script
```
fig, ax = plt.subplots()

# Add data: "co2", "relative_temp" as x-y, index as color
ax.scatter(climate_change.co2, climate_change.relative_temp, c=climate_change.index)

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel('CO2 (ppm)')

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel('Relative temperature (C)')

plt.show()
```

## Plot
![img](index.svg)