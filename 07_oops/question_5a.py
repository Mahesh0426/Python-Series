#class variable
# Add a  class variable to Car that  keeps track of the number of cars created.

class Car:
    total_car = 0
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand
        self.model= usermodel
        Car.total_car += 1
        
    def fuel_type(self):
        return "This car uses petrol or diesel."
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def full_name(self):
        return f"{self.brand} {self.model} with a battery size of {self.battery_size}"
        
    def fuel_type(self):
        return "This car uses electricity."
    

my_car =  Car("Toyota", "Corolla") # object of parent class

# print(my_car.full_name())
# print(my_car.fuel_type())

my_new_car = ElectricCar("tesla", "S 1", "100 kWh")  # object of child class


# print(my_new_car.full_name())
# print(my_new_car.fuel_type())

new_hundai_car = Car("Hundai", "Creta")

print(f"Total number of cars created: {Car.total_car}")
