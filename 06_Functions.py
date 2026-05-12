# Functions are reusable blocks of code that perform a specific task. They allow us to break down our code into smaller, more manageable pieces, and they can be called multiple times throughout our program. In Python, we define a function using the def keyword, followed by the function name and parentheses. The code block within the function is indented.  

def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

# Functions with Parameters:
def self(first , last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = self("John" ,"Vicky")
print(full_name)


#Functions with default arguments:
def ingredients(item_name, price=4500, tax=0.1):
    result = price / tax
    return float(f"{result:.2f}")
print(ingredients("Mobile", 4500, 0.01))


#Example of default args:
from doctest import Example
import time 
def timer(end, start=11):
    for x in range(start , end+1):
        print(x)
        time.sleep(1)
timer(0,10)  
timer(15)
print("Done!")  

# arbitary arguments (*args and **kwargs):
# *args allows you to pass a variable number of non-keyword arguments to a function.
# Example of arbitrary arguments (*args):
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total 
print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15

# **kwargs allows you to pass a variable number of keyword arguments to a function.
# Example of arbitrary keyword arguments (**kwargs):
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")


# lambda functions: Lambda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not reused elsewhere in the code. The syntax for a lambda function is: `lambda arguments: expression`.
# Example of a lambda function:
square = lambda x: x ** 2
print(square(5))  # Output: 25


def bigger(a, b):
    return a if a > b else b
