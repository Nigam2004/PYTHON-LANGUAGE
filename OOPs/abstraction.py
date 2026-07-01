from abc import ABC, abstractmethod

# 1. Define the Abstract Base Class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        """Abstract method; no implementation details provided here."""
        pass

    @abstractmethod
    def fuel_type(self):
        pass

# 2. Implement a Concrete Subclass
class Car(Vehicle):   #Inherited from vehicle class
    
    def start_engine(self):
        # Specific implementation details are hidden inside this subclass
        return "Car engine started: Vroom!"
        
    def fuel_type(self):
        return "Petrol"
    

# my_vehicle=Vehicle()
# print(my_vehicle.fuel_type())
#TypeError: Can't instantiate abstract class Vehicle without an implementation for abstract methods 'fuel_type', 'start_engine'
My_car=Car()
print(My_car.start_engine())
#O/P-> Car engine started: Vroom!