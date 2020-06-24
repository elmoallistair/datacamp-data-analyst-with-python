## Ambiguous dates

You have a DataFrame containing a `subscription_date` column that was collected from various sources with different Date formats such as `YYYY-mm-dd` and `YYYY-dd-mm`. What is the best way to unify the formats for ambiguous values such as `2019-04-07`?

**Possible Answers**

* Set them to `NA` and drop them.
* Infer the format of the data in question by checking the format of subsequent and previous values.
* Infer the format from the original data source.
* All of the above are possible, as long as we investigate where our data comes from, and understand the dynamics affecting it before cleaning it.

**Answer**

> All of the above are possible, as long as we investigate where our data comes from, and understand the dynamics affecting it before cleaning it.