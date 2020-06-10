# A taste of things to come

Congrats on making it to the end of the course! By now you should have a good understanding of the basics of SQL.

There's one more concept we're going to introduce. You may have noticed that all your results so far have been from just one table, e.g. `films` or `people`.

In the real world however, you will often want to query multiple tables. For example, what if you want to see the IMDB score for a particular movie?

In this case, you'd want to get the ID of the movie from the `films` table and then use it to get IMDB information from the `reviews` table. In SQL, this concept is known as a **join**, and a basic join is shown in the editor to the right.

The query in the editor gets the IMDB score for the film *To Kill a Mockingbird*! Cool right?

As you can see, joins are incredibly useful and important to understand for anyone using SQL.

We have a whole follow-up course dedicated to them called [Joining Data in PostgreSQL](https://www.datacamp.com/courses/joining-data-in-postgresql) for you to hone your database skills further!

<hr>

**Instructions**

* Submit the code in the editor and inspect the results.

**Question**
> 
> What is the IMDB score for the film *To Kill a > Mockingbird*?
> 
> **Possible Answers**
> * 8.1
> * 8.4
> * 7.7
> * 9.3
> 
> **Answer**
> > 8.4

## query.sql
```
SELECT title, imdb_score
FROM films
JOIN reviews
ON films.id = reviews.film_id
WHERE title = 'To Kill a Mockingbird';
```