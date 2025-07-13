#An object/collection that can returned its element one at a time, allowing  it to be iterated over in a for loop.

#Iterables with lists :

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in reversed(number):
   # print(num , end=" ")


#Iterables with tuples:

 number_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for num in number_tuple:
    #  print(num, end=" ") 

#Iterables with sets: (it cannot be reversible)

 number_set = {"Apple" , "Banana", "Cherry", "Date", "Elderberry"}
for num in number_set:
    print(num)

#Iterables with dictionaries:
number_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for key, value in reversed(number_dict.items()):
    print(f"{key}: {value}")    
