from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        pass
    def mileage1(self):
        print("non abstract")
        
class Tesla(Car):
    def mileage(self):
        print("abs method defined in tesla class-mileage->30kmph")
        
class Benz(Car):
    def mileage(self):
        print("abs method defined in benz class-mileage->40kmph")
        
t=Tesla()
t.mileage()

b=Benz()
b.mileage()