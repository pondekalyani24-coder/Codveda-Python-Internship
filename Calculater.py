import tkinter as tk
from tkinter import messagebox

# ---------- Calculator Functions ----------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


# ---------- GUI Logic ----------
expression = ""

def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    global expression
    try:
        # Find operator
        if '+' in expression:
            a, b = expression.split('+')
            result = add(float(a), float(b))
        elif '-' in expression:
            a, b = expression.split('-')
            result = subtract(float(a), float(b))
        elif '*' in expression:
            a, b = expression.split('*')
            result = multiply(float(a), float(b))
        elif '/' in expression:
            a, b = expression.split('/')
            result = divide(float(a), float(b))
        else:
            result = expression

        input_text.set(str(result))
        expression = str(result)

    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero not allowed!")
        clear()
    except:
        messagebox.showerror("Error", "Invalid input!")
        clear()


# ---------- GUI Window ----------
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

input_text = tk.StringVar()

display = tk.Entry(root, textvariable=input_text, font=("Arial", 20),
                   bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
display.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14),
                        command=calculate)
    else:
        btn = tk.Button(frame, text=text, width=5, height=2, font=("Arial", 14),
                        command=lambda t=text: press(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(root, text="Clear", width=22, height=2,
                      font=("Arial", 12), command=clear)
clear_btn.pack(pady=10)

root.mainloop()
