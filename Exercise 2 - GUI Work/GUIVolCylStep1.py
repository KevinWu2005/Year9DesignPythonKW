import math

# Function: a small pieces of code that can called upon and executed
# What it takes
# What does/What it's name is
# what it returns.
'''
This function takes two numeric values and calculates
the volume of a cylinder. It returns the volume. If
the passed parameters are invalid it returns -1
'''
def calcVolCylinder(radius, height):
	if radius >= 0 and height >=0:
		volume = math.pi*pow(radius,2) * height
		volume = round(volume, 2)
		return volume
	else:
		return -1



print("Start Program")
result = calcVolCylinder(23,4)
print(result)
print("End Program")