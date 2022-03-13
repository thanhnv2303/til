# Use Lombok to automatically define methods

The [Lombok Library](https://projectlombok.org/) automatically creates the `getter`, `setter`, `constructor`, `toString()`, `equals()`, `hashCode()`, and many more methods for a Java Class. It does so by providing decorators that can be applied to classes.

Some of the most useful ones are:

-   `@Getter`/`@Setter`: Creates getter and setter methods for a field/class.
-   `@NoArgsConstructor`/`@RequiredArgsConstructor`/`@AllArgsConstructor`: Creates constructor with different arguments.
-   `@ToString`: Creates a `toString()` method.
-   `@EqualsAndHashCode`: Creates `equals()` and `hashCode()` methods.
-   `@Data`: Combines all the above decorators. Only `@RequiredArgsConstructor` in constructors.

Example:

```java
import lombok.*;

@Data
class Node {
    private String foo;
    private int bar;
}

/* Usage */
Node n = new Node("baz", 1);
System.out.println(node); // Node(foo='baz', bar=1)
```
