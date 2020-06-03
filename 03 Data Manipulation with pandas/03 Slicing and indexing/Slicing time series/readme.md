## Slicing time series

Slicing is particularly useful for time series, since it's a common thing to want to filter for data within a date range. Add the `date` column to the index, then use `.loc[]` to perform the subsetting. The important thing to remember is to keep your dates in ISO 8601 format, that is, `yyyy-mm-dd`.

Recall from Chapter 1 that you can combine multiple Boolean conditions using logical operators (such as `&`). To do so in one line of code you'll need to add parentheses `()` around each condition.

`pandas` is loaded as `pd` and `temperatures`, with no index, is available.

<hr>

**Instructions**

* Use Boolean conditions to subset for rows in 2010 and 2011, and print the results.
    * _Note that because the date isn't set as an index, a condition that contains only a year, such as `df['date'] == '2009'`, will check if the date is equal to the first day of the first month of the year (e.g. 2009-01-01), rather than checking whether the date occurs within the given year.
* Set the index to the `date` column.
* Use `.loc[]` to subset for rows in 2010 and 2011.
* Use `.loc[]` to subset for rows from Aug 2010 to Feb 2011.

> **script.py**
> ```
> # Use Boolean conditions to subset temperatures for rows in 2010 and > 2011
> print(temperatures[(temperatures["date"] >= "2010") & (temperatures> ["date"] < "2012")])
>
> # Set date as an index
> temperatures_ind = temperatures.set_index("date")
>
> # Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
> print(temperatures_ind.loc["2010":"2011"])
>
> # Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb > 2011
> print(temperatures_ind.loc["2010-08":"2011-02"])
> ```
>
> **Output**
> ```
>             date     city        country  avg_temp_c
> 120   2010-01-01  Abidjan  Côte D'Ivoire      28.270
> 121   2010-02-01  Abidjan  Côte D'Ivoire      29.262
> 122   2010-03-01  Abidjan  Côte D'Ivoire      29.596
> 123   2010-04-01  Abidjan  Côte D'Ivoire      29.068
> 124   2010-05-01  Abidjan  Côte D'Ivoire      28.258
> ...          ...      ...            ...         ...
> 16474 2011-08-01     Xian          China      23.069
> 16475 2011-09-01     Xian          China      16.775
> 16476 2011-10-01     Xian          China      12.587
> 16477 2011-11-01     Xian          China       7.543
> 16478 2011-12-01     Xian          China      -0.490
>
> [2400 rows x 4 columns]
>                city        country  avg_temp_c
> date
> 2010-01-01  Abidjan  Côte D'Ivoire      28.270
> 2010-02-01  Abidjan  Côte D'Ivoire      29.262
> 2010-03-01  Abidjan  Côte D'Ivoire      29.596
> 2010-04-01  Abidjan  Côte D'Ivoire      29.068
> 2010-05-01  Abidjan  Côte D'Ivoire      28.258
> ...             ...            ...         ...
> 2011-08-01     Xian          China      23.069
> 2011-09-01     Xian          China      16.775
> 2011-10-01     Xian          China      12.587
> 2011-11-01     Xian          China       7.543
> 2011-12-01     Xian          China      -0.490
>
> [2400 rows x 3 columns]
>                city        country  avg_temp_c
> date
> 2010-08-01  Abidjan  Côte D'Ivoire      25.400
> 2010-09-01  Abidjan  Côte D'Ivoire      25.710
> 2010-10-01  Abidjan  Côte D'Ivoire      26.397
> 2010-11-01  Abidjan  Côte D'Ivoire      27.446
> 2010-12-01  Abidjan  Côte D'Ivoire      27.666
> ...             ...            ...         ...
> 2010-10-01     Xian          China      12.292
> 2010-11-01     Xian          China       6.742
> 2010-12-01     Xian          China       0.845
> 2011-01-01     Xian          China      -4.811
> 2011-02-01     Xian          China       2.430
>
> [700 rows x 3 columns]
> ```