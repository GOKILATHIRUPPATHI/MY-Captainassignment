import math
radius = float(input("Input the radius of the circle: "))
x=area = math.pi * radius ** 2
print("The area of the circle with radius is " ,x)

filename = input("Input the FileName: ")
f_extns = filename.split(".")
py='python'
print ("The extension of the file is : " + repr(f_extns[-1]),repr(py))
