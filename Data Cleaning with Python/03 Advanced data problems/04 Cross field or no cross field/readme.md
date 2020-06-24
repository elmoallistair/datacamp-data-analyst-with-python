## Cross field or no cross field?

Throughout this course, you've been immersed in a variety of data cleaning problems from range constraints, data type constraints, uniformity and more.

In this lesson, you were introduced to cross field validation as a means to sanity check your data and making sure you have strong data integrity.

Now, you will map different applicable concepts and techniques to their respective categories.

<hr>

**Instructions**

* Map different applicable concepts and techniques to their respective categories.

**Answer**

> **Cross field validation**
> 
> * Confirming the Age provided by users by cross checking their birthdays.
> * Row wise operations such as `.sum(axis = 1)`.
> 
> **Not cross field validation**
> 
> * Making sure a `subscription_date` column has no values set in the future.
> * Making sure that a `revenue` column is a numeric column.
> * The use of the `.astype()` method.