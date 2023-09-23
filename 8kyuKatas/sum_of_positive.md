# Sum of Positive

## Description
You get an array of numbers, return the sum of all of the positives ones.

Example:
```python
[1,-4,7,12] => 1 + 7 + 12 = 20
```
Note: if there is nothing to sum, the sum is default to 0.

---

## Given Code

```python
def positive_sum(arr):
    # Your code here
    return 0

```

---

## Solution

```python
def positive_sum(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            sum += arr[i]
    return sum
```