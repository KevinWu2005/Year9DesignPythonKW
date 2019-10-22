import math
import tkinter as tk
from tkinter import ttk

print("Start Program")
root = tk.Tk() #builds your main window
root.title("Volume calculator for 3D Shapes")

tab = tkk.Notebook()

tab1=tkk.Frame(tab)
tab.add(tab1,text="Cylinder")
tab.pack(expand=1,fill="both")

tab2=tkk.Frame(tab)
tab.add(tab2,text="Cone")
tab.pack(expand=1,fill="both")

tab3=tkk.Frame(tab)
tab.add(tab3,text="Cube")
tab.pack(expand=1,fill="both")

tab4=tkk.Frame(tab)
tab.add(tab4,text="Rectangular Prism")
tab.pack(expand=1,fill="both")

#Step 1: Construct the widget.
#btn1 = tk.Button(root)
#Step 2: Configure the widget.
#btn1.config(text = "Cylinder Volume Calculator", width = 100, height = 5)
#Step 3: Place the widget - pack(), grid(), 
#btn1.pack()

# btn2 = tk.Button(root)
# btn2.config(text = "Cone Volume Calculator", width = 100, height = 5)
# btn2.pack()

# btn3 = tk.Button(root)
# btn3.config(text = "Cube Volume Calculator", width = 100, height = 5)
# btn3.pack()

# btn4 = tk.Button(root)
# btn4.config(text = "Rectangular Prism Volume Calculator", width = 100, height = 5)
# btn4.pack()

#output = tk.Text(root, width = 100, height = 20)
#output.config()
#output.pack()

root.mainloop()

print("END PROGRAM")



