## Subsetting with .loc[]

The killer feature for indexes is `.loc[]`: a subsetting method that accepts index values. When you pass it a single argument, it will take a subset of rows.

The code for subsetting using `.loc[]` can be easier to read than standard square bracket subsetting, which can make your code less burdensome to maintain.

`pandas` is loaded as `pd`. `temperatures` and `temperatures_ind` are available; the latter is indexed by `city`.

<hr>

**Instructions**

> * Create a list of cities to subset on: Moscow and Saint Petersburg. Assign to `cities`.
> * Use `[]` subsetting to filter `temperatures` for rows where the city column takes a value in `cities`.
> * Use `.loc[]` subsetting to filter temperatures_ind for rows where the city is in `cities`.
>
> **script.py**
> ```
> # Make a list of cities to subset on
> cities = ["Moscow", "Saint Petersburg"]
>
> # Subset temperatures using square brackets
> print(temperatures[temperatures["city"].isin(cities)])
>
> # Subset temperatures_ind using .loc[]
> print(temperatures_ind.loc[cities])
> ```
>
> **Output**
> ```
>             date              city country  avg_temp_c
> 10725 2000-01-01            Moscow  Russia      -7.313
> 10726 2000-02-01            Moscow  Russia      -3.551
> 10727 2000-03-01            Moscow  Russia      -1.661
> 10728 2000-04-01            Moscow  Russia      10.096
> 10729 2000-05-01            Moscow  Russia      10.357
> ...          ...               ...     ...         ...
> 13360 2013-05-01  Saint Petersburg  Russia      12.355
> 13361 2013-06-01  Saint Petersburg  Russia      17.185
> 13362 2013-07-01  Saint Petersburg  Russia      17.234
> 13363 2013-08-01  Saint Petersburg  Russia      17.153
> 13364 2013-09-01  Saint Petersburg  Russia         NaN
>
> [330 rows x 4 columns]
>                        date country  avg_temp_c
> city
> Moscow           2000-01-01  Russia      -7.313
> Moscow           2000-02-01  Russia      -3.551
> Moscow           2000-03-01  Russia      -1.661
> Moscow           2000-04-01  Russia      10.096
> Moscow           2000-05-01  Russia      10.357
> ...                     ...     ...         ...
> Saint Petersburg 2013-05-01  Russia      12.355
> Saint Petersburg 2013-06-01  Russia      17.185
> Saint Petersburg 2013-07-01  Russia      17.234
> Saint Petersburg 2013-08-01  Russia      17.153
> Saint Petersburg 2013-09-01  Russia         NaN
>
> [330 rows x 3 columns]
> ```