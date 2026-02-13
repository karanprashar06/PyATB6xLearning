class Dog:
    #A
    name=None
    age=None
    breed=None
    height=None
    weight=None

    #B
    def bark(self,name):
        print("barking")
        print(name)
        print(self.name)

    def talk(self):
        print("talking")

captain = Dog()
captain.name = "pineapple"
captain.bark("ok")
captain.talk()
