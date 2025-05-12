# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"
    
    def fuelType(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuelType(self):
        return "Electric charge"


my_car = Car("BMW", "007")
# print(my_car.fullname())
print( my_car.fullname() ,my_car.fuelType())

electric_car = ElectricCar("Tesla","T0001","80KWH")
# print(electric_car.brand , electric_car.model , electric_car.battery_size)
print(electric_car.fullname() ,electric_car.fuelType())