import random
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '?']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Names=int(input("Enter how many letters:"))
Symbols=int(input("Enter how many symbols:"))
Numbers=int(input("Enter how many numbers:"))
password=""
print("Welcome to password Generator!")
for i in range(Names):
    password=password + random.choice(characters)
for symbol in range(Symbols):
    password=password+random.choice(symbols)
for number in range(Numbers):
    password=password + random.choice(numbers)
password_list=""
password_list=list(password)
random.shuffle(password_list)
password=''.join(password_list)
print(f"The Generated password is {password}")
