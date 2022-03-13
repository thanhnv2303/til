# Default Dictionary Values

By default, it a Python dictionary does not contain a key, it returns `None`. This can be avoided by passing a second 'default' parameter to the `get()` method.

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
