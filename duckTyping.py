#Duck typing : If it looks like a duck or quack like a duck, then its a duck 

class Animal():
    isLive = True

class Cat(Animal):
    def speak(self):
     print("Woof!")   

class Dog(Animal):
     def speak(self):
      print("Woof!")

class Car(Animal):
    isLive = False  
    def speak(self):
        print("Peep")
animals = [Cat() , Dog() , Car() ]
for animal in animals :
    print(animal.speak())
    print(f"is aLive? {animal.isLive}")