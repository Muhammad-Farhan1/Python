temperature = int(input("Enter the temperature: "))

if temperature <= 12:
    print("It is good")
elif 12 < temperature <= 20:
    print("Average temperature")
else:
    print("It is not good")

print("Done")