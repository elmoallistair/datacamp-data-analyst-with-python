## Narrowing the list of suspects

In Chapter 1, we found a list of people whose cars matched the description of the one that kidnapped Bayes:

* Fred Frequentist
* Ronald Aylmer Fisher
* Gertrude Cox
* Kirstine Smith

We'd like to narrow this list down, so we obtained credit card records for each suspect. We'd like to know if any of them recently purchased dog treats to use in the kidnapping. If they did, they would have visited `'Pet Paradise'`.

The credit records have been loaded into a DataFrame called credit_records.

<hr>

**Instructions 1/2**
* Select rows of `credit_records` such that the column `location` is equal to `'Pet Paradise'`.

**Instructions 2/2**
> **Question**
>
> Which suspects purchased pet supplies before > the kidnapping?
>
> **Possible Answers**
> * Fred Frequentist and Ronald Aylmer Fisher
> * Gertrude Cox and Kirstine Smith
> * Fred Frequentist and Gertrude Cox
> * Ronald Aylmer Fisher and Kirstine Smith

## Script
```
# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.location == 'Pet Paradise']

# Display
print(purchase)
```

## Output
```
<script.py> output:
                 suspect      location              date          item  price
    8   Fred Frequentist  Pet Paradise  January 14, 2018    dog treats   8.75
    9   Fred Frequentist  Pet Paradise  January 14, 2018    dog collar  12.25
    28      Gertrude Cox  Pet Paradise  January 13, 2018  dog chew toy   5.95
    29      Gertrude Cox  Pet Paradise  January 13, 2018    dog treats   8.75
```

## Answer
>