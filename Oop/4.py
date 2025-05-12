# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.


# Encapsulation is one of the core principles of object-oriented programming. It involves:
# Restricting direct access to some of an object’s attributes (i.e., making them private).
# Providing controlled access through methods (getters/setters).

# In Python:
# Prefixing an attribute with __ makes it private (e.g., self.__brand).
# A getter method is used to retrieve the value of that private attribute.

class Car: 
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def getBrand(self):
        return self.__brand 
    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    


my_car = Car("BMW", "007")
print("Full name : " ,my_car.fullname())
print("From get barnd : " ,my_car.getBrand())

# ⚠️ What happens if you try to access __brand directly?

# print(my_car.__brand)
# You’ll get an AttributeError because it's private:
# AttributeError: 'Car' object has no attribute '__brand'