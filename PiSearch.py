import tkinter as tk
import math as math

app = tk.Tk()
app.geometry("300x300")

entry = tk.Entry(app)

pi = open("pi.txt", "r")

def button():
    global pi

    input_val = entry.get()
    
    if input_val in pi:
        print ("Your number is in pi")
    
    else:
        print("no")

entry.grid(column = 0, row = 0)
tk.Button(app, command = button).grid(column = 0, row = 1)



app.mainloop()