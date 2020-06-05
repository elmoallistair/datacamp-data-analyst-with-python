## Finding missing values

Missing values are everywhere, and you don't want them interfering with your work. Some functions ignore missing data by default, but that's not always the behavior you might want. Some functions can't handle missing values at all, so these values need to be taken care of before you can use them. If you don't know where your missing values are, or if they exist, you could make mistakes in your analysis. In this exercise, you'll determine if there are missing values in the dataset, and if so, how many.

`pandas` has been imported as `pd` and avocados_2016, a subset of `avocados` that contains only sales from 2016, is available.

<hr>

**Instructions**
* Print a DataFrame that shows whether each value in `avocados_2016` is missing or not.
* Print a summary that shows whether any value in each column is missing or not.
* Create a bar plot of the total number of missing values in each column.

## Scipt
```
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()
```

## Output
```
     date  avg_price  total_sold  small_sold  large_sold  xl_sold  total_bags_sold  small_bags_sold  large_bags_sold  xl_bags_sold
0   False      False       False       False       False    False            False            False            False         False
1   False      False       False       False       False    False            False            False            False         False
2   False      False       False       False        True    False            False            False            False         False
3   False      False       False       False       False    False            False            False            False         False
4   False      False       False       False       False     True            False            False            False         False
5   False      False       False        True       False    False            False            False            False         False
6   False      False       False       False       False    False            False            False            False         False
7   False      False       False       False        True    False            False            False            False         False
8   False      False       False       False       False    False            False            False            False         False
9   False      False       False       False       False    False            False            False            False         False
10  False      False       False       False        True    False            False            False            False         False
11  False      False       False       False       False    False            False            False            False         False
12  False      False       False       False       False    False            False            False            False         False
13  False      False       False       False       False    False            False            False            False         False
14  False      False       False       False       False    False            False            False            False         False
15  False      False       False       False        True    False            False            False            False         False
16  False      False       False       False       False     True            False            False            False         False
17  False      False       False       False       False    False            False            False            False         False
18  False      False       False       False       False    False            False            False            False         False
19  False      False       False       False        True    False            False            False            False         False
20  False      False       False       False       False    False            False            False            False         False
21  False      False       False       False       False    False            False            False            False         False
22  False      False       False       False       False    False            False            False            False         False
23  False      False       False       False       False    False            False            False            False         False
24  False      False       False       False       False    False            False            False            False         False
25  False      False       False       False       False    False            False            False            False         False
26  False      False       False       False       False    False            False            False            False         False
27  False      False       False       False       False    False            False            False            False         False
28  False      False       False       False       False    False            False            False            False         False
29  False      False       False       False       False    False            False            False            False         False
30  False      False       False       False       False     True            False            False            False         False
31  False      False       False       False       False    False            False            False            False         False
32  False      False       False       False       False     True            False            False            False         False
33  False      False       False       False       False    False            False            False            False         False
34  False      False       False       False       False    False            False            False            False         False
35  False      False       False       False       False    False            False            False            False         False
36  False      False       False        True       False    False            False            False            False         False
37  False      False       False       False        True    False            False            False            False         False
38  False      False       False       False       False    False            False            False            False         False
39  False      False       False       False       False    False            False            False            False         False
40  False      False       False        True       False    False            False            False            False         False
41  False      False       False       False       False    False            False            False            False         False
42  False      False       False       False       False    False            False            False            False         False
43  False      False       False       False       False    False            False            False            False         False
44  False      False       False        True       False    False            False            False            False         False
45  False      False       False       False       False    False            False            False            False         False
46  False      False       False       False       False    False            False            False            False         False
47  False      False       False       False       False    False            False            False            False         False
48  False      False       False       False       False    False            False            False            False         False
49  False      False       False       False       False    False            False            False            False         False
50  False      False       False        True       False    False            False            False            False         False
51  False      False       False        True       False    False            False            False            False         False
date               False
avg_price          False
total_sold         False
small_sold          True
large_sold          True
xl_sold             True
total_bags_sold    False
small_bags_sold    False
large_bags_sold    False
xl_bags_sold       False
dtype: bool
```

## Plots
![img](index.svg)