#Inheritance in OOP python :
#Example 1:

class Animal:
    def __init__(self , name):
        self.name = name
        self.is_alive = True

class Dog(Animal):
    def speak(self):
        print("Woh!")     

class Cat(Animal):
    def speak(self):
        print("Meow!")        

class Mouse(Animal):
    def speak(self):
        print("Squ!")        
dog = Dog("Tom" )
cat = Cat("Pika")
mouse = Mouse("Jerry")

#cat.speak()
#dog.speak()
#mouse.speak()


#Example 2:
class Father:
    def __init__(self , name , age):
        self.name = name
        self.age = age

class Son(Father):
    def occupation(self):
        print("Doctor")

class Daughter(Father):
     def occupation(self):
        print("Student")

son = Son("John" , 23)
daughter = Daughter("Elisa" , 18)
#print(daughter.name)
#print(son.name , son.age)
#son.occupation()
#daughter.occupation()



#Multiple inheritance:

class Prey:
    def flee(self):
        print("This animal can fly")

class Predator:
    def hunt(self):
        print("This animal can hunt")

class Fish(Prey , Predator):
    pass

class Lion(Predator):
    pass

class Butterfly(Prey):
    pass

fish = Fish()
lion = Lion()
butterfly = Butterfly()

#fish.hunt()
#lion.hunt()
#butterfly.flee()