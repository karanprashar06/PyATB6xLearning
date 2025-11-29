class Calc:
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b



    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


a = float(input("Enter the value of a"))
b = float(input("Enter the value of b"))
object_Ref = Calc(a,b)
print(object_Ref.sub())
print(object_Ref.sum())
print(object_Ref.div())
print(object_Ref.mul())