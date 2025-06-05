def celcius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celcius(f):
    return (f - 32) * 5 / 9

choice = int(input("Choose 1 or 2 respectively for Celcius or Fahrenheit input temperature : "))

if choice == 1:
    Celcius = int(input("Enter temperatur in Celcius: "))
    Fahrenheit = celcius_to_fahrenheit(Celcius)
    print(f"{Celcius}°C is equal to {Fahrenheit}°F")

elif choice == 2:
    Fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    Celcius = fahrenheit_to_celcius(Fahrenheit)
    print(f"{Fahrenheit}°F is equal to {Celcius}°C")

else:
    print("Choose either 1 or 2. Please!")