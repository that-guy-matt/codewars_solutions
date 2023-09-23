# Double Char

## Description
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Example (Input -> Output):
```python
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
```

---

## Given Code

```python
def double_char(s):
    pass
```

---

## Solution

```python
def double_char(s):
    #new string to be filled
    newString = ""
    #iterate through each character in s
    for char in s:
        #add each character twice to new string
        newString += char * 2
    return newString 
```