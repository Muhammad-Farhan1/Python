'''
def decorator(func):
    def wrapper():
        print("Transaction Started:")
        func()
        print("Transaction Terminated.")
    return wrapper  

@decorator
def hello():
    print("Steps of transaction are performing here.")
hello()'''

#Ice cream Example:

def get_ice_cream(func):
    def wrapper(flavour):
        print("You add sprinklers")
        func(flavour)   
        print("now you can eat it.")    
    return wrapper    

@get_ice_cream
def eat_ice_cream(flavour):
    print(f"Take your {flavour} ice-cream ")
eat_ice_cream("vanilla")    
