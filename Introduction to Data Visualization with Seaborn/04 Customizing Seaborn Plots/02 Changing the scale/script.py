# Set the context to "paper"
sns.set_context('paper')
# sns.set_context('notebook')
# sns.set_context('talk')
# sns.set_context('poster')

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()