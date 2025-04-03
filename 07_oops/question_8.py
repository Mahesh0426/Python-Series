# class Inheritance and instance() Function
#Demonstrate the use of isintance() function to check if my_tesla is an instance of Car and ElectricCar.

class Car:
    def __init__(self,userbrand, usermodel):
        self.__brand = userbrand
        self.__model= usermodel
   
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    @property
    def model(self):
        return self.__model
    
 
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

 
    def full_name(self):
        return f"{self.brand} {self.model} with a battery size of {self.battery_size}"
        
    
    

# my_car =  Car("Toyota", "Corolla") # object of parent class
# # print(my_car.brand)
# # my_car.model = "Tiago"
# print(my_car.model)
# print(my_car.full_name())

 

my_new_car = ElectricCar("tesla", "S 1", "100 kWh")  # object of child class
print(isinstance(my_new_car, ElectricCar))  # True
print(isinstance(my_new_car, Car))  # True
# print(my_new_car.model)
# print(my_new_car.brand)
# print(my_new_car.full_name())


