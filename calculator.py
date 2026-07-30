import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------
# Function to handle number/operator button presses.
# Inserts the given value at the end of the entry field.
# ---------------------------------------------------------
def press(value):
    entry.insert("end", value)

# ---------------------------------------------------------
# Function to clear the entry field completely.
# ---------------------------------------------------------
def clear():
    entry.delete(0, "end")

# ---------------------------------------------------------
# Function to evaluate the expression typed in the entry field.
# Uses eval() to compute the result of the math expression.
# Handles division by zero and other invalid inputs with
# error popups, then clears the entry field.
# ---------------------------------------------------------
def calculate():
    try:
        result = eval(entry.get())      # Evaluate the expression as Python code
        entry.delete(0, "end")          # Clear the entry before showing the result
        entry.insert("end", result)     # Display the calculated result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        clear()
    except:
        messagebox.showerror("Error", "Invalid Input")
        clear()

# ---------------------------------------------------------
# Main application window setup
# ---------------------------------------------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

# Entry widget where the expression/result is displayed
entry = tk.Entry(root, width=25)
entry.grid(row=0, column=0, columnspan=4)

# ---------------------------------------------------------
# Row 1: buttons 7, 8, 9, and division operator
# ---------------------------------------------------------
button7 = tk.Button(root, text="7", width=5, command=lambda: press("7"))
button7.grid(row=1, column=0)

button8 = tk.Button(root, text="8", width=5, command=lambda: press("8"))
button8.grid(row=1, column=1)

button9 = tk.Button(root, text="9", width=5, command=lambda: press("9"))
button9.grid(row=1, column=2)

buttonDivide = tk.Button(root, text="/", width=5, command=lambda: press("/"))
buttonDivide.grid(row=1, column=3)

# ---------------------------------------------------------
# Row 2: buttons 4, 5, 6, and multiplication operator
# ---------------------------------------------------------
button4 = tk.Button(root, text="4", width=5, command=lambda: press("4"))
button4.grid(row=2, column=0)

button5 = tk.Button(root, text="5", width=5, command=lambda: press("5"))
button5.grid(row=2, column=1)

button6 = tk.Button(root, text="6", width=5, command=lambda: press("6"))
button6.grid(row=2, column=2)

buttonMultiply = tk.Button(root, text="*", width=5, command=lambda: press("*"))
buttonMultiply.grid(row=2, column=3)

# ---------------------------------------------------------
# Row 3: buttons 1, 2, 3, and subtraction operator
# ---------------------------------------------------------
button1 = tk.Button(root, text="1", width=5, command=lambda: press("1"))
button1.grid(row=3, column=0)

button2 = tk.Button(root, text="2", width=5, command=lambda: press("2"))
button2.grid(row=3, column=1)

button3 = tk.Button(root, text="3", width=5, command=lambda: press("3"))
button3.grid(row=3, column=2)

buttonMinus = tk.Button(root, text="-", width=5, command=lambda: press("-"))
buttonMinus.grid(row=3, column=3)

# ---------------------------------------------------------
# Row 4: button 0, clear (C), equals (=), and addition operator
# ---------------------------------------------------------
button0 = tk.Button(root, text="0", width=5, command=lambda: press("0"))
button0.grid(row=4, column=0)

buttonClear = tk.Button(root, text="C", width=5, command=clear)
buttonClear.grid(row=4, column=1)

buttonEqual = tk.Button(root, text="=", width=5, command=calculate)
buttonEqual.grid(row=4, column=2)

buttonPlus = tk.Button(root, text="+", width=5, command=lambda: press("+"))
buttonPlus.grid(row=4, column=3)

# ---------------------------------------------------------
# Start the Tkinter event loop (keeps the window open and
# responsive to user interaction)
# ---------------------------------------------------------
root.mainloop()
