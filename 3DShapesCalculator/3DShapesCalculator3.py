import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#Functions
def on_closing():
	print("closing")
	#Step 2 create messagebox
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()
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

#Create Tab Control
TAB_CONTROL = ttk.Notebook(root)

#FRONT PAGE
home = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(home, text='HomePage')
title = ttk.Label(home, text="3DShapesCalculator!", font=("3DShapesCalculator", 32))
title.pack()
title.place(rely=0.15,relx=0.3)
subtitle = ttk.Label(home, text="Click above to begin!",font=("Click above to begin!",24))
subtitle.pack()
subtitle.place(rely=0.29,relx=0.33)


#Cone Button
cone = tk.Button(home)
cone.config(text = "Cone Volume Calculator", width = 10, height = 10)
cone.pack()
cone.place(height=200,width=200,rely=0.5,relx=0.05)
#Cylinder Button
cylinder = tk.Button(home)
cylinder.config(text = "Cylinder Volume Calculator", width = 10, height = 10)
cylinder.pack()
cylinder.place(height=200,width=200,rely=0.5,relx=0.35)
#Cube Button
cubebutton = tk.Button(home)
cubebutton.config(text = "Cube Volume Calculator", width = 10, height = 10)
cubebutton.pack()
cubebutton.place(height=200,width=200,rely=0.5,relx=0.65)



#CONE TAB
cone = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(cone, text='ConeVolumeCalculator')
TAB_CONTROL.pack(expand=1, fill="both")
ttk.Label(cone, text="Cone Formula = πr^2(1/3h)", font=("Cone Formula = πr^2(1/3h)", 32)).place(rely=0.15,relx=0.3)

#CYLINDER TAB
cylinder = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(cylinder, text='CylinderVolumeCalculator')
TAB_CONTROL.pack(expand=1, fill="both")
ttk.Label(cylinder, text="Cylinder Formula = πr^2h ", font=("Cylinder Formula = πr^2h ", 32)).place(rely=0.15,relx=0.3)


#CUBE TAB
cube = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(cube, text='CubeVolumeCalculator')
TAB_CONTROL.pack(expand=1, fill="both")
ttk.Label(cube, text="Cube Formula = S^3", font=("Cube Formula = S^3", 32)).place(rely=0.15,relx=0.3)


#Calling Main()
root.protocol("WM_DELETE_WINDOW",on_closing)
root.mainloop()