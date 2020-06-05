## DataFrame to CSV

You're almost there! To make things easier to read, you'll need to sort the data and export it to CSV so that your colleagues can read it.

`pandas` as `pd` has been imported for you.

<hr>

**Instructions**

* Sort `airline_totals` by the values of `bumps_per_10k` from highest to lowest, storing as `airline_totals_sorted`.
* Print your sorted DataFrame.
* Save the sorted DataFrame as a CSV called `"airline_totals_sorted.csv"`.

## Script
```
# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values('bumps_per_10k', ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv('airline_totals_sorted.csv')
```

## Output
```
<script.py> output:
                         nb_bumped  total_passengers  bumps_per_10k
    airline
    EXPRESSJET AIRLINES       3326          27858678          1.194
    SPIRIT AIRLINES           2920          32304571          0.904
    SOUTHWEST AIRLINES       18585         228142036          0.815
    JETBLUE AIRWAYS           3615          53245866          0.679
    SKYWEST AIRLINES          3094          47091737          0.657
    AMERICAN AIRLINES        11115         197365225          0.563
    FRONTIER AIRLINES         1228          22954995          0.535
    ALASKA AIRLINES           1392          36543121          0.381
    UNITED AIRLINES           4941         134468897          0.367
    VIRGIN AMERICA             242          12017967          0.201
    DELTA AIR LINES           1591         197033215          0.081
    HAWAIIAN AIRLINES          122          16577572          0.074
```