## CSV to DataFrame

You work for an airline, and your manager has asked you to do a competitive analysis and see how often passengers flying on other airlines are involuntarily bumped from their flights. You got a CSV file (`airline_bumping.csv`) from the Department of Transportation containing data on passengers that were involuntarily denied boarding in 2016 and 2017, but it doesn't have the exact numbers you want. In order to figure this out, you'll need to get the CSV into a pandas DataFrame and do some manipulation!

`pandas` is imported for you as `pd`. `"airline_bumping.csv"` is in your working directory.

<hr>

**Instructions 1/4**
* Read the CSV file `"airline_bumping.csv"` and store it as a DataFrame called `airline_bumping`.
* Print the first few rows of `airline_bumping`.

**Instructions 2/4**
* For each airline group, select the `nb_bumped`, and `total_passengers` columns, and calculate the sum (for both years). Store this as `airline_totals`.

**Instructions 3/4**
* Create a new column of `airline_totals` called `bumps_per_10k`, which is the number of passengers bumped per 10,000 passengers in 2016 and 2017.

**Instructions 4/4**
* Print `airline_totals` to see the results of your manipulations.


## Script
```
# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv('airline_bumping.csv')

# Take a look at the DataFrame
print(airline_bumping.head())
```
```
# From previous step
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby('airline')[['nb_bumped','total_passengers']].sum()
```
```
# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals['nb_bumped'] / airline_totals['total_passengers'] * 10000
```
```
# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)
```


## Output
```
<script.py> output:
                 airline  year  nb_bumped  total_passengers
    0    DELTA AIR LINES  2017        679          99796155
    1     VIRGIN AMERICA  2017        165           6090029
    2    JETBLUE AIRWAYS  2017       1475          27255038
    3    UNITED AIRLINES  2017       2067          70030765
    4  HAWAIIAN AIRLINES  2017         92           8422734
                         nb_bumped  total_passengers  bumps_per_10k
    airline
    ALASKA AIRLINES           1392          36543121          0.381
    AMERICAN AIRLINES        11115         197365225          0.563
    DELTA AIR LINES           1591         197033215          0.081
    EXPRESSJET AIRLINES       3326          27858678          1.194
    FRONTIER AIRLINES         1228          22954995          0.535
    HAWAIIAN AIRLINES          122          16577572          0.074
    JETBLUE AIRWAYS           3615          53245866          0.679
    SKYWEST AIRLINES          3094          47091737          0.657
    SOUTHWEST AIRLINES       18585         228142036          0.815
    SPIRIT AIRLINES           2920          32304571          0.904
    UNITED AIRLINES           4941         134468897          0.367
    VIRGIN AMERICA             242          12017967          0.201
```