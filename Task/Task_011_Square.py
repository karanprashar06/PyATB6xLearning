
#TASK 1

def squre(num):
    if num > 0:
        print(num **2)
    else:
        print("Enter a number greater than 0")

squre(int(input("Enter a positive number: ")))

#TASK 2

def triangle(side1, side2, side3):
    if side1 == side2 == side3:
        print("Triangle is Equilater")
    elif side1 == side2 or   side2 == side3 or side1 == side3:
        print("Triangle is Isosceles")
    else:
        print("Triangle is Scalene")

triangle(3,3,3)
triangle(3,3,4)
triangle(3,4,5)
