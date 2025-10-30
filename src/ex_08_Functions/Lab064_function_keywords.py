def display_information(name, role):
   #print("Name:", name, "Role:", role)
    print(f"Name: {name} Role: {role}")

display_information("John", "Admin")
display_information(role="Admin",name="peter")
display_information("ara","uality_analyst")


def display_information(name, role):
    print(f"Name : {name}, role is {role}")
    # print("Name: ", name, "role is ", role)


# display_information("Pramod", "QA")
# Better Version
display_information(name="Pramod2", role="QA2")
display_information(role="QA3", name="Pramod3")
display_information("QA4", "Pramod4")