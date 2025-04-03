#Static Method 
# Add a static method to the car class that returns a general description of a car.


class Car:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model= usermodel
        
    def fuel_type(self):
        return "This car uses petrol or diesel."
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def full_name(self):
        return f"{self.brand} {self.model} with a battery size of {self.battery_size}"
        
    def fuel_type(self):
        return "This car uses electricity."
    

my_car =  Car("Toyota", "Corolla") # object of parent class
# print(my_car.brand)
# print(my_car.model)
print(my_car.full_name())
# print(my_car.fuel_type())
print(my_car.general_description())

my_new_car = ElectricCar("tesla", "S 1", "100 kWh")  # object of child class
# print(my_new_car.model)
# print(my_new_car.brand)
print(my_new_car.full_name())
# print(my_new_car.fuel_type())
print(my_new_car.general_description())
