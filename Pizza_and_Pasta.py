
import math
class food:
    def pizeria(self):
        print("----------Welcome To Amazing Pizza and Pasta Pizeria----------")
        data="""
        press 1 for Menu 
        press 2 for Exit
        """
        print(data)
        c=int(input("Enter Your Choice"))
        if c==1:
            print("""

            1) Large Pizza = 600/-
            2) Large Pizza = 1100/-
            3) Large Pizza = 1600/-
            For more then 4 or 4 per pizza price is 400

            Offer: if Buy 4 Or More Pizza You get 1.5L Soft Drink 

            1) Large Pasta = 800/-
            2) Large Pasta = 1500/-
            3) Large Pasta = 2100/-
            For more then 4 or 4 per pasta  price is 600

            Offer: if Buy 4 Or More Pasta You get 2 bruschetta free

            Extended Offer: Buy 4 Or More Pizza And Pastas And Get 2 Chocco Brownies Ice Cream Free.

            """)
            sum=0
            sum1=0
            bill=0
            bill1=0
            while True:
                N=input("Enter Your Name:")
                print("welcome",N)
                pi=int(input("Enter Number Of Pizza You Want"))
                if pi==1:
                    sum=sum+pi
                    bill+=600
                    print("Your PIzza Amount Is:",600,"/-")
                elif pi==2:
                    sum=sum+pi
                    bill+=1100
                    print("Your PIzza Amount Is:",1100,"/-")
                elif pi==3:
                    sum=sum+pi
                    bill+=1700
                    print("Your PIzza Amount Is:",1600,"/-")
                else:
                    sum=sum+pi
                    bill+=(pi*400)
                    print("Your PIzza Amount Is:",(pi*400),"/-")
                    print("Congratulation!! You Get 1.5L Soft Drink Free On This Order")
                A=input("Do you want to order pasta(y/n)= ")
                if A=="y":
                    pas=int(input("Enter Number Of Pasta You Want:"))
                    if pas==1:
                        sum1=sum1+pas
                        bill1+=800
                        print("Your pasta amount is= ",800,"/-")
                    elif pas==2:
                        sum1=sum1+pas
                        bill1+=1500
                        print("Your pasta amount is= ",1500,"/-")
                    elif pas==3:
                        sum1=sum1+pas
                        bill1+=2100
                        print("Your pasta amount is= ",2100,"/-")
                    else:
                        sum1=sum1+pas
                        bill1+=(pas*600)
                        print("       ")
                        print('-------------------------------------------------------------')
                        print("***Congratutions !! get 1 bruschetta free***")
                        # print("***Congratutions !! get 1 choco brownies ice cream free***")
                        print("       ")
                        print('-------------------------------------------------------------')
                        print("Your pasta amount is= ",(pas*600),"/-")
                total=bill+bill1
                print(f"Your Total Amount is:{total}")
                x=input("Want To Order For Another Customer press y for yes press N for no:")
                if x!="y":
                    print("             ") 
                    print("-------------Pizza and Pasta Bill-----------------")
                    print("             ") 
                    print("Payment received from pizza= ",round(bill),"/-")
                    print("Payment received from pasta= ",round(bill1),"/-")
                    print("             ") 
                    print(f"Your net order amount of the day is= {total}","/-")
                    print("             ") 
                    print("Number of pizza and pasta sold in one sift= ", round(sum+sum1),"/-")
                    print("             ") 
                    if sum>=4:
                        print("            ")
                        print("Number of soft drink bottle given= ",round(math.floor(sum/4)))
                    else:
                        print("        ")
                        print("Number of soft drink bottle given= ",0) 
                    if sum1>=4:   
                        print("         ") 
                        print("Number of bruschetta given to customer= ",round(math.floor(sum1/4)))
                    else:
                        print("               ")
                        print("Number of bruschetta given to customer= ",0)
                    print("             ") 
                    if (sum>=4 and sum1>=4):  
                        print("Number of choco brownies ice cream given to customer= ",(math.floor((sum)/4)+math.floor(sum1)/4))
                    else:
                        print("Number of choco brownies ice cream given to customer= ",0)    
                    print("             ") 
                    print("---------------Have a nice day !!!-----------------") 
                    print("             ")   
                    break
obj=food()
obj.pizeria()



                
