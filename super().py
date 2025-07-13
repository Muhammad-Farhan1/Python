class Shape:
    def __init__(self, color , is_filled ):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"The color is {self.color} and it is  {'Filled' if self.is_filled == True else 'Not Filled'}")

class Circle(Shape):
    def __init__(self,color , is_filled, radius):
        super().__init__(color , is_filled)    
        self.radius = radius

    def describe(self):
        print(f"The area of circle is {3.14 * self.radius ** 2}")
        super().describe()

class Square(Shape):
    def __init__(self,color , is_filled, width):
       super().__init__(color , is_filled) 
       self.width = width

    def describe(self):
       print(f"The area of square is { self.width ** 2}")
       super().describe()

class Triangle(Shape):
    def __init__(self,color , is_filled, width , height):
       super().__init__(color , is_filled) 
       self.width = width
       self.height = height

    def describe(self):
       print(f"The area of triangle is {1/2 * self.width * self.height}")
       super().describe()

circle = Circle("Red",True,5)
square = Square( "Green" , False ,  6)
triangle = Triangle("Blue", True , 3 , 9)

circle.describe()
square.describe()
triangle.describe()