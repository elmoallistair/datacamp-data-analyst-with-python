# It's AS simple AS aliasing

You may have noticed in the first exercise of this chapter that the column name of your result was just the name of the function you used. For example,

> SELECT MAX(budget)\
> FROM films;

gives you a result with one column, named `max`. But what if you use two functions like this?

> SELECT MAX(budget), MAX(duration)\
> FROM films;

Well, then you'd have two columns named `max`, which isn't very useful!

To avoid situations like this, SQL allows you to do something called *aliasing*. Aliasing simply means you assign a temporary name to something. To alias, you use the `AS` keyword, which you've already seen earlier in this course.

For example, in the above example we could use aliases to make the result clearer:

> SELECT MAX(budget) AS max_budget,\
>        MAX(duration) AS max_duration\
>FROM films;

Aliases are helpful for making results more readable!

<hr>

**Instructions**
* Get the title and net profit (the amount a film grossed, minus its budget) for all films. Alias the net profit as `net_profit`.
* Get the title and duration in hours for all films. The duration is in minutes, so you'll need to divide by 60.0 to get the duration in hours. Alias the duration in hours as `duration_hours`.
* Get the average duration in hours for all films, aliased as `avg_duration_hours`.


## query.sql
```
SELECT title, gross - budget AS net_profit FROM films
SELECT title, duration/60.0 AS duration_hours FROM films
SELECT AVG(duration) / 60.0 AS avg_duration_hours FROM films
```