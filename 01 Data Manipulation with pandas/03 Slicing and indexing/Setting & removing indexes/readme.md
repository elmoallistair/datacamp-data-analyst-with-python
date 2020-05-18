## Setting & removing indexes

pandas allows you to designate columns as an index. This enables cleaner code when taking subsets (as well as providing more efficient lookup under some circumstances).

In this chapter, you'll be exploring `temperatures`, a DataFrame of average temperatures in cities around the world. `pandas` is loaded as `pd`.

<hr>

**Instructions**

* *Look at `temperatures`*.
* Set the index of `temperatures` to `"city"`, assigning to `temperatures_ind`.
* *Look at `temperatures_ind`. How is it different from `temperatures`?*
* Reset the index of `temperatures_ind`, keeping its contents.
* Reset the index of `temperatures_ind`, dropping its contents.

> **script.py**
> ```
> # Look at temperatures
> print(temperatures)
>
> # Index temperatures by city
> temperatures_ind = temperatures.set_index("city")
>
> # Look at temperatures_ind
> print(temperatures_ind)
>
> # Reset the index, keeping its contents
> print(temperatures_ind.reset_index())
>
> # Reset the index, dropping its contents
> print(temperatures_ind.reset_index(drop=True))
> ```
>
> **Output**
> ```
>             date     city        country  avg_temp_c
> 0     2000-01-01  Abidjan  Côte D'Ivoire      27.293
> 1     2000-02-01  Abidjan  Côte D'Ivoire      27.685
> 2     2000-03-01  Abidjan  Côte D'Ivoire      29.061
> 3     2000-04-01  Abidjan  Côte D'Ivoire      28.162
> 4     2000-05-01  Abidjan  Côte D'Ivoire      27.547
> ...          ...      ...            ...         ...
> 16495 2013-05-01     Xian          China      18.979
> 16496 2013-06-01     Xian          China      23.522
> 16497 2013-07-01     Xian          China      25.251
> 16498 2013-08-01     Xian          China      24.528
> 16499 2013-09-01     Xian          China         NaN
>
> [16500 rows x 4 columns]
>
>               date        country  avg_temp_c
> city
> Abidjan 2000-01-01  Côte D'Ivoire      27.293
> Abidjan 2000-02-01  Côte D'Ivoire      27.685
> Abidjan 2000-03-01  Côte D'Ivoire      29.061
> Abidjan 2000-04-01  Côte D'Ivoire      28.162
> Abidjan 2000-05-01  Côte D'Ivoire      27.547
> ...            ...            ...         ...
> Xian    2013-05-01          China      18.979
> Xian    2013-06-01          China      23.522
> Xian    2013-07-01          China      25.251
> Xian    2013-08-01          China      24.528
> Xian    2013-09-01          China         NaN
>
> [16500 rows x 3 columns]
>
>           city       date        country  avg_temp_c
> 0      Abidjan 2000-01-01  Côte D'Ivoire      27.293
> 1      Abidjan 2000-02-01  Côte D'Ivoire      27.685
> 2      Abidjan 2000-03-01  Côte D'Ivoire      29.061
> 3      Abidjan 2000-04-01  Côte D'Ivoire      28.162
> 4      Abidjan 2000-05-01  Côte D'Ivoire      27.547
> ...        ...        ...            ...         ...
> 16495     Xian 2013-05-01          China      18.979
> 16496     Xian 2013-06-01          China      23.522
> 16497     Xian 2013-07-01          China      25.251
> 16498     Xian 2013-08-01          China      24.528
> 16499     Xian 2013-09-01          China         NaN
>
> [16500 rows x 4 columns]
>
>             date        country  avg_temp_c
> 0     2000-01-01  Côte D'Ivoire      27.293
> 1     2000-02-01  Côte D'Ivoire      27.685
> 2     2000-03-01  Côte D'Ivoire      29.061
> 3     2000-04-01  Côte D'Ivoire      28.162
> 4     2000-05-01  Côte D'Ivoire      27.547
> ...          ...            ...         ...
> 16495 2013-05-01          China      18.979
> 16496 2013-06-01          China      23.522
> 16497 2013-07-01          China      25.251
> 16498 2013-08-01          China      24.528
> 16499 2013-09-01          China         NaN
>
> [16500 rows x 3 columns]
> ```