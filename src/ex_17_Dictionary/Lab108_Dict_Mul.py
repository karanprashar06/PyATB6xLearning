student_infor1 ={
    "name" : "Karan",
    "age" : 31,
    "address" : {
        "city" : "Delhi",
        "state" : "New Delhi"
    }
}
student_infor2 ={
    "name" : "Akshay",
    "age" : 30,
    "address" : {
        "city" : "Hisar",
        "state" : "Haryana"
    }
}

#combined two dict in a single list
student_list = [student_infor1, student_infor2]
print(student_list)
print(student_list[0])
print(student_list[1]["name"])
print(student_list[1]["age"])
print(student_list[0]["address"]["city"])
print(student_list[1]["address"]["state"])

print(student_infor2["age"])