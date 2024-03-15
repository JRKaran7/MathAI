import tkinter as tk
from tkinter import messagebox
import sympy as sp


def main():
    root = tk.Tk()
    root.title("Equation Operations")

    equation_label = tk.Label(root, text="Enter the Equation:")
    equation_label.grid(row=0, column=0, padx=5, pady=5)
    equation_entry = tk.Entry(root)
    equation_entry.grid(row=0, column=1, padx=5, pady=5)

    operation_label = tk.Label(root, text="Choose Operation:")
    operation_label.grid(row=1, column=0, padx=5, pady=5)
    operation_var = tk.IntVar()
    operation_var.set(1)  # Default value
    operations = [("Derivative", 1), ("Double Derivative", 2), ("Indefinite Integral", 3),
                  ("Definite Integral", 4), ("Limit", 5)]
    for text, val in operations:
        tk.Radiobutton(root, text=text, variable=operation_var, value=val).grid(row=1, column=val, padx=5, pady=5)

    a_label = tk.Label(root, text="Enter max value:")
    a_label.grid(row=2, column=3, padx=5, pady=5)
    a_entry = tk.Entry(root)
    a_entry.grid(row=2, column=4, padx=5, pady=5)

    b_label = tk.Label(root, text="Enter min value:")
    b_label.grid(row=3, column=3, padx=5, pady=5)
    b_entry = tk.Entry(root)
    b_entry.grid(row=3, column=4, padx=5, pady=5)

    limit_label = tk.Label(root, text="Enter limit value:")
    limit_label.grid(row=4, column=3, padx=5, pady=5)
    limit_entry = tk.Entry(root)
    limit_entry.grid(row=4, column=4, padx=5, pady=5)

    calculate_button = tk.Button(root, text="Calculate", command=perform_operation)
    calculate_button.grid(row=5, column=0, columnspan=5, padx=5, pady=5)

    result_label = tk.Label(root, text="")
    result_label.grid(row=6, column=0, columnspan=5, padx=5, pady=5)

    root.mainloop()


def perform_operation():
    equation = main.equation_entry.get()
    try:
        x = sp.Symbol('x')
        operation = main.operation_var.get()

        if operation == 1:
            result = sp.diff(equation, x)
            main.result_label.config(text=f"Derivative: {result}")
        elif operation == 2:
            diff_eq = sp.diff(equation, x)
            result = sp.diff(diff_eq, x)
            main.result_label.config(text=f"Double Derivative: {result}")
        elif operation == 3:
            result = sp.integrate(equation, x)
            main.result_label.config(text=f"Indefinite Integral: {result}")
        elif operation == 4:
            a = float(main.a_entry.get())
            b = float(main.b_entry.get())
            result = sp.integrate(equation, (x, b, a))
            main.result_label.config(text=f"Definite Integral: {result}")
        elif operation == 5:
            m = float(main.limit_entry.get())
            limit = sp.limit(equation, x, m)
            main.result_label.config(text=f"Limit: {limit}")
        else:
            messagebox.showerror("Error", "Invalid Operation")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

