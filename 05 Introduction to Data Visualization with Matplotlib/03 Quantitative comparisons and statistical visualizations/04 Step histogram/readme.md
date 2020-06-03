"Step" histogram

Histograms allow us to see the distributions of the data in different groups in our data. In this exercise, you will select groups from the Summer 2016 Olympic Games medalist dataset to compare the height of medalist athletes in two different sports.

The data is stored in a Pandas DataFrame object called `summer_2016_medals` that has a column "Height". In addition, you are provided a Pandas GroupBy object that has been grouped by the sport.

In the exercise below, you will visualize and label the histograms of two sports: "Gymnastics" and "Rowing" and see the marked difference between medalists in these two sports.

**Instructions**

* Use the `hist` method to display a histogram of the `"Weight"` column from the `mens_rowing` DataFrame, label this as `"Rowing"`.
* Use `hist` to display a histogram of the `"Weight"` column from the `mens_gymnastics` DataFrame, and label this as `"Gymnastics"`.
* For both histograms, use the 'histtype' argument to visualize the data using the `'step'` type and set the number of bins to use to 5.
* Add a legend to the figure, before it is displayed.

## Script
```
fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing.Weight, label='Rowing', histtype='step', bins=5)

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics.Weight, label='Gymnastics', histtype='step', bins=5)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()
```

## Output
![img](index.svg)