## Loading a DataFrame

We're still working hard to solve the kidnapping of Bayes, the Golden Retriever. Previously, we used a license plate spotted at the crime scene to narrow the list of suspects to:

* Fred Frequentist
* Ronald Aylmer Fisher
* Gertrude Cox
* Kirstine Smith

We've obtained credit card records for all four suspects. Perhaps some of them made suspicious purchases before the kidnapping?

The records are in a CSV called `"credit_records.csv"`.

<hr>

**Instructions**
* Import the `pandas` module under the alias `pd`.
* Load the CSV `"credit_records.csv"` into a DataFrame called `credit_records`.
* Display the first five rows of `credit_records` using the `.head()` method.

## Script
```
# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv('credit_records.csv')

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())
```

## Output
```
<script.py> output:
                suspect         location              date         item  price
    0    Kirstine Smith   Groceries R Us   January 6, 2018     broccoli   1.25
    1      Gertrude Cox  Petroleum Plaza   January 6, 2018  fizzy drink   1.90
    2  Fred Frequentist   Groceries R Us   January 6, 2018     broccoli   1.25
    3      Gertrude Cox   Groceries R Us  January 12, 2018     broccoli   1.25
    4    Kirstine Smith    Clothing Club   January 9, 2018        shirt  14.25
```