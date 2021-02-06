## Getting Started in Python

Welcome to the wonderful world of Data Analysis in Python! In this chapter, you'll learn the basics of Python syntax, load your first Python modules, and use functions to get a suspect list for the kidnapping of Bayes, DataCamp's prize-winning Golden Retriever.

<br>

### Importing Python modules

```
# Use an import statement to import statsmodels
import statsmodels

# Import statsmodels under the alias sm
import statsmodels as sm

# Use an import statement to import seaborn with alias sns
import seaborn as sns
```

### Creating a float

```
# Fill in Bayes' age (4.0)
bayes_age = 4.0

# Display the variable bayes_age
print(bayes_age)
```

### Creating strings

```
# Bayes' favorite toy
favorite_toy = "Mr. Squeaky"

# Bayes' owner
owner = "DataCamp"

# Display variables
print(favorite_toy)
print(owner)
```

### Correcting string errors

```
# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors
birthday = "2017-07-14"
case_id = "DATACAMP!123-456?"
```

### Load a DataFrame

```
# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv("ransom.csv")

# Display DataFrame
print(r)
```

### Correcting a function error

```
# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors

# Plot a graph
plt.plot(x_values, y_values)

# Display the graph
plt.show()
```

### Snooping for suspects

```
# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = "FRQ****"

# Call the function lookup_plate()
lookup_plate(plate)

# Call lookup_plate() with the keyword argument for color
lookup_plate(plate, color="Green")
```