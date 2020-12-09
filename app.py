import tkinter as tk

window = tk.Tk()

window.title("My App")

window.geometry("400x400")

# Create label

title = tk.Label(text="Hello World. Welcome to CS50 and to the GUI created.")
title.grid(column=0, row=0)

# Create Button One

button1 = tk.Button(text="Click Me!")
button1.grid(column=0, row=1)

# Create Entry Field
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

window.mainloop()
