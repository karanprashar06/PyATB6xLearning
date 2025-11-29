a = 10 # Variable everywhere in the program

class Person:
    b=11 # Instance Variable , a variable which is declared in the class

    def print_info(self):
        c =20 #Local variable , a variable which is declared ina function which has scope of the function only
        print(c)
        print(a)
        print(self.b)

object_ref = Person()
object_ref.print_info()

print(a)
#print(b)
#print(c)