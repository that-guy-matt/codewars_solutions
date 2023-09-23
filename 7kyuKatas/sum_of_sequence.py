def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        sum = 0
        num = begin_number
        while num <= end_number:
            num += step 
            sum += begin_number
            begin_number = num  
        return sum
