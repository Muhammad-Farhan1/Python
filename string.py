#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello".

print("Hello" , 'World!')

a="Python is Fun"
print(a)

#Strings are Arrays
print(a[0]) 

#String Length
print(len(a))

#Loop through string:
for x in "Apple":
    print(x ,end="" )
print()

#Check String (in or not in keyword:)
statement = "Cold winds are blowing and weather is soo cool"
print("are" in statement)
print("Cold" not in statement)

#Slicing String
#You can return a range of characters by using the slice syntax.
abc = "Slice method of string in python"
print(abc[4:11])  #Note: It include spaces also
print(abc[:16]) #By leaving start index,the range will start from first character.
#Similarly ,By leaving out the end index the range will go to the end.

#Negative indexing:
print(abc[-1])

#String Methods:
txt = " bobby Is kiNg "
print(txt.upper()) #It makes all character in Upper Case
print(txt.capitalize()) #It makes all letters first alphabet capital
print(txt.lower()) #It makes all character in lower Case
print(txt.strip()) #It Remove Whitespace
print(txt.replace("bobby" , "Bob"))
print(txt.split(" "))#splits the string into substrings if it finds(symbols#,.)
print(txt.count("b")) #Returns the number of times a specified value occurs
print(txt.find("i"))#Searches the string for a specified value and returns the position of where it was found
print(txt.isalnum()) #Returns True if all characters in the string are alphanumeric
print(txt.isalpha())#Returns True if all characters in the string are alphabet
print(txt.isascii())#Returns True if all characters in the string are Characters
print(txt.isdigit())#Returns True if all characters in the string are alphanumeric


#String Concatenation
y = "Hello"
z = "World"
u = y + " " + z
print(u)

#F-Strings -> Formatted String
name = "Maxwell"
age = 40
print(f"My name is {name} and age is {age}")


'''
Method --->	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''