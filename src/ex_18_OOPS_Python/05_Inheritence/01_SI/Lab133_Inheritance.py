class Father():
    def info(self):
        self.name ="BObby"
        self.age ="60"
        print(self.name)
        print(self.age)

class son(Father):
    def info2(self):
        self.name ="Karan"
        self.age ="31"
        print(self.name)
        print(self.age)

obj_ref = son()
obj_ref.info()
obj_ref.info2()