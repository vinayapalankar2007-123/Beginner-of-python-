unit = input("kilograms or grams? (K    or  G;  ")
weight = float(input("enter your weight :  "))

if unit=="k":
    weight=weight*1000
    print(f"weight in grams is:  {weight} gms")
elif unit=="g":
    weight=weight /1000
    print(f"wight in kgs is:  {weight}kgs")
else:
        print("invalid measurment")