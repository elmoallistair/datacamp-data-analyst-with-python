# GROUP BY

Now you know how to sort results! Often you'll need to aggregate results. For example, you might want to count the number of male and female employees in your company. Here, what you want is to group all the males together and count them, and group all the females together and count them. In SQL, `GROUP BY` allows you to group a result by one or more columns, like so:

> SELECT sex, count(*)\
> FROM employees\
> GROUP BY sex;

This might give, for example:
| sex    | count |
|--------|-------|
| male   | 15    |
| female | 19    |

Commonly, `GROUP BY` is used with *aggregate* functions like `COUNT()` or `MAX()`. Note that `GROUP BY` always goes after the `FROM` clause!

<hr>

What is `GROUP BY` used for?

**Possible Answers**
* Performing operations by column
* Performing operations all at once
* Performing operations in a particular order
* Performing operations by group

**Answer**
> Performing operations by group
