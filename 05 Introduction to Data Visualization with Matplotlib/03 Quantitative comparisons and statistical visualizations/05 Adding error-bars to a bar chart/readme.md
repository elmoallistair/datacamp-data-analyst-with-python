## Adding error-bars to a bar chart

Statistical plotting techniques add quantitative information for comparisons into the visualization. For example, in this exercise, we will add error bars that quantify not only the difference in the means of the height of medalists in the 2016 Olympic Games, but also the standard deviation of each of these groups, as a way to assess whether the difference is substantial relative to the variability within each group.

For the purpose of this exercise, you will have two DataFrames: `mens_rowing` holds data about the medalists in the rowing events and `mens_gymnastics` will hold information about the medalists in the gymnastics events.

**Instructions**

* Add a bar with size equal to the mean of the `"Height"` column in the `mens_rowing` DataFrame and an error-bar of its standard deviation.
* Add another bar for the mean of the `"Height"` column in `mens_gymnastics` with an error-bar of its standard deviation.
* Add a label to the the y-axis: `"Height (cm)"`.

## Script
```
fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar("Rowing", mens_rowing.Height.mean(), yerr=mens_rowing.Height.std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar("Gymnastics", mens_gymnastics.Height.mean(), yerr=mens_gymnastics.Height.std())

# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()
```

## Output
![img](index.svg)