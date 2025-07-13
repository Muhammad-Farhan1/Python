#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random
low = 1
high = 100
option = ("Rock" , "Paper" , "Scissors")
list = ["0" , "2" , "3" ,"4" , "A" , "G" , "H"]
#number = random.randint(low , high)
#number = random.random()
#number = random.choice(option)

#random.shuffle(list)
#print(list)

print(random.randint(1,10))

'''
randrange() -> Returns a random number between the given range
randint() ->	Returns a random number between the given range
shuffle() ->	Takes a sequence and returns the sequence in a random order
'''