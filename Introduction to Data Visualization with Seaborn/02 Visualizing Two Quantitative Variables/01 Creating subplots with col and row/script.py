# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences",
            y="G3",
            data=student_data,
            kind='scatter')

# Show plot
plt.show()