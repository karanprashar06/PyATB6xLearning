class Person:
    #Attributes
    name = None
    age = None
    id = None
    email = None
    phone = None
    height = None
    address = None

    #Behaviour
    def talk(self): #self: This, self will be first argument in every behaviour.
        print("I can talk to you")

    def sleep(self,name):    #Arg with No Return
        print("I am a method")
        print("I can sleep",name)

    def sleep2(self,name):  #Arg with Return
        print("I am a method",name)
        return None

    def walk(self):
        print("I am a walking")

    def method_walk_return(self):
        return "I am a walking"

def func1():
    print("Outside func1")


#Create an object of the class
# ObjectRef = ClassName()-->Object

geeta = Person()
geeta.name = "Geeta"
geeta.age = 18
geeta.id = 1234
geeta.email = "mcmkcds@Csdc"
geeta.phone = "0123456789"
geeta.height = "12"
geeta.address = "123 Main St."

print(geeta.walk())
#print(geeta.method_walk_return())
print(geeta.name)
print(geeta.age)
print(geeta.id)