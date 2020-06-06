## Correcting column selection errors

A junior detective tried to access the location columns of `credit_records`, but he made some mistakes. Help correct his code so that we can search for suspicious purchases.

In all exercises going forward, `pandas` will be imported as `pd`. The DataFrame `credit_records` has already been imported.

<hr>

**Instructions**
* Correct the code so that it runs without errors.

## Script
```
# One or more lines of code contain errors.
# Fix the errors so that the code runs.

# Select the location column in credit_records
location = credit_records['location']

# Select the item column in credit_records
items = credit_records.item

# Display results
print(location)
```

## Output
```
<script.py> output:
    0       Groceries R Us
    1      Petroleum Plaza
    2       Groceries R Us
    3       Groceries R Us
    4        Clothing Club
    5          Burger Mart
    6          Burger Mart
    7        Clothing Club
    8        Clothing Club
    9        Clothing Club
    10       Clothing Club
    11     Petroleum Plaza
    12     Petroleum Plaza
    13         Burger Mart
    14       Clothing Club
    15         Burger Mart
    16      Groceries R Us
    17     Petroleum Plaza
    18     Petroleum Plaza
    19       Clothing Club
    20     Petroleum Plaza
    21     Petroleum Plaza
    22      Groceries R Us
    23         Burger Mart
    24         Burger Mart
    25      Groceries R Us
    26         Burger Mart
    27      Groceries R Us
    28       Clothing Club
    29       Clothing Club
                ...
    74      Groceries R Us
    75      Groceries R Us
    76       Clothing Club
    77         Burger Mart
    78       Clothing Club
    79       Clothing Club
    80       Clothing Club
    81      Groceries R Us
    82       Clothing Club
    83         Burger Mart
    84       Clothing Club
    85       Clothing Club
    86      Groceries R Us
    87     Petroleum Plaza
    88         Burger Mart
    89     Petroleum Plaza
    90         Burger Mart
    91         Burger Mart
    92       Clothing Club
    93      Groceries R Us
    94     Petroleum Plaza
    95         Burger Mart
    96      Groceries R Us
    97     Petroleum Plaza
    98       Clothing Club
    99       Clothing Club
    100      Clothing Club
    101      Clothing Club
    102        Burger Mart
    103     Groceries R Us
    Name: location, Length: 104, dtype: object
```