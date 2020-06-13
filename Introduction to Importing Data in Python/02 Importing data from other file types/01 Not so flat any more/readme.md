## Not so flat any more

In Chapter 1, you learned how to use the IPython magic command `! ls` to explore your current working directory. You can also do this natively in Python using the library [`os`](https://docs.python.org/2/library/os.html), which consists of miscellaneous operating system interfaces.

The first line of the following code imports the library `os`, the second line stores the name of the current directory in a string called `wd` and the third outputs the contents of the directory in a list to the shell.

> import os\
> wd = os.getcwd()\
> os.listdir(wd)

Run this code in the IPython shell and answer the following questions. Ignore the files that begin with `.`.

<hr>

Check out the contents of your current directory and answer the following questions: (1) which file is in your directory and NOT an example of a flat file; (2) why is it not a flat file?

**Possible Answers**

* `database.db` is not a flat file because relational databases contain structured relationships and flat files do not.
* `battledeath.xlsx` is not a flat because it is a spreadsheet consisting of many sheets, not a single table.
* `titanic.txt` is not a flat file because it is a `.txt`, not a `.csv`.

**Answer**

> `battledeath.xlsx` is not a flat because it is a spreadsheet consisting of many sheets, not a single table.