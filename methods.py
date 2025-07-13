#Static method:
class Employee:
    def __init__(self , name , position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager" , "Cashier" , "Chef" , "Coder"]
        return position in valid_position
    

employee1 = Employee("John" , "Cashier")   
#print(Employee.is_valid_position("Chef")) 
#print(employee1.get_info())

#Example #2
class UnitConverter:
    @staticmethod
    def km_to_miles(km):
        return km * 0.621371
    
    @staticmethod
    def cel_to_fah(cel):
        return (cel * 9/5) + 32
    
    @staticmethod
    def kg_to_pounds(kg):
        return kg * 2.20462
    
#print(f"{UnitConverter.km_to_miles(3):.2f}")    
#print(UnitConverter.cel_to_fah(32))
#print(UnitConverter.kg_to_pounds(2))

#Class Methods:

class Student:
    count = 0 

    def __init__(self , name , gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    #instance method:
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return cls.count

std1 = Student("John" , 4.0)    
std2 = Student("Mickey" , 2.4) 
std3 = Student("Michael" , 3.3)
print(Student.get_count())



#Magic methods

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title} with {self.pages} pages"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages


book1 = Book("Python Basics", 300)
book2 = Book("Advanced Python", 450)

print(book1)                #  __str__
# print(len(book1))            __len__
 # print(book1 + book2)        __add__
