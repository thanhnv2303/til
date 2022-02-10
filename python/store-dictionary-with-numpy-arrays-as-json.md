# Store a Dictionary with Numpy Arrays as a JSON object

Dictionaries with Numpy Arrays in it cannot be stored as a JSON object by default. Therefore, to so store it as JSON, we need to convert all the Numpy arrays inside the dictionary to lists. This can be done by using the following code:

```python
import json
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

# Pass this class name as a value to the 'cls' parameter
# of the json.dump() or the json.dumps() function

# Example

array = np.array([[1, 2, 3], [4, 5, 6]])
dictionary = {
    'array': array,
    'array inside a list': [array],
    'array inside a tuple inside a list': [1, (2, 3, 4, array)]
}
json_string = json.dumps(dictionary, cls=NumpyEncoder)
print(json_string)

"""
Output:
{
  "array": [[1, 2, 3], [4, 5, 6]],
  "array inside a list": [[[1, 2, 3], [4, 5, 6]]],
  "array inside a tuple inside a list": [1, [2, 3, 4, [[1, 2, 3], [4, 5, 6]]]]
}
"""
```

Source: https://stackoverflow.com/a/47626762/10307491
