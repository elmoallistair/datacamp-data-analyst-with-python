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