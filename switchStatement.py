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

#Vowel Words:
char = input("Enter a character from vowel :")

def is_vowel(char):
    match char:
        case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
            return True    
        case _:
            return False    
        
print(is_vowel(char))