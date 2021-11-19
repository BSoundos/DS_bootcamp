# 1/ Write a Python class named Rectangle constructed by a length and width 
#and a method which will compute the area of a rectangle.

class Rectangle(): 

    def __init__(self,length,width):
        self.length = length 
        self.width = width 
    
    def Rectangle_Area (self):
        return self.length*self.width

# 2/ Create a Vehicle class with max_speed and mileage instance attributes
class Vehicule:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed 
        self.mileage = mileage
    def add(self):
        return 1+1

# 3/ Create a Vehicle class without any variables and methods.
class Vehicule1:
    pass

# 4/ Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class ChildBus (Vehicule):
    def __init__(self,max_speed,mileage):
        super().__init__(max_speed,mileage)
    
    
    












