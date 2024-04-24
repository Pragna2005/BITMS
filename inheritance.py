class Animal:
    def __init__(self,name,height):
        self.name=name
        self.height=height
class Dog(Animal):
    def isDog(self):
        print(f"{self.name} is Animal")

a=Dog("lucky",5)
print(a.isDog())

'''class Dog:
    num1=3
    def home(self,a,b)
    self.a=a
    '''