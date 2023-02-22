import math

#1. Write a Python program to convert degree to radian.

degree = int(input())
print(degree*math.pi/180)

#2. Write a Python program to calculate the area of a trapezoid.

height = int(input())
first = int(input())
second = int(input())
print(height*first+(abs(second-first)*5/2))

#3. Write a Python program to calculate the area of regular polygon.

side = int(input())
length = int(input())
print(side*(length*length)*(math.cos(math.pi/side)/math.sin(math.pi/side))/4)

#4. Write a Python program to calculate the area of a parallelogram.

length = int(input())
height = int(input())
print(length*height)