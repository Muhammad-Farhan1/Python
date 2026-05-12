# Output - The process of displaying information on the screen or other output devices. In Python, you can use the built-in print() function to output data to the console. The print() function can take multiple arguments and will convert them to strings before displaying them.
print("Hello, World!")
print("^"*50)

# sep — items ke beech separator (default space hai)
print("Farhan", "Okara", "Pakistan", sep=" | ")
print("*"*50)
# Output: Farhan | Okara | Pakistan

# end — line ke end pe kya aaye (default newline hai)
print("Hello", end=" ")
print("World")
print("*"*50)
# Output: Hello World

# Input - The process of receiving data from the user. In Python, you can use the built-in input() function to get input from the user. The input() function takes a prompt string as an argument and returns the user's input as a string.
name = input("Enter your name: ")
print(f"Hello, {name}!")
print("*"*50)

# Formatted string literals (f-strings) - F-strings are a way to format strings in Python. They allow you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and the resulting values are inserted into the string. F-strings are prefixed with the letter 'f' or 'F' before the opening quotation mark.
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
print("*"*50)
