







if __name__ == '__main__':


    print("Unit Converter")


    input("Please choose the unit you wish to convert: 1) Temperature 2) Speed: ").strip()

    unit_selector = input("Please choose the unit you wish to convert: 1) Temperature 2) Speed: ").strip()

  
    if unit_selector == "1":
        val = float(input("Enter the temperature "))
        unit = input("Celcius or Farenheit")
        print("la tuya por ahora")
    elif unit_selector == "2":
        val = float(input("Enter the speed"))
        unit = input("KMH or MPH")
        print("Vamo a ve klk")
    else:
        print("Abstengase de poner mierda")
