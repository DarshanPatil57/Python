# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
    
    def fullname(self):
        return f"{self.brand} {self.__model}"
    
    @staticmethod
    def general_description():
        return "Cars are means of Transport !"
    
    @property
    def model(self):
        return self.__model


my_car = Car("BMW", "007")
# if model is creted befor we should not be able to change that : make it private then for read only make methods 
my_car.model = '000' 
print(my_car.fullname())
# print(my_car.__dict__)


print(Car.general_description())


# ❓Why does model not change, even though you assign to it?

# Because:
# self.__model is a private attribute (name-mangled).
# my_car.model = '000' creates a new public attribute model on the object, it does NOT overwrite __model.
# You're not changing the internal __model value — you're just adding a new attribute on the fly!


# Private attributes (__model) are protected via name mangling.

# When you do my_car.model = "000" without a property or setter, you don’t change __model, you just create a new attribute.

# To truly make it read-only or controlled, you should use @property.