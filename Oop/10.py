# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


class Battery:
    def battery_info(self):
        return "This is battery info"

class Engine:
    def engine_info(self):
        return "This is engine info"

class ElectricCar(Battery,Engine):
    pass

my_car = ElectricCar()
print(my_car.battery_info())
print(my_car.engine_info())