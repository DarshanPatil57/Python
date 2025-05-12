# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car = Car("BMW", "007")


electric_car = ElectricCar("Tesla","T0001","80KWH")

print(isinstance(electric_car,Car))
print(isinstance(electric_car,ElectricCar)) 