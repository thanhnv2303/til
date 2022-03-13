# Python Dataclass

Python's DataClass Module are similar to [Java's Lombok decorators](../java/lombok.md). Automatically creates the following special methods for a class:

-   `__init__`
-   `__repr__()`
-   `__eq__()`
-   `__lt()`, `__le()`, `__gt()`, `__ge()` if `order=True` is passed.

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
