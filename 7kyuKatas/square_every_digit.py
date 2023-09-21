def square_digits(num):
    string = str(num)
    answer = ""
    for i in range(len(string)):
        answer += str(int(string[i]) * int(string[i]))
    return int(answer)