# Type Casting - Type casting is the process of converting a value from one data type to another. In Python, you can use built-in functions to perform type casting. Here are some common type casting functions:
# - int() - Converts a value to an integer
# - float() - Converts a value to a floating-point number
# - str() - Converts a value to a string
# - bool() - Converts a value to a boolean

# Example of type casting
x = 5
y = "10"
# Convert y from string to integer and add it to x
result = x + int(y)
print(result)  # Output: 15
print("*"*50)

# Boolean Casting - In Python, the following values are considered false when converted to a boolean:
# - None
# - False
# - 0 (zero of any numeric type)
# - 0.0 (zero float)
# - 0j (zero complex)
# - Empty sequences and collections (e.g., '', [], (), {})
# All other values are considered true when converted to a boolean.

print(bool(0))      # False  ← zero hamesha False
print(bool(1))      # True   ← koi bhi number besides 0 = True
print(bool(""))     # False  ← khali string = False
print(bool("hi"))   # True   ← koi bhi text = True
print(bool(None))   # False  ← None hamesha False