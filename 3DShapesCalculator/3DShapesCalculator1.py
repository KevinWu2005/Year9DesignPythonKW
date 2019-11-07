import tkinter as tk
from tkinter import ttk

# intializing the window
root = tk.Tk()
root.title("3DShapesCalculator")
# configuring size of the window 
root.geometry('750x500')
#Tab Name Labels
ttk.Label(text="3DShapesCalculator").grid(column=0, row=0, padx=310, pady=50)

#Calling Main()
root.mainloop()