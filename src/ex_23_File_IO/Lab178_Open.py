# t = open('testdata.txt', 'r')
# t = open('testdata.txt', 'w')
# t = open('testdata.txt', 'r+')
# t = open('testdata.txt', 'w+')
# t = open('testdata.txt', 'r')
# print(t)
# t.close()

# Automatically close
with open('testdata.txt', 'r') as f:
    data = f.read()
    data2 = f.readline()
    data3 = f.readlines()

print(data)
print(data2)
print(data3)