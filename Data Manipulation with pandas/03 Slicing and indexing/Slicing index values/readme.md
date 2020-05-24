## Slicing index values

Slicing lets you select consecutive elements of an object using `first:last` syntax. DataFrames can be sliced by index values, or by row/column number; we'll start with the first case. This involves slicing inside the `.loc[]` method.

Compared to slicing lists, there are a few things to remember.

* You can only slice an index if the index is sorted (using `.sort_index()`).
* To slice at the outer level, `first` and `last` can be strings.
* To slice at inner levels, `first` and `last` should be tuples.
* If you pass a single slice to `.loc[]`, it will slice the rows.

`pandas` is loaded as `pd`. `temperatures_ind` has country and city in the index, and is available.

**Instructions**
* Sort the index of `temperatures_ind`.
* Use slicing with `.loc[]` to get these subsets:
    * from Pakistan to Russia.
    * from Lahore to Moscow. (*This will return nonsense.*)
    * from Pakistan, Lahore to Russia, Moscow.

> **script.py**
> ```
> # Sort the index of temperatures_ind
> temperatures_srt = temperatures_ind.sort_index()
> 
> # Subset rows from Pakistan to Russia
> print(temperatures_srt.loc["Pakistan":"Russia"])
> 
> # Try to subset rows from Lahore to Moscow
> print(temperatures_srt.loc["Lahore":"Moscow"])
> 
> # Subset rows from Pakistan, Lahore to Russia, Moscow
> print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])
> ```
> 
> **Output**
> ```
>                                 date  avg_temp_c
> country  city
> Pakistan Faisalabad       2000-01-01      12.792
>          Faisalabad       2000-02-01      14.339
>          Faisalabad       2000-03-01      20.309
>          Faisalabad       2000-04-01      29.072
>          Faisalabad       2000-05-01      34.845
> ...                              ...         ...
> Russia   Saint Petersburg 2013-05-01      12.355
>          Saint Petersburg 2013-06-01      17.185
>          Saint Petersburg 2013-07-01      17.234
>          Saint Petersburg 2013-08-01      17.153
>          Saint Petersburg 2013-09-01         NaN
> 
> [1155 rows x 2 columns]
> 
>                          date  avg_temp_c
> country city
> Mexico  Mexico     2000-01-01      12.694
>         Mexico     2000-02-01      14.677
>         Mexico     2000-03-01      17.376
>         Mexico     2000-04-01      18.294
>         Mexico     2000-05-01      18.562
> ...                       ...         ...
> Morocco Casablanca 2013-05-01      19.217
>         Casablanca 2013-06-01      23.649
>         Casablanca 2013-07-01      27.488
>         Casablanca 2013-08-01      27.952
>         Casablanca 2013-09-01         NaN
> 
> [330 rows x 2 columns]
> 
>                       date  avg_temp_c
> country  city
> Pakistan Lahore 2000-01-01      12.792
>          Lahore 2000-02-01      14.339
>          Lahore 2000-03-01      20.309
>          Lahore 2000-04-01      29.072
>          Lahore 2000-05-01      34.845
> ...                    ...         ...
> Russia   Moscow 2013-05-01      16.152
>          Moscow 2013-06-01      18.718
>          Moscow 2013-07-01      18.136
>          Moscow 2013-08-01      17.485
>          Moscow 2013-09-01         NaN
> 
> [660 rows x 2 columns]
> ```