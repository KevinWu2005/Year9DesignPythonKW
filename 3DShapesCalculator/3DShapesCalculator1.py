import tkinter as tk
from tkinter import ttk
#WORKING START HOME PAGE GUI
# intializing the window
def calcVolumeCone(radius, height):

	if radius >= 0 and height >= 0:
		volume = math.pi*pow(radius,2)*(height/3)
		volume = round(volume,2)
		return volume	
	else:
		return -1



def calcVolumeCylinder(radius, height):

	if radius >= 0 and height >= 0:
		volume = math.pi*pow(radius,2)*height 
		volume = round(volume,2)
		return volume	
	else:
		return -1



def calcVolumeCube(edge):

	if edge >= 0:
		volume = pow(edge,2)
		volume = round(volume,2)
		return volume
	else:
		return -1

root = tk.Tk()
root.title("3DShapesCalculator")
# configuring size of the window 
root.geometry('750x500')
root.configure(background='light blue')

title = tk.Label(root,text="3DShapesCalculator!")
title = tk.Label(root, text="3DShapesCalculator!", font=("3DShapesCalculator", 32))
title.pack()
title.place(rely=0.15,relx=0.3)
#Cone Button
Cone = tk.Button(root)
Cone.config(text = "Cone Volume Calculator", width = 10, height = 10)
Cone.pack()
Cone.place(height=200,width=200,rely=0.5,relx=0.05)

#Cylinder Button
Cylinder = tk.Button(root)
Cylinder.config(text = "Cylinder Volume Calculator", width = 10, height = 10)
Cylinder.pack()
Cylinder.place(height=200,width=200,rely=0.5,relx=0.35)

#Cube Button
Cube = tk.Button(root)
Cube.config(text = "Cube Volume Calculator", width = 10, height = 10)
Cube.pack()
Cube.place(height=200,width=200,rely=0.5,relx=0.65)

#Calling Main()
root.mainloop()