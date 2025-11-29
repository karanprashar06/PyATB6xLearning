class Bio_data:
    def __init__(self, name, age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def print_info(self):
        print("Name of the person"+self.name)
        print("Age of the person"+self.age)
        print("Occupation of the person"+self.occupation)

o_ref = Bio_data("Karan", "31","Qa Lead")
o_ref.print_info()

o_ref1 = Bio_data("Akshay", "30","Director")
o_ref1.print_info()