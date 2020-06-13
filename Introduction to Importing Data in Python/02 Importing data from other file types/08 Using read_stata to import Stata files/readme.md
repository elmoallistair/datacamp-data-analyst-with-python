## Using read_stata to import Stata files

The `pandas` package has been imported in the environment as `pd` and the file `disarea.dta` is in your working directory. The data consist of disease extents for several diseases in various countries (more information can be found [here](http://www.cid.harvard.edu/ciddata/geog/readme_disarea.html)).

<hr>

What is the correct way of using the `read_stata(`) function to import `disarea.dta` into the object `df`?

**Possible Answers**

* `df = 'disarea.dta'`
* `df = read_stata.pd('disarea.dta')`
* `df = pd.read_stata('disarea.dta')`
* `df = pd.read_stata(disarea.dta)`

**Answer**

> `df = pd.read_stata('disarea.dta')`