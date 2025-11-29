# Encapsulation -
# Hide the data members(class variables, instance variables)
# by using only the methods.


class car:
    def __init__(self):
        self.public_karan ="karan"
        self.__private_baby ="Pass123"

    def nany(self):
        self.__private_password ="234"

object_ref = car()

print(object_ref.public_karan)
print(object_ref.nany())

#print(object_ref.__private_baby)