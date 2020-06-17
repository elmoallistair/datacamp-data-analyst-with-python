## Pop quiz: Exploring your JSON

Load the JSON `'a_movie.json'` into a variable, which will be a dictionary. Do so by copying, pasting and executing the following code in the IPython Shell:

```
import json
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)
```

Print the values corresponding to the keys `'Title'` and `'Year'` and answer the following question about the movie that the JSON describes:

<hr>

Which of the following statements is true of the movie in question?

**Possible Answers**

* The title is 'Kung Fu Panda' and the year is 2010.
* The title is 'Kung Fu Panda' and the year is 2008.
* The title is 'The Social Network' and the year is 2010.
* The title is 'The Social Network' and the year is 2008.

Answer

> The title is 'The Social Network' and the year is 2010.