'''class A:
    a=33
    def __init__(self,a,b):
        print("Uncodemy")
#        print(a+b)
        self.a=a
        self.b=b
    def m1(self):
        print(self.a+self.b)

           
#obj=A()
obj=A(2,3)
obj.m1()


class Car:
    wheels=4
    def __init__(self,model,brand,fuelType):
        self.model=model
        self.brand=brand
        self.fuelType=fuelType

    def carInfo(self):
       
        print(f"{self.model} {self.brand} which is {self.fuelType} fuel-type has {self.wheels} wheels.")

obj=Car("2026","Maruti","Petrol")
obj.carInfo()

'''