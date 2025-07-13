#Class variable in OOP python:

class Student :
    batch = 2026
    num_students = 0
    age_std = 18
    def __init__(self, name, f_name , Code , grades):
        self.name = name
        self.f_name = f_name
        self.Code = Code
        self.grades = grades
        Student.num_students += 1

std1 = Student( "John" , "Wick" ,432 , "A+")  
std2 = Student( "Lee" , "Laa" , 532 , "A")  
std3 = Student( "Bobby" , "Les" , 112 , "D")  

print(std1.name , std1.f_name , std1.Code , std1.grades ,Student.num_students )      
print(f"The name of student is {std2.name} and his father name is {std2.f_name} and roll number is {std2.Code} and now the total number of students is {Student.num_students} of the batch {Student.batch}")         
     