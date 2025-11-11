square ={ x**2 for x in range(5) }
print(square)

square2 = {1}
for i in range(5):
    square2.add(i**2)
print(square2)


fset = frozenset({1,2,3,4})
print(fset)