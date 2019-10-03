import tkinter as tk

print("Start Program")
root = tk.Tk() #builds your main window
root.title("Story Writing Practice")
#Widget/Element is an element in a GUI, Button, Textbox, input box, slider

#Step 1: Construct the widget.
btn1 = tk.Button(root)
#Step 2: Configure the widget.
btn1.config(text = "Type Below", width = 100, height = 3)
#Step 3: Place the widget - pack(), grid(), 
btn1.pack()

output = tk.Text(root, width = 100, height = 20)
output.config()
output.pack()

#new widget
#Step 1: Construct the widget.
btn1 = tk.Button(root)
#Step 2: Configure the widget.
btn1.config(text = "Every secret of a writer's soul, every experience of his life, every quality of his mind, is written large in his works", width = 100, height = 3)
#Step 3: Place the widget - pack(), grid(), 
btn1.pack()

root.mainloop()

print("END PROGRAM")



