a = int(input("enter a number:  "))
b = int(input("enter second number: "))
ch = input("enter an operator (+,-,*,/)")

if ch=="+":
    print("addition is: " ,a+b)
elif ch=="-":
    print("addition is: ",a-b)
elif ch=="*":
    print("multiplication is: ",a*b)     
elif ch== "/":
    print("division is: ",a/b)   
else:
    print("invalid operator!!!")    