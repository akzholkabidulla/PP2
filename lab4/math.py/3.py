from math import tan
import math
n = int(input("Input number of sides:"))
length = int(input("input the length of a side:"))
area = (n*pow(length,2))/4*math.tan(math.pi/n)
print(f"The area of the polygon is:{area}")
