## Referential integrity violations

Given the current state of your database, what happens if you execute the following SQL statement?

```
DELETE FROM universities WHERE id = 'EPF';
```

**Possible Answers**

* It throws an error because the university with ID "EPF" does not exist.
* The university with ID "EPF" is deleted.
* It fails because referential integrity from `universities` to `professors` is violated.
* It fails because referential integrity from `professors` to `universities` is violated.

**Answer**

> It fails because referential integrity from `professors` to `universities` is violated.