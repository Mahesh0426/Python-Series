#Encapsulation
#Modify the CAr class to encapsuleate the brand attribute, making it private , and provide a getter method for it.
#inheritane
#Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
class Car:
    def __init__(self,userbrand, usermodel):
        self.__brand = userbrand # Private attribute by using double underscore
        self.model= usermodel  # Public attribute
        

        #getter method
    def get_brand(self):
        return self.__brand + " is the brand of the car"

    def full_name(self):
        return f"{self.__brand} {self.model}"



my_car =  Car("Toyota", "Corolla")
# print(my_car.__brand)
# print(my_car.model)
print(my_car.get_brand())
 

