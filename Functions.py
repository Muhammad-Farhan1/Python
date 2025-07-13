
'''def say_hello(name , age):
    print(f"Hello, {name}!")
    print("Happy birthday to you! ")
    print(f"You are {age} years old")
say_hello("John" , 24)    
say_hello("Vicky" , 33)  '''  

#function with return statement:

def self(first , last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = self("John" ,"Vicky")
#print(full_name)


#Functions with default arguments:

def ingredients(item_name, price=4500, tax=0.1):
    result = price / tax
    return float(f"{result:.2f}")

#print(ingredients("Mobile", 4500, 0.01))


#Example of default args:
import time 
def timer(end, start=11):
    for x in range(start , end+1):
        print(x)
        time.sleep(1)
#timer(0,10)  
#timer(15)
#print("Done!")  


#keyword arguments :

'''def greetings(greet , title , f_name , l_name):
    print(f"{greet} {title}. {f_name} {l_name}")
greetings("Hello", "Mr", "John" ,"Vicky")
greetings("Hi" , l_name="Joseph" , title="Mister" ,f_name="Lister")'''


#Arbitrary arguments (known as *args):

'''def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum(4,5,7,6,76,644,333,55,2))'''


#Keyword args (known as **kwargs):
def address(**kwargs):
 '''     for key,value in kwargs.items():
        print(f"{key}:{value}")
address(street="123 Main St",
        city="Springfield",
        state="IL",
        zip_code="62704") ''' 

