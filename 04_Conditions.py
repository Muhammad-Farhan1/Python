# Conditions in Python allow you to execute different blocks of code based on certain conditions. Typeically, you use if, elif, and else statements to create these conditions.

# Example of if statement
age = 20
if age >= 18:
    print("You are an adult.")

# Example of if-else statement
age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Example of if-elif-else statement
age = 25
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Ternary operator (also known as conditional expression) is a concise way to write an if-else statement in a single line. The syntax is: `value_if_true if condition else value_if_false`.
age = 10
message = "Young" if age < 18 else "Younger"
print(message)

height = 5.7
message = "Good height" if height > 6.0 else "Average height"
print(message)

# Switch-case statements are not natively supported in Python, but you can achieve similar functionality using dictionaries or if-elif-else statements. Here's an example using a dictionary to mimic a switch-case statement:
day = input("Enter a day of the week: ").capitalize()
def is_weekend(day):
    match day :
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Invalid day"
print(is_weekend(day))