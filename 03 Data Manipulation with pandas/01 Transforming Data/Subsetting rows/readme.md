## Subsetting rows

A large part of data science is about finding which bits of your dataset are interesting. One of the simplest techniques for this is to find a subset of rows that match some criteria. This is sometimes known as *filtering rows* or *selecting rows*.

There are many ways to subset a DataFrame, perhaps the most common is to use relational operators to return `True` or `False` for each row, then pass that inside square **brackets**.

```
dogs[dogs["height_cm"] > 60]
dogs[dogs["color"] == "tan"]
```

You can filter for multiple conditions at once by using the "logical and" operator, `&`.

```
dogs[(dogs["height_cm"] > 60) & (dogs["col_b"] == "tan")]
```

`homelessness` is available and `pandas` is loaded as `pd`.

<hr>

**Instructions 1/3**

Filter `homelessness` for cases where the number of individuals is greater than ten thousand, assigning to `ind_gt_10k`. *View the printed result*.

> **code.py**
> ```
> # Filter for rows where individuals is greater than 10000
> ind_gt_10k = homelessness[(homelessness["individuals"]) > 10000]
>
> # See the result
> print(ind_gt_10k)
> ```
>
> **Output**
> ```
>                 region       state  individuals  family_members  state_pop
> 4              Pacific  California     109008.0         20964.0   39461588
> 9       South Atlantic     Florida      21443.0          9587.0   21244317
> 32        Mid-Atlantic    New York      39827.0         52070.0   19530351
> 37             Pacific      Oregon      11139.0          3337.0    4181886
> 43  West South Central       Texas      19199.0          6111.0   28628666
> 47             Pacific  Washington      16424.0          5880.0    7523869
> ```

**Instructions 2/3**

Filter `homelessness` for cases where the USA Census region is `"Mountain"`, assigning to `mountain_reg`. *View the printed result*.

> **script.py**
> ```
> # Filter for rows where region is Mountain
> mountain_reg = homelessness[(homelessness["region"] == "Mountain")]
>
> # See the result
> print(mountain_reg)
> ```
>
> **Output**
> ```
>       region       state  individuals  family_members  state_pop
> 2   Mountain     Arizona       7259.0          2606.0    7158024
> 5   Mountain    Colorado       7607.0          3250.0    5691287
> 12  Mountain       Idaho       1297.0           715.0    1750536
> 26  Mountain     Montana        983.0           422.0    1060665
> 28  Mountain      Nevada       7058.0           486.0    3027341
> 31  Mountain  New Mexico       1949.0           602.0    2092741
> 44  Mountain        Utah       1904.0           972.0    3153550
> 50  Mountain     Wyoming        434.0           205.0     577601
> ```

**Instructions 3/3**

Filter `homelessness` for cases where the number of family members is less than one thousand and the region is `"Pacific"`, assigning to `fam_lt_1k_pac`. *View the printed result*.

> script.py
> ```
> # Filter for rows where family_members is less than 1000
> # and region is Pacific
> fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) &(homelessness["region"] == "Pacific")]
>
> # See the result
> print(fam_lt_1k_pac)
> ```
>
> Output
> ```
>     region   state  individuals  family_members  state_pop
> 1  Pacific  Alaska       1434.0           582.0     735139
> ```