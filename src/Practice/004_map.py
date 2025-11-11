import math
number = [1,2,3,4,5]
print(number)

def square(x):
    return x*x

up_list = list(map(square, number))
print(up_list)