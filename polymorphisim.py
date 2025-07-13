from abc import ABC,abstractmethod

class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):
   def __init__(self , radius) :
       self.radius = radius

   def area(self):  
       return 3.14 * self.radius ** 2 

class Square(Shapes):
    def __init__(self , side) :
       self.side = side

    def area(self):  
       return self.side ** 2

class Triangle(Shapes):
    def __init__(self , height , width) :
       self.height = height
       self.width = width

    def area(self):  
       return self.height * self.width * 0.5

class Mobile(Square):
    def __init__(self, side):
        super().__init__(side)


shapes = [Circle(4) , Square(7) , Triangle(2,4) , Mobile(4)]

for shape in shapes:
    print(f"{shape.area()}cm")

#Example number 2:

class Animal:
    def speak(self):
        pass  # This will be overridden

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    def speak(self):
        return "Moo"

animals = [Dog(), Cat(), Cow()]

#for animal in animals:
#    print(animal.speak())
