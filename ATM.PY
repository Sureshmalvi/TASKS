print("Hello Welcome\nPlease Enter Your Account Detail to Continue With Your Account")
a="suresh"
b=4321
ac_bal=0
c=input("Enter Your Name:").lower()
d=int(input("Enter Your Pin:"))
if c==a and d==b:
        print("validation succesfull")
        while True:
                print("                    ")
                if d==b:
                    print("What Do You Want:-")
                    print("1.View Account Balance\n2.Withdraw Money\n3.Deposit Money")
                    choice=int(input("Enter Your Choice:"))
                    if choice==1:
                        print("      ")
                        print("Available Balance is:",ac_bal,"/-")
                    elif choice==2:
                        print("       ")
                        withdraw=int(input("Enter Amount:"))
                        if(withdraw>ac_bal):
                            print("Insufficent Balance")
                            print("Deposit Some Money")
                        else:
                            print("     ")
                            ac_bal=ac_bal-withdraw
                            print("Collect Money:",withdraw,"/-")
                            print("Available Balance is:",ac_bal,"/-")
                    elif choice==3:
                        print("        ")
                        dep=int(input("Enter Amount You Want To Deposit:"))
                        ac_bal=ac_bal+dep
                        print("Amount Added Successfull:",ac_bal,"/-")
                    else:
                        break
else:
    print("Invalid Input")

