try:
    number = int(input("Enter a number:"))
    print(1 / number)
except ZeroDivisionError:
    print("Number can't be divided by zero!")    
except ValueError:
    print("Only integer numbers are allowed!")     
except Exception:
    print("Something went Wrong! you must check it carefully 📄")  
finally:
    print("It will be run no matter!")      
