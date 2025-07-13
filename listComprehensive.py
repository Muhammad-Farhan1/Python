#List comprehension :
# Old method:
doubles = []
for x in range(1,10):
    doubles.append(x * 2)

#print(doubles)

#New Method -> [expression for value in iterables if condition(Optional)]
doubles = [x * 2 for x in range(1,11)]
triples = [x * 3 for x in range(1,11)]
squares = [x * x for x in range(1,11) ]
#print(squares)

#List comprehensive with if condition :

grades = [33 , 80, 59, 99, 54]
check_results = [grade for grade in grades if grade > 33]
#print(check_results)

number = [1, -2 , 4 , -3, 6 , -5 , 0 , 0 , 0 , 0]
positive_nums = [num for num in number if num > 0]
negative_nums = [num for num in number if num < 0]
zero_nums = [num for num in number if num == 0]
print(positive_nums)
print(negative_nums)
print(zero_nums)