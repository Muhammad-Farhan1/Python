'''word = "Apple" 

letter = input("Guess a letter: ").upper()
if letter in word.upper():
    print(f"{letter} is Found!")
else:
    print(f"{letter} is not Found!")    
'''

    #Membership operators in sets :
'''
colors = {"black" , "orange" , "blue" , "gray"}    

color = input("Guess the color:")

if color in colors:
    print(f"{color} is found")
else:
    print(f"{color} is not found")    '''


#Membership operators in dictionaries:

grade= {"Moh" : "A" ,
        "Havel" : "B",
        "Ali" : "C"}

student = input("Enter something about student: ").capitalize()

if student in grade:
    print(f"{student}'s grade is : {grade[student]}")
else:
    print(f"{student} incorrect!")    