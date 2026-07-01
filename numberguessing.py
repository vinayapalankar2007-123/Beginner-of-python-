a = 7
attempts =0

while True:
    guess =int(input("guess a number 1-9:  "))
    attempts+=1
    if guess ==a:
        print("you wonl!!")
        break
       
    elif guess>=a:
        print("high!!!")    
    elif guess<=a:
         print("low!")   
         
else:
         print("try again!!!!!")
 
 
print(f"no of attemts number is  {attempts}")