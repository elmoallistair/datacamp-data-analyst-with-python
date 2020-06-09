## Reindexing DataFrame from a list

Sorting methods are not the only way to change DataFrame Indexes. There is also the `.reindex()` method.

In this exercise, you'll reindex a DataFrame of quarterly-sampled mean temperature values to contain monthly samples (this is an example of *upsampling* or increasing the rate of samples, which you may recall from the [pandas Foundations](https://www.datacamp.com/courses/pandas-foundations) course).

The original data has the first month's abbreviation of the quarter (three-month interval) on the Index, namely `Apr`, `Jan`, `Jul`, and `Oct`. This data has been loaded into a DataFrame called `weather1` and has been printed in its entirety in the IPython Shell. Notice it has only four rows (corresponding to the first month of each quarter) and that the rows are not sorted chronologically.

You'll initially use a list of all twelve month abbreviations and subsequently apply the `.ffill()` method to *forward-fill* the null entries when upsampling. This list of month abbreviations has been pre-loaded as `year`.

<hr>

**Instructions**
* Reorder the rows of `weather1` using the `.reindex()` method with the list `year` as the argument, which contains the abbreviations for each month.
* Reorder the rows of `weather1` just as you did above, this time chaining the `.ffill()` method to replace the null values with the last preceding non-null value.

## Script
```
# Import pandas
import pandas as pd

# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)

# Print weather2
print(weather2)

# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather1.reindex(year).ffill()

# Print weather3
print(weather3)
```

## Output
```
<script.py> output:
           Mean TemperatureF
    Month
    Jan            32.133333
    Feb                  NaN
    Mar                  NaN
    Apr            61.956044
    May                  NaN
    Jun                  NaN
    Jul            68.934783
    Aug                  NaN
    Sep                  NaN
    Oct            43.434783
    Nov                  NaN
    Dec                  NaN
           Mean TemperatureF
    Month
    Jan            32.133333
    Feb            32.133333
    Mar            32.133333
    Apr            61.956044
    May            61.956044
    Jun            61.956044
    Jul            68.934783
    Aug            68.934783
    Sep            68.934783
    Oct            43.434783
    Nov            43.434783
    Dec            43.434783
```