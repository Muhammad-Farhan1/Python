
age = int(input("Enter you age :"))

while age < 0 :
    print("YOu entered wrong age ")
    age = int(input("Enter you age :"))
    
print(f"you are {age} years old")   


#2nd example
name = input("Enter your name:")

while len(name) >= 12 :
    print("You entered wrong name")
    name = input("Enter your name again:")
print("You entered right name")