balance = 10000
while True:
        print("1.withdraw")
        print("2.balance")
        print("3.deposite")
        print("4.exit")
        ch=input("enter your choice:  ")
        if ch=="1":
            withdraw = int(input("enter an ammount to withdraw:  "))
            if withdraw>balance:
                print("insufficient balance!!")
            else:
                    balance-=withdraw
                    
                    print("withdrawan succesfully!!")
                    
        if ch=="2":
                        print(f"your balance is ₹{balance}")
                        
        if ch=="3":
            deposite=int(input("enter deposite ammount :  "))
            balance+=deposite
            print(f"your balance is ₹{balance}")
            
            
        if ch=="4":
            break