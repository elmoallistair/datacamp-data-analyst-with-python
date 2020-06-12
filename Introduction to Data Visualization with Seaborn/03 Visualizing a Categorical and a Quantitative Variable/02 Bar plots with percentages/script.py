# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender',
            y='Interested in Math',
            data=survey_data,
            kind='bar')

# Show plot
plt.show()