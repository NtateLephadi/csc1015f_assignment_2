from math import *
pi = 1
denominator = 1
count = 0
while 2 / denominator != 1:
    pi *= 2 / denominator
    if count == 0:
        denominator = sqrt(2)
        count += 1
    else:
        temp_denominator = denominator
        denominator = sqrt(temp_denominator+2)
    
print("Approximation of pi: " + str(round(pi, 3)))
radius = eval(input("Enter the radius:\n"))
area = pi * radius ** 2
print("Area: " + str(round(area, 3)))