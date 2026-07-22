height = int(input("Enter the height: "))
bill= 0
if height >=3:
    print("you can ride")
    age = int(input("enter the age: "))
    if age <12:
        bill = 150
        print("pay 150 rupees")
    elif age <=18:
        bill = 250
        print("pay 250 rupees")
    else:
        bill = 500
        print("pay 500 rupees")
    
    answer=input("do you want a picture? (yes/no)")
    if answer=="yes" or answer=="YES":
        Bill=bill + 50
        print(f"Your total bill is {Bill}")
    if answer=="no" or answer=="NO":
        print(bill)
else:
    print("cant ride")
    print("Bye")
