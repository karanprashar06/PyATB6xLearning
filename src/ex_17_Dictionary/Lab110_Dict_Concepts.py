from heapq import merge

key=["Name","Age","Address"]
value = ["Karan",31,"Delhi","abc"]

my_dicgt = dict(zip(key,value))
print(my_dicgt)

tom=["Name","Age","Address"]
jerry = ["Karan",31,"Delhi","abc"]

my_dict = dict(zip(tom,jerry))
print(my_dict)

#Merge Two Dictionaries
dict1 ={"Name":"Karan","age":31}
dict2 ={"Name1":"Akshay","age1":30}

ok =merge(dict1,dict2)
print(ok)


#By the use of union operator
merge_dict = dict1 | dict2
print(merge_dict)

print(merge_dict.get("age"))
print(merge_dict.get("Name"))
print(merge_dict.get("Address"))