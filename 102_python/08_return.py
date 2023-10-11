
def my_sum(min,max):
    print(min,max)    
    sum = 0
    for x in range(min , max):
        sum += x
    return sum

result = my_sum(2,24)
print(result)
result_2 = my_sum(result, result + 3)
print(result_2)