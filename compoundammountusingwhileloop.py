#compound intrest calculater
#a=p*pow(1+r/n),t)
principle=0
rate=0
time=0

while principle <=0:
    principle= float(input("enter principle ammount :  "))
    if principle <=0:
        print("cant be negaative or zero")

while rate <=0:
    rate = int(input("enter rate ammount :  "))
    if rate <=0:
        print("cant be negaative or zero")

while time <=0:
    time = int(input("enter time in years  :  "))
    if time <=0:
        print("cant be negaative or zero")


print(principle)
print(rate)
print(time)

total = principle *pow((1+rate/100),time)
print(total)