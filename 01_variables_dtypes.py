#Variables - A variable is a named container that stores data in memory. When you create a variable, Python reserves a space in memory and gives it a name so you can access it later.
age = 10   
height = 5.7
name = "john"
f_name = "wick"
is_inter_done = True
intro = f"My name is {name} and my father name is {f_name} while my age is {age} and my height is {height} and my intermediate has been done {is_inter_done}"
print(intro) 
print('*'*50)


'''
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)
print('*'*50)
#Note : int and str can't be added 

# Data Types - In Python, there are several built-in data types that you can use to store different kinds of data. Some of the most common data types include:
# - int (integer)
# - float (floating-point number)
# - str (string)
# - bool (boolean)

print(type(age))  # Output: <class 'int'>
print(type(height))  # Output: <class 'float'>
print(type(name))  # Output: <class 'str'>
print(type(is_inter_done))  # Output: <class 'bool'>

print('*'*50)