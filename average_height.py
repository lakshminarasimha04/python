heights=input("Enter all heights separated by a space: ")
height_list=heights.split( )
count=0
for height in height_list:
    count=count+1
for i in range(count):
    height_list[i] =int(height_list[i])
print(f"Total entered heights is {count}")

total=0
for person in height_list:
    total=person+total
avg=total/count
print(f"Average height is {round(avg)}")
