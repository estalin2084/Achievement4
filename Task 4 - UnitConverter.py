#Name: Unit Converter.py
# Author: Estalin Peña
# Date Created: october 24, 2022
# Date Last Modified: october 24, 2022
# Purpose: Convert Temperature (Celsius and Fahrenheit) and speed (KMH/MPH)

#Fuction name: temp_convert
#Description: Will Output the conversion of the temperature selected by the user
#Parameters: 
#            Val: Numeric value of the temperature
#            Unit: The kind of temperature the user wants to convert
#Return value:The conversion of the temperature selected by the user


def temp_convert(val, unit):
    cel_to_fah = (val * 1.8) + 32
    fah_to_cel = (val - 32)/1.8
    if unit.upper() =="C":
        print('{:.2f} {}'.format(cel_to_fah, "Fahrenheit".strip()))
    if unit.upper() =="F":
        print('{:.2f} {}'.format(fah_to_cel, "Celsius".strip()))

#Fuction name: speed_convert
#Description: Will Output the conversion of the speed selected by the user
#Parameters: 
#            Val: Numeric value of the speed
#            Unit: The kind of speed the user wants to convert
#Return value:The conversion of the speed selected by the user
def speed_convert(val, unit):
    kmh_to_mph = (val *  0.6214)
    mph_to_kmh = (val * 1.609344 )
    if unit.upper() == "KMH":
        print('{:.2f} {}'.format(kmh_to_mph, "Miles per hour".strip()))
    if unit.upper() == "MPH":
        print('{:.2f} {}'.format(mph_to_kmh, "Kilometers per hour".strip()))



print(" ")#spaces between the information
print("\t","\t", "\t",  "Welcome to the Unit Converter")#Displays the welcome message
print(" ")#spaces between the information

unit_selector = input("Please select the unit you wish to convert: 1) Temperature 2) Speed: ").strip()#Takes the type of unit the user wishes to convert
print(" - " *40)#separates the data printed with dashes

 
if unit_selector == "1": #This evaluates the user selection  for Temperature
    val = float(input("Please enter the temperature: "))#This takes the numeric value of the temperature
    unit = input("'C' Celcius or 'F' Farenheit: ")#The user selects Celsius of Fahrenheit
    temp_convert(val, unit)#This returns the values from the fuction tempt converter and  applies the formula
elif unit_selector == "2": #This evaluates the user selection for speed.
    val = float(input("Please enter the speed: ")) #This input takes the numeric value of the speed
    unit = input("KMH or MPH: ") #this takes the kind of distance 
    speed_convert(val, unit)#This returns the values from the fuction speed converter and  applies the formula

goodBye = input("Do you wish to continue? [Yes/No]: ".strip())#This variable asks the user if wants to continue in the process 

while goodBye == True: #This while evaluates either if the user wants to continue or not converting speed or temperatures.
    if goodBye.upper() == "Yes" or goodBye.upper() == "Y":
        goodBye = True
    elif goodBye.upper() == "No" or goodBye.upper() == "N":
        goodBye == False
        break
else: #If no is selected then we wish the user a great day!
    print("Have a great day!".strip())