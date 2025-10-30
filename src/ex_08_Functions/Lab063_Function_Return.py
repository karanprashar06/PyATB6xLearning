def math1(a, b):
    return a + b
sum = math1(1, 2)
print(sum)

#Multiple return
def math2(a,b):
    return a + b,a-b,a*b,a/b

sum_r,sub_r,mul_r,div_r = math2(1,2)
print(sum_r)
print(sub_r)
print(mul_r)
print(div_r)