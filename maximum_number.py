#maximum number finding using for loop
numbers = input("Enter the numbers: ")
# 345 263 372 675 854
number_list = numbers.split()
count=0
for number in number_list:
    count+= 1
for i in range(count):
    number_list[i]=int(number_list[i])
print(f"Entered number are {count}")    
maximum_number=number_list[0]
for number in number_list:
    if number > maximum_number:
        maximum_number=number
print(f"The Maximum Number is {maximum_number}")
