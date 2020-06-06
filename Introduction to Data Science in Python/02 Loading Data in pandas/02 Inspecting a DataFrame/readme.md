## Inspecting a DataFrame

We've loaded the credit card records of our four suspects into a DataFrame called `credit_records`. Let's learn more about the structure of this DataFrame.

The `pandas` module has been imported under the alias `pd`. The DataFrame `credit_records` has already been imported.

How many rows are in `credit_records`?

**Instructions 1/2**
* Use the `.info()` method to inspect the DataFrame `credit_records`

**Instructions 2/2**
> **Question**
> How many rows are in > `credit_records`?
>
> Possible Answers
> * 103
> * 104
> * 5
> * 64

## Script
```
#Use .info() to inspect the DataFrame credit_records
print(credit_records.info())
```

## Output
```
<script.py> output:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 104 entries, 0 to 103
    Data columns (total 5 columns):
    suspect     104 non-null object
    location    104 non-null object
    date        104 non-null object
    item        104 non-null object
    price       104 non-null float64
    dtypes: float64(1), object(4)
    memory usage: 4.1+ KB
    None
```

## Answer
> 104