import tkinter as tk

window = tk.Tk()

# Adds a title to the window
window.title("My Awesome App")

window.geometry("300x300")

# Create label

prompt = tk.Label(text="Hello World. Welcome to CS50 Awesome App.")
prompt.grid()

# Create Entry Field
entry_field1 = tk.Entry()
entry_field1.grid()

# Create Button One

button1 = tk.Button(text="CLICK ME!")
button1.grid()

# Create Text Field
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid()

window.mainloop()
