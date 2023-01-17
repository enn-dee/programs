unit = input("Is the temp in Celsuis or Fahrenheit (C/F): ")
temp = float(input("Enter the temp: "))
if unit == 'C' or unit == 'c':
    temp = round((9*temp)/5+32, 1)
    print(f"The temp in Fahrenheit is {temp}°F")

elif unit == "F" or unit == 'f':
    temp = round((temp-32)*5/9, 1)
    print(f"The temp in Celsuis is {temp}°C")
else:
    print(f"{unit} is invalid unit of measurement")
