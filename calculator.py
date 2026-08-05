import tkinter as tk
from tkinter import messagebox

# ---------- Functions ----------

# Add the button value to whatever is already in the display
def press(value):
    entry.insert("end", value)

# Clear button - empties the display
def clear():
    entry.delete(0, "end")

# Backspace button - removes the last character from the display
def backspace():
    current_text = entry.get()
    entry.delete(0, "end")
    entry.insert("end", current_text[:-1])

# Solve whatever expression is currently in the display
def calculate():
    try:
        # eval() solves the full expression (e.g. "5+3*2")
        # using eval() here since this is just a beginner project
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert("end", result)
    except ZeroDivisionError:
        # dividing by 0
        messagebox.showerror("Error", "Cannot divide by zero")
        clear()
    except SyntaxError:
        # something like "5++" that doesn't make sense
        messagebox.showerror("Error", "Invalid Input")
        clear()
    except Exception:
        # catch anything else I didn't think of
        messagebox.showerror("Error", "Something went wrong")
        clear()


# ---------- Main Window ----------

root = tk.Tk()
root.title("Calculator")
root.geometry("300x420")
root.resizable(False, False)  # keep the window size fixed

# Display box
entry = tk.Entry(root, width=25, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# ---------- Number Buttons (1-9) ----------
# instead of writing a separate button for each number, using a loop
# so the code doesn't repeat itself

numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
positions = [
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2),
    (3, 0), (3, 1), (3, 2),
]

for number, position in zip(numbers, positions):
    row, column = position
    button = tk.Button(
        root, text=number, width=6, height=2,
        command=lambda n=number: press(n)   # n=number locks in the current value for each button
    )
    button.grid(row=row, column=column)


# ---------- Operator Buttons ----------

button_divide = tk.Button(root, text="/", width=6, height=2, command=lambda: press("/"))
button_divide.grid(row=1, column=3)

button_multiply = tk.Button(root, text="*", width=6, height=2, command=lambda: press("*"))
button_multiply.grid(row=2, column=3)

button_minus = tk.Button(root, text="-", width=6, height=2, command=lambda: press("-"))
button_minus.grid(row=3, column=3)

button_plus = tk.Button(root, text="+", width=6, height=2, command=lambda: press("+"))
button_plus.grid(row=4, column=3)

button_percent = tk.Button(root, text="%", width=6, height=2, command=lambda: press("%"))
button_percent.grid(row=5, column=3)


# ---------- Bottom Row Buttons ----------

button_0 = tk.Button(root, text="0", width=6, height=2, command=lambda: press("0"))
button_0.grid(row=4, column=0)

button_clear = tk.Button(root, text="C", width=6, height=2, command=clear)
button_clear.grid(row=4, column=1)

button_equal = tk.Button(root, text="=", width=6, height=2, command=calculate)
button_equal.grid(row=4, column=2)

button_decimal = tk.Button(root, text=".", width=6, height=2, command=lambda: press("."))
button_decimal.grid(row=5, column=0)

button_backspace = tk.Button(root, text="⌫", width=6, height=2, command=backspace)
button_backspace.grid(row=5, column=1)


root.mainloop()
