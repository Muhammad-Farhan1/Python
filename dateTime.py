import datetime

#date = datetime.date(2025,3,4)
#date = datetime.date.today()
#time = datetime.time(12,30,44)
#time = datetime.time.now()


now = datetime.datetime.now()
formatted = now.strftime("%H:%M:%S %d-%m-%Y")
print(now)