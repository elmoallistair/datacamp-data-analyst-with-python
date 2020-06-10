## SELECTing single columns

While SQL can be used to create and modify databases, the focus of this course will be *querying* databases. A *query* is a request for data from a database table (or combination of tables). Querying is an essential skill for a data scientist, since the data you need for your analyses will often live in databases.

In SQL, you can select data from a table using a `SELECT` statement. For example, the following query selects the `name` column from the `people` table:

> SELECT name\
> FROM people;

In this query, `SELECT` and `FROM` are called keywords. In SQL, keywords are not case-sensitive, which means you can write the same query as:

> select name\
> from people;

That said, it's good practice to make SQL keywords uppercase to distinguish them from other parts of your query, like column and table names.

It's also good practice (but not necessary for the exercises in this course) to include a semicolon at the end of your query. This tells SQL where the end of your query is!

Remember, you can see the results of executing your query in the **query result** tab to the right!

<hr>

**Instructions**
* Select the `title` column from the `films table`.
* Select the `release_year` column from the `films table`.
* Select the `name` of each person in the `people` table.

## query.sql
```
SELECT title FROM films
SELECT release_year FROM films
SELECT name FROM people
```