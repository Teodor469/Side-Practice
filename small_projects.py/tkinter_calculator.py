from tkinter import *
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Simple calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def devision(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return "Devision by zero is impossible"
    
def button_add(number):
    e.delete(0, END)
    e.insert(0, number)


#Creating the buttons
button_1 = tk.Button(root, text='1', padx=40, pady=20, command=lambda: button_add(1))
button_2 = tk.Button(root, text='2', padx=40, pady=20, command=lambda: button_add(2))
button_3 = tk.Button(root, text='3', padx=40, pady=20, command=lambda: button_add(3))
button_4 = tk.Button(root, text='4', padx=40, pady=20, command=lambda: button_add(4))
button_5 = tk.Button(root, text='5', padx=40, pady=20, command=lambda: button_add(5))
button_6 = tk.Button(root, text='6', padx=40, pady=20, command=lambda: button_add(6))
button_7 = tk.Button(root, text='7', padx=40, pady=20, command=lambda: button_add(7))
button_8 = tk.Button(root, text='8', padx=40, pady=20, command=lambda: button_add(8))
button_9 = tk.Button(root, text='9', padx=40, pady=20, command=lambda: button_add(9))
button_0 = tk.Button(root, text='0', padx=40, pady=20, command=lambda: button_add(0))
add_button = tk.Button(root, text='+', padx=39, pady=20, command=lambda: button_add('+'))
subtract_button = tk.Button(root, text='-', padx=40, pady=20, command=lambda: button_add('-'))
multiply_button = tk.Button(root, text='*', padx=40, pady=20, command=lambda: button_add('*'))
devide_button = tk.Button(root, text='/', padx=40, pady=20, command=lambda: button_add('/'))
equal_button = tk.Button(root, text='=', padx=39, pady=20, command=lambda: button_add('='))
clear_button = tk.Button(root, text='C', padx=86.5, pady=20, command=lambda: button_add('C'))


#Adding button grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
clear_button.grid(row=4, column=1, columnspan=2)
add_button.grid(row=4, column=3)
subtract_button.grid(row=3, column=3)
multiply_button.grid(row=2, column=3)
devide_button.grid(row=1, column=3)
equal_button.grid(row=5, column=0)

root.mainloop()