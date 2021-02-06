## Visualizing a Categorical and a Quantitative Variable

Categorical variables are present in nearly every dataset, but they are especially prominent in survey data. In this chapter, you will learn how to create and customize categorical plots such as box plots, bar plots, count plots, and point plots. Along the way, you will explore survey data from young people about their interests, students about their study habits, and adult men about their feelings about masculinity.

<br>

### Count plots

```
# Create count plot of internet usage
sns.catplot(x='Internet usage', data=survey_data, kind='count')

# Show plot
plt.show()
```

### Bar plots with percentages

```
# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender',
            y='Interested in Math',
            data=survey_data,
            kind='bar')

# Show plot
plt.show()
```

### Customizing bar plots

```
# Create bar plot of average final grade in each study category
sns.catplot(x='study_time',
            y='G3',
            data=student_data,
            kind='bar')

# Show plot
plt.show()
```

### Create and interpret a box plot

```
# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x='study_time',
            y='G3',
            data=student_data,
            kind='box',
            order=study_time_order)

# Show plot
plt.show()
```

### Omitting outliers

```
# Create a box plot with subgroups and omit the outliers
sns.catplot(x='internet',
            y='G3',
            data=student_data,
            kind='box',
            col='location',
            hue='location',
            sym='')

# Show plot
plt.show()
```

### Adjusting the whiskers

```
# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()
```

### Customizing point plots

```
# Create a point plot of family relationship vs. absences
sns.catplot(x='famrel',
            y='absences',
            data=student_data,
            kind='point')

# Show plot
plt.show()
```

### Point plots with subgroups

```
# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)

# Show plot
plt.show()
```