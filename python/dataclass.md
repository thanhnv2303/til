# Use Dataclass to automatically create special functions

Python's DataClass Module are similar to [Java's Lombok decorators](../java/lombok.md). Automatically creates the following special methods for a class:

-   `__init__`
-   `__repr__()`
-   `__eq__()`
-   `__lt()`, `__le()`, `__gt()`, `__ge()` (if the argument `order=True` is passed in the decorator)

Example:

```py
from dataclasses import dataclass

@dataclass
class Node:
    foo: str
    bar: int

n = Node('baz', 1)

print(n) # Node(foo='baz', bar=1)
```

Source: [dataclasses — Data Classes — Python 3.10.5 documentation](https://docs.python.org/3/library/dataclasses.html)
