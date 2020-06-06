## Selecting missing puppies

Let's return to our DataFrame of missing puppies, which is loaded as mpr. Let's select a few different rows to learn more about the other missing dogs.

<hr>

**Instructions**
* Select the dogs where `Age` is greater than `2`.
* Select the dogs whose `Status` is equal to `Still Missing`.
* Select all dogs whose `Dog` Breed is not equal to `Poodle`.

## Script
```
# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr['Status'] == 'Still Missing']
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)
```

## Output
```
<script.py> output:
      Dog Name             Owner Name       Dog Breed Status  Age
    2   Sparky             Dr. Apache   Border Collie  Found    3
    3  Theorem  Joseph-Louis Lagrange  French Bulldog  Found    4
    5    Benny   Hillary Green-Lerman          Poodle  Found    3
      Dog Name    Owner Name         Dog Breed         Status  Age
    0    Bayes      DataCamp  Golden Retriever  Still Missing    1
    1  Sigmoid                       Dachshund  Still Missing    2
    4      Ned  Tim Oliphant          Shih Tzu  Still Missing    2
      Dog Name             Owner Name         Dog Breed         Status  Age
    0    Bayes               DataCamp  Golden Retriever  Still Missing    1
    1  Sigmoid                                Dachshund  Still Missing    2
    2   Sparky             Dr. Apache     Border Collie          Found    3
    3  Theorem  Joseph-Louis Lagrange    French Bulldog          Found    4
    4      Ned           Tim Oliphant          Shih Tzu  Still Missing    2
```