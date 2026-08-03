import tkinter as tk
from tkinter import messagebox
<<<<<<< HEAD

def press(value):
    entry.insert("end", value)

def clear():
    entry.delete(0, "end")

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert("end", result)
=======
# Add the clicked button value to the calculator display
def press(value):
    entry.insert("end", value)
# Clear everything from the display
def clear():
    entry.delete(0, "end")
# Evaluate the entered mathematical expression
def calculate():
    try:
# Calculate the result from the user's input
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert("end", result)
# Show an error if the user tries to divide y zero
>>>>>>> d9abbec (Update calculator project)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        clear()
# Handle invalid expressions
    except SyntaxError:
        messagebox.showerror("Error", "Invalid Input")
        clear()
<<<<<<< HEAD

=======
# Create the main application window
>>>>>>> d9abbec (Update calculator project)
root = tk.Tk()

root.title("Calculator")
<<<<<<< HEAD
root.geometry("300x350")

entry = tk.Entry(root, width=25)
entry.grid(row=0, column=0, columnspan=4)

button7 = tk.Button(root, text="7", width=5, command=lambda: press("7"))
button7.grid(row=1, column=0)

button8 = tk.Button(root, text="8", width=5, command=lambda: press("8"))
button8.grid(row=1, column=1)

button9 = tk.Button(root, text="9", width=5, command=lambda: press("9"))
button9.grid(row=1, column=2)

buttonDivide = tk.Button(root, text="/", width=5, command=lambda: press("/"))
buttonDivide.grid(row=1, column=3)

button4 = tk.Button(root, text="4", width=5, command=lambda: press("4"))
button4.grid(row=2, column=0)

button5 = tk.Button(root, text="5", width=5, command=lambda: press("5"))
button5.grid(row=2, column=1)

button6 = tk.Button(root, text="6", width=5, command=lambda: press("6"))
button6.grid(row=2, column=2)

buttonMultiply = tk.Button(root, text="*", width=5, command=lambda: press("*"))
buttonMultiply.grid(row=2, column=3)

button1 = tk.Button(root, text="1", width=5, command=lambda: press("1"))
button1.grid(row=3, column=0)

button2 = tk.Button(root, text="2", width=5, command=lambda: press("2"))
button2.grid(row=3, column=1)

button3 = tk.Button(root, text="3", width=5, command=lambda: press("3"))
button3.grid(row=3, column=2)

buttonMinus = tk.Button(root, text="-", width=5, command=lambda: press("-"))
buttonMinus.grid(row=3, column=3)

button0 = tk.Button(root, text="0", width=5, command=lambda: press("0"))
button0.grid(row=4, column=0)

buttonClear = tk.Button(root, text="C", width=5, command=clear)
buttonClear.grid(row=4, column=1)

buttonEqual = tk.Button(root, text="=", width=5, command=calculate)
buttonEqual.grid(row=4, column=2)

buttonPlus = tk.Button(root, text="+", width=5, command=lambda: press("+"))
buttonPlus.grid(row=4, column=3)

root.mainloop()
=======
root.geometry("300x420")
root.resizable(False,False)
# Calculator display
entry = tk.Entry(root, width=25,font=("Arial",16),justify="right")
entry.grid(row=0, column=0, columnspan=4,padx=10,pady=10)
button_7 = tk.Button(root, text="7", width=6,height=2, command=lambda: press("7"))
button_7.grid(row=1, column=0)
button_8 = tk.Button(root, text="8", width=6,height=2, command=lambda: press("8"))
button_8.grid(row=1, column=1)
button_9 = tk.Button(root, text="9", width=6,height=2, command=lambda: press("9"))
button_9.grid(row=1, column=2)
button_divide = tk.Button(root, text="/", width=6,height=2, command=lambda: press("/"))
button_divide.grid(row=1, column=3)
button_4 = tk.Button(root, text="4", width=6,height=2, command=lambda: press("4"))
button_4.grid(row=2, column=0)
button_5 = tk.Button(root, text="5", width=6,height=2, command=lambda: press("5"))
button_5.grid(row=2, column=1)
button_6 = tk.Button(root, text="6", width=6,height=2, command=lambda: press("6"))
button_6.grid(row=2, column=2)
button_multiply = tk.Button(root, text="*", width=6,height=2, command=lambda: press("*"))
button_multiply.grid(row=2, column=3)
button_1 = tk.Button(root, text="1", width=6,height=2, command=lambda: press("1"))
button_1.grid(row=3, column=0)
button_2 = tk.Button(root, text="2", width=6,height=2, command=lambda: press("2"))
button_2.grid(row=3, column=1)
button_3 = tk.Button(root, text="3", width=6,height=2, command=lambda: press("3"))
button_3.grid(row=3, column=2)
button_minus = tk.Button(root, text="-", width=6,height=2, command=lambda: press("-"))
button_minus.grid(row=3, column=3)
button_0 = tk.Button(root, text="0", width=6,height=2, command=lambda: press("0"))
button_0.grid(row=4, column=0)
button_clear = tk.Button(root, text="C", width=6,height=2, command=clear)
button_clear.grid(row=4, column=1)
button_equal = tk.Button(root, text="=", width=6,height=2, command=calculate)
button_equal.grid(row=4, column=2)
button_plus = tk.Button(root, text="+", width=6,height=2, command=lambda: press("+"))
button_plus.grid(row=4, column=3)
button_decimal = tk.Button(
    root,
    text=".",
    width=6,
    height=2,
    command=lambda: press(".")
)
button_decimal.grid(row=5,column=0)
root.mainloop()

>>>>>>> d9abbec (Update calculator project)
