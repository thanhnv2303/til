# Default Dictionary Values

There are two methods to get a value corresponding to a key in a dictionary `d` - `d[key]` and `d.get(key)`. The first method throws a `KeyError` when the key is not found in the dictionary, while the second method returns `None` if the key is not found.

The second method can be improved by passing a default value as a second argument like `d.get(key, default)`. This would return the default value if the key is not found in the dictionary.

There is a more elegant method to do this using the `colllection` library's `defaultdict` class.

Example:

```py
from collections import defaultdict

x = defaultdict(int)
print(x['key']) # prints 0 by default

x = defaultdict(list)
print(x['key']) # prints [] by default

# This is where things get interesting

def default_value() -> int:
    return 42

x = defaultdict(default_value)
print(x['key']) # prints 42 by default

x = defaultdict(lambda: 42)
print(x['key']) # prints 42 by default
```
