import tkinter as tk
from tkinter import ttk

# intializing the window
root = tk.Tk()
root.title("3DShapesCalculator")
# configuring size of the window 
root.geometry('750x500')

title = tk.Label(root,text="3DShapesCalculator!")
title = tk.Label(root, text="3DShapesCalculator!", font=("3DShapesCalculator", 32))
title.pack()

#Cone Button
Cone = tk.Button(root)
Cone.config(text = "Cone Volume Calculator", width = 10, height = 10)
Cone.pack()

#Cylinder Button
Cylinder = tk.Button(root)
Cylinder.config(text = "Cylinder Volume Calculator", width = 10, height = 10)
Cylinder.pack()

#Cube Button
Cube = tk.Button(root)
Cube.config(text = "Cube Volume Calculator", width = 10, height = 10)
Cube.pack()


#Calling Main()
root.mainloop()