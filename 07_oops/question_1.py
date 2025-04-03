# Create a Car class with attributes like  brand and model. Then create an instance of this class.
class Car:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model= usermodel
        
my_car =  Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("tata", "Safari")
print(my_new_car.model)
print(my_new_car.brand)