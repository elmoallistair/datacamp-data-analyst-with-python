## Visualizing Two Quantitative Variables

In this chapter, you will create and customize plots that visualize the relationship between two quantitative variables. To do this, you will use scatter plots and line plots to explore how the level of air pollution in a city changes over the course of a day and how horsepower relates to fuel efficiency in cars. You will also see another big advantage of using Seaborn - the ability to easily create subplots in a single figure!

<br>

### Creating subplots with col and row

```
# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences",
            y="G3",
            data=student_data,
            kind='scatter')

# Show plot
plt.show()
```

### Creating two-factor subplots

```
# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col="schoolsup",
            col_order=["yes", "no"],
            row="famsup",
            row_order=["yes", "no"])

# Show plot
plt.show()
```

### Changing the size of scatter plot points

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower",
            y="mpg",
            data=mpg,
            kind="scatter",
            size="cylinders",
            hue="cylinders")

# Show plot
plt.show()
```

### Changing the style of scatter plot points

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x='acceleration', y='mpg', data=mpg, kind='scatter', style='origin', hue='origin')

# Show plot
plt.show()
```

### Interpreting line plots

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x="model_year",y="mpg", data=mpg, kind='line')

# Show plot
plt.show()
```

### Visualizing standard deviation with line plots

```
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci='sd')

# Show plot
plt.show()
```

### Plotting subgroups in line plots

```
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower
sns.relplot(x='model_year',
            y='horsepower',
            data=mpg,
            kind='line',
            ci=None)

# Show plot
plt.show()
```