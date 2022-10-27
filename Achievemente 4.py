####
###
###
###
###

print("Unit converter")


def temp_convert(val, unit):
    cel_to_fah = (val * 1.8) + 32
    fah_to_cel = (val - 32)/1.8
    if unit.upper() =="F":
        print(cel_to_fah, "Fahrenheit")
    if unit.upper() =="C":
        print(fah_to_cel, "Celsius")
    
def speed_convert(val, unit):
    kmh_to_mph = (val *  0.6213711922)
    mph_to_kmh = (val/1.609344 )
    if unit.upper() == "KMH":
        print(kmh_to_mph)
    if unit.upper() == "MPH":
        print(mph_to_kmh)
    







    






