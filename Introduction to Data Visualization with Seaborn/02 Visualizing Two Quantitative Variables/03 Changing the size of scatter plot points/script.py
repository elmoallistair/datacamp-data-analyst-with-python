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