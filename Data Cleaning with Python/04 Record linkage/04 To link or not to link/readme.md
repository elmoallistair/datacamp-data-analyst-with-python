## To link or not to link?

Similar to joins, record linkage is the act of linking data from different sources regarding the same entity. But unlike joins, record linkage does not require exact matches between different pairs of data, and instead can find close matches using string similarity. This is why record linkage is effective when there are no common unique keys between the data sources you can rely upon when linking data sources such as a unique identifier.

In this exercise, you will classify each card whether it is a traditional join problem, or a record linkage one.

<hr>

**Instructions**
* Classify each card into a problem that requires record linkage or regular joins.

**Answer**

**Record linkage**
* Two customer DataFrames containing names and address, one with a unique identifier peer customer, one without.
* Using an `address` column to join two DataFrames, with the address in each DataFrame being formatted slightly diferently.
* Merging two basketball DataFrames, with columns `team_A`, `team_B`, and `time` and differently formatted team names between each DataFrame.

**Regular joins**

* Two basketball DataFrames with a common unque. identifier per game
* Consolidating two DataFrames containing details on DataCamp courses, with each DataCamp course having its own unique identifier.