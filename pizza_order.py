size= input("which size do you want? small/medium/large")
bill=0
if size=="small":
    bill+=100
    print("pay 100")
elif size=="medium":
    bill+=200
    print("pay 200")
else:
    bill+=300
    print("pay 300")

pepperoni=input("Do you want pepperoni: yes/no")
if pepperoni=="yes" or pepperoni=="YES":
    if size=="small":
       bill+=30
    else:
       bill+=50

extra_cheese=input("Do you want extra cheese?? yes?no")
if extra_cheese=="Yes" or extra_cheese=="YES":
    if size=="small":
       bill+=20

print(f"totall bill is {bill}")    
    
