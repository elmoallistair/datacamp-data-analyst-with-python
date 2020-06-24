## Getting the right index

Here's a DataFrame named `matches` containing potential matches between two DataFrames, `users_1` and `users_2`. Each DataFrame's row indices is stored in `uid_1` and `uid_2` respectively.

```
             first_name  address_1  address_2  marriage_status  date_of_birth
uid_1 uid_2                                                                  
0     3              1          1          1                1              0
     ...            ...         ...        ...              ...            ...
     ...            ...         ...        ...              ...            ...
1     3              1          1          1                1              0
     ...            ...         ...        ...              ...            ...
     ...            ...         ...        ...              ...            ...
```

<hr>

How do you extract all values of the `uid_1` index column?

**Possible Answers**

* `matches.index.get_level_values(0)`
* `matches.index.get_level_values(1)`
* `matches.index.get_level_values('uid_1'`)
* `Both 1 and 3 are correct.`

**Answer**

> `Both 1 and 3 are correct.`
