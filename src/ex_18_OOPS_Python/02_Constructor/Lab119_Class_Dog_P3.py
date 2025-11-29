class Dog:
    #A
    name= None
    breed= None
    age= None
    height= None
    weight= None

    def __init__(self, nameGiven,breedGiven):
        print("Param C")
        self.name = nameGiven
        self.breed = breedGiven

    #B
    def bark(self):
        print("barking")
    def talk(self):
        print("talking")
    def eat(self):
        print("who is eating->"+self.name)


captain = Dog("Captain","Pitbull")
sheru = Dog("Sheru","Indie")
captain.eat()
sheru.eat()
captain.bark()
captain.talk()