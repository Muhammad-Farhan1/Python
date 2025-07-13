'''
import os
file_path = "C:\\Users\\Ali Baba\\Desktop\\test1.txt" #It's temporary

if os.path.exists(file_path):
  print("The Location exists")
  if os.path.isfile(file_path):
    print("File")
  elif os.path.isdir(file_path):
    print("Directory") 
else:
  print("The Location exists")'''

#Writing files (txt):
employees = ["John" , "Mickey" , "Shaper" , "Pat"]
file_path = "C:\\Users\\Ali Baba\\Desktop\\test1.txt"
try:
    with open(file=file_path , mode="w") as file:
        for employee in employees:
            file.write(employee + " ")
        print("File has been created")   
except FileExistsError:
    print("It is also exists!")       


#Writing files (json): 
import json   
employees = {
    "Name" : "John",
    "Age" : 32,
    "Job" : "Chef",
    "Residence" : "Paris"
}
file_path = "C:\\Users\\Ali Baba\\Desktop\\test.json"
try:
    with open(file_path , "w") as file:  
        json.dump(employees , file , indent=5)
        print("File has been created")   
except FileExistsError:
    print("It is also exists!")    


    #Reading Files is exactly same with a difference of one line just <3