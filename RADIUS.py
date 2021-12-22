import math
radius = float(input("Input the radius of the circle: "))
x=area = math.pi * radius ** 2
print("The area of the circle with radius is " ,x)

filename = input("Input the Filename: ")
f = filename.split(".")
print ("The extension of the file is : " + (f[-1]))
