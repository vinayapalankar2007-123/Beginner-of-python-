unit = input("convert to celcius or faranheit? (C/F) : ")
temp = float(input("enter the temperature : "))

if unit =="c":
    temp=round((9*temp)/5+32,1)
    print(f"temperature in faranheit is : {temp} °F")
    
elif unit=="f":
        temp = round((temp-32)*5/9,1)
        print(f"temperature in celcius is : {temp} °C ")
        
else:
           print("invalid measurment")
         