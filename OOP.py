class Car:
    def __init__(self, name, year, color, for_sale):
        self.name = name
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You are able to drive the {self.name}")

    def stop(self):
        print(f"You are not able to drive the {self.name} {self.color}")

    def describe(self):
        print(f"Your car name is {self.name}. The model of the car is {self.year}. It's Color is {self.color} and is it for sale ? :{self.for_sale}")
car1 = Car("Bugatti", 2023, "Yellow", False)
car2 = Car("Mustang", 2025, "Red", True)
#print(car2.name , car2.year , car2.color , car2.for_sale)
#car1.stop()
#car1.drive()
#car2.describe()




