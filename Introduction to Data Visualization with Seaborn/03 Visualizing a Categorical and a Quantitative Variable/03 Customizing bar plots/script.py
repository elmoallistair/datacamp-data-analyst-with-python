# Create bar plot of average final grade in each study category
sns.catplot(x='study_time',
            y='G3',
            data=student_data,
            kind='bar')

# Show plot
plt.show()