# Powers of 2

## Description
Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).

Example:
```python
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
```

---

## Given Code

```python
def powers_of_two(n):
    return []
```

---

## Solution

```python
def powers_of_two(n):
    powers = []
    for i in range(n + 1):
        powers.append(2 ** i)
    return powers
```