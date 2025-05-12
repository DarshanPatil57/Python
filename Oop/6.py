# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.


class Car: 
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car +=1
    
    def fullname(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_car = Car("BMW", "007")

my_car_two = Car("Tata", "Nexon")

electric_car = ElectricCar("Tesla","T0001","80KWH")


print("Total Cars : ",Car.total_car)