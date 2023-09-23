# String Repeat

## Description
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Example (input -> output):
```python
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
```

---

## Given Code

```python
def repeat_str(repeat, string):
    return ''
```

---

## Solution

```python
def repeat_str(n, s):
    final = ''
    for i in range(n):
        final += s
    return final
```