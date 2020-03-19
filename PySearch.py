import tkinter as tk

app = tk.Tk()
app.geometry("300x300")

entry = tk.Entry(app)
placement = tk.Label(app)

guess = []

pi = open("/home/mcarmi/Documents/Programs/PythonPrograms/PySearch/pi.txt", "r").read()

def button():
    global pi
    global guess 

    input_val = entry.get()
    
    if input_val in pi:
        placement.config(text = "That number is " + str(pi.index(input_val)) + " in pi")
        guess.append(input_val + " is " + str(pi.index(input_val)))
        print (guess)

    else:
        placement.config(text = "That number is not in pi")
        guess.append(input_val + " is not in pi" )
        print (guess)


tk.Label(app, text = "Enter a number: ").grid(column = 0, row = 0)
entry.grid(column = 1, row = 0)
tk.Button(app, command = button, text = "Search").grid(column = 1, row = 1)
placement.grid(column = 1, row = 2)


app.mainloop()