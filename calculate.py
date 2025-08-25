import math
import tkinter as tk
from tkinter import messagebox

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(self.root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=10, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Trigonometric buttons
        tk.Button(self.root, text="sin", width=10, command=self.sin).grid(row=row_val, column=0)
        tk.Button(self.root, text="cos", width=10, command=self.cos).grid(row=row_val, column=1)
        tk.Button(self.root, text="tan", width=10, command=self.tan).grid(row=row_val, column=2)
        tk.Button(self.root, text="Clear", width=10, command=self.clear).grid(row=row_val, column=3)

        # Exponential and logarithmic buttons
        row_val += 1
        tk.Button(self.root, text="x^2", width=10, command=self.square).grid(row=row_val, column=0)
        tk.Button(self.root, text="x^3", width=10, command=self.cube).grid(row=row_val, column=1)
        tk.Button(self.root, text="log", width=10, command=self.log).grid(row=row_val, column=2)
        tk.Button(self.root, text="ln", width=10, command=self.natural_log).grid(row=row_val, column=3)

        # Other buttons
        row_val += 1
        tk.Button(self.root, text="sqrt", width=10, command=self.sqrt).grid(row=row_val, column=0)
        tk.Button(self.root, text="1/x", width=10, command=self.reciprocal).grid(row=row_val, column=1)
        tk.Button(self.root, text="Exit", width=10, command=self.root.quit).grid(row=row_val, column=2)
        tk.Button(self.root, text="Help", width=10, command=self.help).grid(row=row_val, column=3)

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entry.insert(tk.END, button)

    def sin(self):
        try:
            result = math.sin(math.radians(float(self.entry.get())))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def cos(self):
        try:
            result = math.cos(math.radians(float(self.entry.get())))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def tan(self):
        try:
            result = math.tan(math.radians(float(self.entry.get())))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def square(self):
        try:
            result = float(self.entry.get()) ** 2
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def cube(self):
        try:
            result = float(self.entry.get()) ** 3
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def log(self):
        try:
            result = math.log10(float(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def natural_log(self):
        try:
            result = math.log(float(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def sqrt(self):
        try:
            result = math.sqrt(float(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reciprocal(self):
        try:
            result = 1 / float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear(self):
        self.entry.delete(0, tk.END)

    def help(self):
        messagebox.showinfo("Help", "This is an advanced calculator with trigonometric, exponential, and logarithmic functions.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Advanced Calculator")
    calc = AdvancedCalculator(root)
    root.mainloop()
