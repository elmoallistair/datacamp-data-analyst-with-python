## Customizing axis labels and adding titles

Customizing the axis labels requires using the set_xlabel and set_ylabel methods of the Axes object. Adding a title uses the set_title method.

In this exercise, you will customize the content of the axis labels and add a title to a plot.

As before, the data is already provided in Pandas DataFrame objects loaded into memory: `seattle_weather` and `austin_weather`. These each have a `MONTH` column and a `MLY-PRCP-NORMAL` column. These data are plotted against each other in the first two lines of the sample code provided.

In addition, a Figure object named `fig` and an Axes object named `ax` have already been created for you.

<hr>

**Instructions**
* Use the `set_xlabel` method to add the label: "Time (months)".
* Use the `set_ylabel` method to add the label: "Precipitation (inches)".
* Use the `set_title` method to add the title: "Weather patterns in Austin and Seattle".

## Script
```
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel('Time (months)')

# Customize the y-axis label
ax.set_ylabel('Precipitation (inches)')

# Add the title
ax.set_title('Weather patterns in Austin and Seattle')

# Display the figure
plt.show()
```

## Plots
![img](index.svg)