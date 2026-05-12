# Data Structure in python is a way of organizing and storing data in a way that allows for efficient access and modification. Python has several built-in data structures, including lists, tuples, sets, and dictionaries.

# list is a collection which is ordered and changeable. It allows duplicate members.
fruits = ["apple", "mango", "banana"]
# Indexing
print(fruits[0])     # apple
print(fruits[-1])    # banana (last item)
# Slicing
print(fruits[0:2])   # ['apple', 'mango']
# Add karna
fruits.append("grape")      # end mein add
fruits.insert(1, "orange")  # specific index pe add
# Remove karna
fruits.remove("mango")   # value se remove
fruits.pop()             # last item remove
# Length
print(len(fruits))
# Loop
for fruit in fruits:
    print(fruit)

# Tuple is a collection which is ordered and unchangeable. It allows duplicate members
coordinates = (10, 20, 30)
print(coordinates[0])    # 10
print(len(coordinates))  # 3
# Ye kaam nahi karega:
coordinates[0] = 99    # Error! Tuple immutable hai


# Set is a collection which is unordered and unindexed. It does not allow duplicate members.
numbers = {1, 2, 3, 3, 4, 4, 5}
print(numbers)    # {1, 2, 3, 4, 5} ← duplicates hat gaye!
# Add/Remove
numbers.add(6)
numbers.remove(1)
# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)    # {3, 4}       ← common values
print(a | b)    # {1,2,3,4,5,6} ← sab values
print(a - b)    # {1, 2}       ← a mein hain, b mein nahi


# Dictionary is a collection which is unordered, changeable and indexed. It does not allow duplicate members.
student = {
    "name": "Farhan",
    "age": 21,
    "city": "Okara"
}
# Access karna
print(student["name"])        # Farhan
print(student.get("age"))     # 21
# Add/Update
student["gpa"] = 3.8
student["age"] = 22
# Remove
del student["city"]
# Loop
for key, value in student.items():
    print(f"{key}: {value}")