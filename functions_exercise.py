from math import ceil
def paint_calc(height,width,coverage):
    area=height * width
    number_of_cans= area / coverage
    number_of_cans=ceil(number_of_cans)
    print(f"You'll need {number_of_cans} cans of paint.")

paint_calc(5,10,7)
    
