import math
def paint_calc(height,width,coverage):
    area=height * width
    number_of_cans= area / coverage
    number_of_cans=ceil(number_of_cans)
    print(f"You'll need {number_of_cans} cans of paint.")
h=int(input("Enter the height of wall in meters:"))
w=int(input("Enter the width of wall in meters:"))

paint_calc(height=h,width=w,coverage=7)  
