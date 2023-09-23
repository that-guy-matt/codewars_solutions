def smash(words):
    s = ''
    for i in range(len(words)):
        s += words[i]
        if i != len(words)-1:
            s += ' '
    return s