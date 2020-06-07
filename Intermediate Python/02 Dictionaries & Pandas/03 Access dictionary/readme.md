## Access dictionary

If the keys of a dictionary are chosen wisely, accessing the values in a dictionary is easy and intuitive. For example, to get the capital for France from `europe` you can use:

> `europe['france']`

Here, `'france'` is the key and `'paris'` the value is returned.

**Instructions**
* Check out which keys are in europe by calling the keys() method on europe. Print out the result.
* Print out the value that belongs to the key 'norway'.

## Script
```
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])
```

## Output
```
<script.py> output:
    dict_keys(['spain', 'norway', 'france', 'germany'])
    oslo
```