## Identify the primary key

Have a look at the example table from the previous video. As the database designer, you have to make a wise choice as to which column should be the primary key.

```
     license_no     | serial_no |    make    |  model  | year
--------------------+-----------+------------+---------+------
 Texas ABC-739      | A69352    | Ford       | Mustang |    2
 Florida TVP-347    | B43696    | Oldsmobile | Cutlass |    5
 New York MPO-22    | X83554    | Oldsmobile | Delta   |    1
 California 432-TFY | C43742    | Mercedes   | 190-D   |   99
 California RSK-629 | Y82935    | Toyota     | Camry   |    4
 Texas RSK-629      | U028365   | Jaguar     | XJS     |    4
```

<hr>

Which of the following column or column combinations could best serve as primary key?

**Possible Answers**

* PK = {make}
* PK = {model, year}
* PK = {license_no}
* PK = {year, make}

**Answer**

> PK = {license_no}