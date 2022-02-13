# Finding the average of two very big integers

If we are dealing with two very big integers (like `uint32` or `uint64`), we can't just add them together and then divide by two as it would cause integer overflow leading to a wrong answer.

Instead, if we know which of the two is bigger, then we can calculate the width and halve it using:

```cpp
unsigned average(unsigned low, unsigned high) {
    return low + (high - low) / 2;
}
```

There's another way to do this which does not depend on knowing which of the two is bigger:

```cpp
unsigned average(unsigned a, unsigned b) {
    return (a / 2) + (b / 2) + (a & b & 1);
}
```

There's another technique to do so using technique in the style known as [SWAR](https://en.wikipedia.org/wiki/SWAR), which stands for "SIMD within a register".

```cpp
unsigned average(unsigned a, unsigned b) {
    return (a & b) + (a ^ b) / 2;
}
```

Source: [On finding the average of two unsigned integers without overflow](https://devblogs.microsoft.com/oldnewthing/20220207-00/?p=106223)
