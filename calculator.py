class Claculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        sum = int(self.a) + int(self.b)
        return sum




a= input(("Enter The Value of A"))
b = input(("ENter the value of B "))

obj  =Claculator(a,b)
print(obj.add())

    