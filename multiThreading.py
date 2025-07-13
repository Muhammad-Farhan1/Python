import threading
import time


def home_work():
    time.sleep(3)
    print("When will you complete your home work?")

def take_rest():
    time.sleep(2)
    print("Now you should take some rest")

def go_to_school(first , last):
    time.sleep(4)
    print(f"You should go to school {first} {last}")

case1 = threading.Thread(target=home_work)
case2 = threading.Thread(target=take_rest)
case3 = threading.Thread(target=go_to_school , args=("john" , "wick"))

case1.start()
case2.start()
case3.start()

case1.join()
case2.join()
case3.join()

print("finished")