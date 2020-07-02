## Filtering by multiple conditions

Which one of these commands would filter the `ri` DataFrame to only include female drivers who were stopped for a speeding violation?

**Possible Answers**

* `ri[(ri.driver_gender = 'F') & (ri.violation = 'Speeding')]`
* `ri[ri.driver_gender == 'F' & ri.violation == 'Speeding']`
* `ri[(ri.driver_gender == 'F') & (ri.violation == 'Speeding')]`
* `ri[(ri.driver_gender == 'F') | (ri.violation == 'Speeding')]`
* `ri[(ri.driver_gender == 'F') and (ri.violation == 'Speeding')]`

**Answer**

> `ri[(ri.driver_gender = 'F') & (ri.violation = 'Speeding')]`