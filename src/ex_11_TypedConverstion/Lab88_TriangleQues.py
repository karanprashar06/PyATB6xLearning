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