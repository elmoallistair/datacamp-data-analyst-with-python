## List of dictionaries

You recently got some new avocado data from 2019 that you'd like to put in a DataFrame using the list of dictionaries method. Remember that with this method, you go through the data row by row.

| date         | small_sold | large_sold |
|--------------|------------|------------|
| "2019-11-03" | 10376832   | 7835071    |
| "2019-11-10" | 10717154   | 8561348    |

`pandas` as pd `is` imported.

<hr>

**Instructions**

* Create a list of dictionaries with the new data called `avocados_list`.
* Convert the list into a DataFrame called `avocados_2019`.
* Print your new DataFrame.

## Script
```
# Create a list of dictionaries with new data
avocados_list = [
    {'date': "2019-11-03", 'small_sold': 10376832, 'large_sold': 7835071},
    {'date': "2019-11-10", 'small_sold': 10717154, 'large_sold': 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)
```

## Output
```
         date  small_sold  large_sold
0  2019-11-03    10376832     7835071
1  2019-11-10    10717154     8561348
```