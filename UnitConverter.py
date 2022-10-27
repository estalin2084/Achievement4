#Name: Unit Converter.py
# Author: Estalin Peña
# Date Created: october 24, 2022
# Date Last Modified: october 24, 2022
# Purpose: Convert Temperature (Celsius and Fahrenheit) and speed (KMH/MPH)


def temp_convert(val, unit):
    cel_to_fah = (val * 1.8) + 32
    fah_to_cel = (val - 32)/1.8
    if unit.upper() =="C":
        print('{:.2f} {}'.format(cel_to_fah, "Fahrenheit".strip()))
    if unit.upper() =="F":
        print('{:.2f} {}'.format(fah_to_cel, "Celsius".strip()))

def speed_convert(val, unit):
    kmh_to_mph = (val *  0.6214)
    mph_to_kmh = (val * 1.609344 )
    if unit.upper() == "KMH":
        print('{:.2f} {}'.format(kmh_to_mph, "Miles per hour".strip()))
    if unit.upper() == "MPH":
        print('{:.2f} {}'.format(mph_to_kmh, "Kilometers per hour".strip()))



print(" ")
print("\t","\t", "\t",  "Welcome to the Unit Converter")
print(" ")

unit_selector = input("Please select the unit you wish to convert: 1) Temperature 2) Speed: ").strip()

 
if unit_selector == "1":
    val = float(input("Please enter the temperature: "))
    unit = input("'C' Celcius or 'F' Farenheit: ")
    temp_convert(val, unit)
elif unit_selector == "2":
    val = float(input("Please enter the speed: "))
    unit = input("KMH or MPH: ")
    speed_convert(val, unit)

goodBye = input("Do you wish to continue? [Yes/No]: ".strip())

while goodBye == True:
    if goodBye.upper() == "Yes" or goodBye.upper() == "Y":
        goodBye = True
    elif goodBye.upper() == "No" or goodBye.upper() == "N":
        goodBye == False
        break
else:
    print("Have a great day!".strip())