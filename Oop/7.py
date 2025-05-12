# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"
    @staticmethod
    def general_description():
        return "Cars are means of Transport !"

my_car = Car("BMW", "007")
print(my_car.fullname())
# print(my_car.general_description())
print(Car.general_description())


# While using static method no need to use "self"