## Two methods for selecting columns

Once again, we've loaded the credit card records of our four suspects into a DataFrame called `credit_records`. Let's examine the items that they've purchased.

The `pandas` module has been imported under the alias `pd`. The DataFrame credit_records has already been imported.

<hr>

**Instructions 1/2**
* Select the column `item` from `credit_records` using brackets and string notation.
* Select the column `item` from `credit_records` using dot notation.

## Script
```
# Select the column item from credit_records
# Use brackets and string notation
items = credit_records['item']

# Display the results
print(items)
```
```
# Select the column item from credit_records
# Use dot notation
items = credit_records.item

# Display the results
print(items)
```

## Output
```
<script.py> output:
    0          broccoli
    1       fizzy drink
    2          broccoli
    3          broccoli
    4             shirt
    5            burger
    6             fries
    7             pants
    8             shirt
    9             shirt
    10            pants
    11      fizzy drink
    12          carwash
    13     cheeseburger
    14            pants
    15     cheeseburger
    16         broccoli
    17          carwash
    18      fizzy drink
    19            shirt
    20      fizzy drink
    21          carwash
    22             eggs
    23           burger
    24     cheeseburger
    25           cheese
    26            fries
    27           cheese
    28            dress
    29            dress
               ...
    74           cheese
    75             milk
    76            dress
    77     cheeseburger
    78            shirt
    79            pants
    80            pants
    81         broccoli
    82            shirt
    83            fries
    84            dress
    85            pants
    86             milk
    87              gas
    88            fries
    89              gas
    90            fries
    91           burger
    92            pants
    93             milk
    94      fizzy drink
    95     cheeseburger
    96        cucumbers
    97      fizzy drink
    98            pants
    99            shirt
    100           pants
    101           dress
    102          burger
    103       cucumbers
    Name: item, Length: 104, dtype: object
```