import tkinter as tk

# Create window
root = tk.Tk()
root.title("Mathematical Calculator")
root.geometry("400x500")
root.resizable(False, False)

# Display
display = tk.Entry(root, font=("Arial", 20), justify="right", bd=8)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=15)

# Function to add numbers/operators
def click(value):
    display.insert(tk.END, value)

# Function to calculate answer
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Function to clear screen
def clear():
    display.delete(0, tk.END)

# Function to close calculator
def close():
    root.destroy()

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('%',4,1), ('^',4,2), ('+',4,3),
]

# Create buttons
for (text,row,col) in buttons:
    if text == "^":
        tk.Button(
            root,
            text=text,
            width=8,
            height=3,
            command=lambda: click("**")
        ).grid(row=row,column=col,padx=5,pady=5)
    else:
        tk.Button(
            root,
            text=text,
            width=8,
            height=3,
            command=lambda t=text: click(t)
        ).grid(row=row,column=col,padx=5,pady=5)

# Bottom buttons
tk.Button(root,text="C",width=8,height=3,command=clear).grid(row=5,column=0,padx=5,pady=5)
tk.Button(root,text="=",width=8,height=3,command=calculate).grid(row=5,column=1,padx=5,pady=5)
tk.Button(root,text="OFF",width=8,height=3,command=close).grid(row=5,column=2,columnspan=2,padx=5,pady=5)

root.mainloop()