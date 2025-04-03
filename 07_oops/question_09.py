#Multiple Inheritance
# Create two class Battery and Engine , and let the ElectricCar class inherit from both of them.
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
    

class Battery:
    def battery_info(self):
        return "This is a battery class"
class Engine:
    def engine_info(self):
        return "This is an engine class"

#multiple inheritance
class ElectricCarTwo(Battery,Engine,Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla","Model S")  # object of child class
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())