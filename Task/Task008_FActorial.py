print("Enter the number which Factorial You want to see")

num = int(input("Enter a number which fact you want to see: "))

fact =1

if num <1:
    print("Number is less than 1")
if num ==0:
    print("fact=", fact)
else:
    for i in range(1,num+1):
        fact = fact * i
print(fact)
