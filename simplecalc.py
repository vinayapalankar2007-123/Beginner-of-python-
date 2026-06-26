operator = input("enter an operator to do calculation : ")
num1= float(input("enter first number : "))
num2= float(input("enter second number : "))

if operator== "+":
    result=num1+num2
    print(result)
    
elif operator==  "-":
     result=num1-num2
     print(result)
    
elif operator==  "*":
    result= num1*num2
    print(result)
    
elif operator=="/":
        result =num1/num2
        print(result)
        
else:
      print(f"{operator} is invalid")