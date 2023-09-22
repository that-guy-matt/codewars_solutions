# Reduce but Grow

## Description
Given a non-empty array of integers, return the result of multiplying the values together in order. 

Example:
```python
[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
```

---

## Given Code

```python
def grow(arr):
    pass
```

---

## Solution

```python
def grow(arr):
    total = 1
    for i in arr:
        total *= i
    return total
```