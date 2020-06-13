## Working with mixed datatypes (1)

Much of the time you will need to import datasets which have different datatypes in different columns; one column may contain strings and another floats, for example. The function `np.loadtxt()` will freak at this. There is another function, `np.genfromtxt()`, which can handle such structures. If we pass `dtype=None` to it, it will figure out what types each column should be.

Import `'titanic.csv'` using the function `np.genfromtxt()` as follows:

> data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)

Here, the first argument is the filename, the second specifies the delimiter , and the third argument `names` tells us there is a header. Because the data are of different types, `data` is an object called a structured array. Because numpy arrays have to contain elements that are all the same type, the structured array solves this by being a 1D array, where each element of the array is a row of the flat file imported. You can test this by checking out the array's shape in the shell by executing `np.shape(data)`.

Accessing rows and columns of structured arrays is super-intuitive: to get the ith row, merely execute `data[i]` and to get the column with name 'Fare', execute `data['Fare']`.

<hr>

After importing the Titanic data as a structured array (as per the instructions above), print the entire column with the name `Survived` to the shell. What are the last 4 values of this column?

**Possible Answers**

* 1,0,0,1.
* 1,2,0,0.
* 1,0,1,0.
* 0,1,1,1.

**Answer**

> 1,0,1,0