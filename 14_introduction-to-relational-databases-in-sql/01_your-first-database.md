## Your first database

In this chapter, you'll create your very first database with a set of simple SQL commands. Next, you'll migrate data from existing flat tables into that database. You'll also learn how meta-information about a database can be queried.

<br>

### Query information_schema with SELECT

```
-- Query the right table in information_schema
SELECT table_name
FROM information_schema.tables
-- Specify the correct table_schema value
WHERE table_schema = 'public';

-- Query the right table in information_schema to get columns
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'university_professors' AND table_schema = 'public';

-- Query the first five rows of our table
SELECT *
FROM university_professors
LIMIT 5;
```

### CREATE your first few TABLEs

```
-- Create a table for the professors entity type
CREATE TABLE professors (
 firstname text,
 lastname text
);

-- Print the contents of this table
SELECT *
FROM professors

-- Create a table for the universities entity type
CREATE TABLE universities (
    university_shortname text,
    university text,
    university_city text
);

-- Print the contents of this table
SELECT *
FROM universities
```

### ADD a COLUMN with ALTER TABLE

```
-- Add the university_shortname column
ALTER TABLE professors
ADD COLUMN university_shortname text;

-- Print the contents of this table
SELECT *
FROM professors
```

### RENAME and DROP COLUMNs in affiliations

```
-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;

-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;
```

### Migrate data with INSERT INTO SELECT DISTINCT

```
-- Insert unique professors into the new table
INSERT INTO professors
SELECT DISTINCT firstname, lastname, university_shortname
FROM university_professors;

-- Doublecheck the contents of professors
SELECT *
FROM professors;

-- Insert unique affiliations into the new table
INSERT INTO affiliations
SELECT DISTINCT firstname, lastname, function, organization
FROM university_professors;

-- Doublecheck the contents of affiliations
SELECT *
FROM affiliations;
```

### Delete tables with DROP TABLE

```
-- Delete the university_professors table
DROP TABLE university_professors;
```