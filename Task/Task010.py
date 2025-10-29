#TASK1
#Print even numbers between 1 and 20

for i in range(1,21,1):
    if i % 2 == 0:
        print(i)




#TASK2
#Print numbers from 10 down to 1

for i in range(10,0,-1):
    print(i)


#TASK3
#Skip numbers divisible by 3, from (0,100)

for i in range(0,100):
    if i % 3 == 0:
        continue
    print(i)