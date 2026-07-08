
import tkinter as tk
from tkinter import messagebox

def press(value):
    entry.insert("end", value)

def clear():
    entry.delete(0, "end")

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert("end", result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        clear()
    except:
        messagebox.showerror("Error", "Invalid Input")
        clear()

root = tk.Tk()

root.title("Calculator")
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