## Using File to import HDF5 files

The `h5py` package has been imported in the environment and the file L`IGO_data.hdf5` is loaded in the object `h5py_file`.

<hr>

What is the correct way of using the h5py function, `File()`, to import the file in `h5py_file` into an object, `h5py_data`, for *reading* only?

**Possible Answers**

* `h5py_data = File(h5py_file, 'r')`
* `h5py_data = h5py.File(h5py_file, 'r')`
* `h5py_data = h5py.File(h5py_file, read)`
* `h5py_data = h5py.File(h5py_file, 'read')`

**Answer**

> `h5py_data = h5py.File(h5py_file, 'r')`