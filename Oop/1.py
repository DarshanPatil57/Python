#1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.


# model = input('Enter model name : ')
# brand = input('Enter brand name : ')

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model


my_car = Car("Honda","001")

# print(my_car)
print(my_car.brand)
print(my_car.model)
        