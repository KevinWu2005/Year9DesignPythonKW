import math
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#Functions
def on_closing():
	print("closing")
	#Step 2 create messagebox
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()
def calcVolumeCone(*args):

	if int(cone1.get()) >= 0 and int(cone2.get()) >= 0:
		volume = math.pi*pow(int(cone1.get()),2)*(int(cylinder2.get())/3)
		volume = round(volume,2)
		messagebox.showinfo("Answer",str(volume))
	else:
		return -1
def calcVolumeCylinder(*args):

	if int(cylinder1.get()) >= 0 and int(cylinder2.get()) >= 0:
		volume = math.pi*pow(int(cylinder1.get()),2)*(int(cylinder2.get()))
		volume = round(volume,2)
		messagebox.showinfo("Answer",str(volume))
	else:
		return -1

def calcVolumeCube(*args):

	if int(cube1.get()) >= 0:
		volume = pow(int(cube1.get()),3)
		volume = round(volume,2)
		messagebox.showinfo("Answer",str(volume))
	
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
conebutton = tk.Button(home)
conebutton.config(text = "Cone Volume Calculator", width = 10, height = 10)
conebutton.pack()
conebutton.place(height=200,width=200,rely=0.5,relx=0.05)
#Cylinder Button
cylinderbutton = tk.Button(home)
cylinderbutton.config(text = "Cylinder Volume Calculator", width = 10, height = 10)
cylinderbutton.pack()
cylinderbutton.place(height=200,width=200,rely=0.5,relx=0.35)
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
#ENTRY
ttk.Label(cone, text="Radius").place(rely=0.3,relx=0.35)
ttk.Label(cone, text="Height").place(rely=0.35,relx=0.35)
cone1 = ttk.Entry(cone)
cone2 = ttk.Entry(cone)
cone2.bind("<Return>",calcVolumeCone)
cone1.place(rely=0.3,relx=0.43)
cone2.place(rely=0.35,relx=0.43)


#CYLINDER TAB
cylinder = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(cylinder, text='CylinderVolumeCalculator')
TAB_CONTROL.pack(expand=1, fill="both")
ttk.Label(cylinder, text="Cylinder Formula = πr^2h ", font=("Cylinder Formula = πr^2h ", 32)).place(rely=0.15,relx=0.3)
#ENTRY
ttk.Label(cylinder, text="Radius").place(rely=0.3,relx=0.35)
ttk.Label(cylinder, text="Height").place(rely=0.35,relx=0.35)
cylinder1 = ttk.Entry(cylinder)
cylinder2 = ttk.Entry(cylinder)
cylinder2.bind("<Return>",calcVolumeCylinder)
cylinder1.place(rely=0.3,relx=0.43)
cylinder2.place(rely=0.35,relx=0.43)

#CUBE TAB
cube = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(cube, text='CubeVolumeCalculator')
TAB_CONTROL.pack(expand=1, fill="both")
ttk.Label(cube, text="Cube Formula = S^3", font=("Cube Formula = S^3", 32)).place(rely=0.15,relx=0.3)
#ENTRY
ttk.Label(cube, text="Side Length").place(rely=0.3,relx=0.30)
cube1 = ttk.Entry(cube)
cube1.bind("<Return>",calcVolumeCube)
cube1.place(rely=0.3,relx=0.43)



#Calling Main()
root.protocol("WM_DELETE_WINDOW",on_closing)
root.mainloop()