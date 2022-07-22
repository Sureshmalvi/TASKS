import random
n=random.randint(1,1000)
x=int(input("enter the number"))
print(n)
if x==n:
    print("computer number","your number")
    print("number tie")
elif x>n:
    print("computer number","your number")
    print("you win")
elif x<n:
    print("computer number","your number")
    print("comp win")
else:
    print("game complete")

