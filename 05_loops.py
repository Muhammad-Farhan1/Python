# Loop is a programming structure that allows us to repeat a block of code multiple times. In Python, we have two main types of loops: for loops and while loops.

# for loops are used to iterate over a sequence (like a list, tuple, or string) or a range of numbers.

# for loop example
count = 0
for numbers in range(1,10):
    if numbers % 2 ==0 :
        count += 1
        print(numbers)
print(f"We have {count} numbers")

# while loops are used to repeat a block of code as long as a certain condition is true.

count = 0
number = 1
while number < 10:
    if number % 2 == 0:
        count += 1
        print(number)
    number += 1
print(f"We have {count} numbers")

# Loop Control Statements:
# break: This statement is used to exit the loop prematurely when a certain condition is met.
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue: This statement is used to skip the current iteration of the loop and move to the next iteration.
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

# pass: This statement is a placeholder that does nothing. It is used when a statement is required syntactically but you don't want to execute any code.
for i in range(1, 10):
    if i % 2 == 0:
        pass  # This will do nothing for even numbers
    else:
        print(i)  # This will print odd numbers    

# Nested Loops: You can also have loops inside loops, which are called nested loops. The inner loop will be executed for each iteration of the outer loop.
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}") 