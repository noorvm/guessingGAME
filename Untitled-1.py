import random

x=random.randrange(0,20)
win="loose 😥😪"
for j in range (0,5):
    if(j!=5):
        i=int (input("entre number \t"))
        print(f"u have {4-j} chance left")
        if(i>x):
            print("number is to big")
        elif(i<x):
            print("number is small") 
        else:
            win="won🥇🥳🥳 "
            break     
print(win)
print(f"value is {x}")       