def double_char(s):
    #new string to be filled
    newString = ""
    #iterate through each character in s
    for char in s:
        #add each character twice to new string
        newString += char * 2
    return newString 