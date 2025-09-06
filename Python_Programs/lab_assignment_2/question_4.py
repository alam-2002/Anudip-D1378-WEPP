# Q4) Python program to find the area of a triangle whose sides are given

side1 = 25
side2 = 35
side3 = 15

# Calculate the semi-perimeter (s)
s = (side1 + side2 + side3) / 2

# Calculate the area using formula
area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5

# Print the calculated area
print("Area of the triangle is:", area) 

'''
OutPut:- 
Area of the triangle is: 162.37976320958225
'''
