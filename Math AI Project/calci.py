from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def reg():
    import tkinter as tk
    from tkinter import messagebox
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error

    def submit_values(entry_x, entry_y):
        x_input = entry_x.get()
        y_input = entry_y.get()

        try:
            x_values = np.array([float(val) for val in x_input.split(",")])
            y_values = np.array([float(val) for val in y_input.split(",")])

            if len(x_values) != len(y_values):
                raise ValueError("Number of x and y values must be equal")

            confirm = messagebox.askyesno("Confirmation",
                                          "Are these the correct values?\n\nX: {}\nY: {}".format(x_values, y_values))
            if confirm:
                calculate_linear_regression(x_values, y_values)
                entry_x.delete(0, tk.END)
                entry_y.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def calculate_linear_regression(x_values, y_values):
        model = LinearRegression()
        x_values = x_values.reshape(-1, 1)
        model.fit(x_values, y_values)

        # Coefficients
        m = model.coef_[0]
        b = model.intercept_

        # Mean Squared Error
        y_pred = model.predict(x_values)
        mse = mean_squared_error(y_values, y_pred)

        # Plot
        plt.scatter(x_values, y_values, color='blue')
        plt.plot(x_values, model.predict(x_values), color='red')
        plt.title('Linear Regression')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

        # Display Results
        messagebox.showinfo("Results",
                            "Coefficients:\nSlope (m): {}\nIntercept (b): {}\nMean Squared Error: {}".format(m, b, mse))

    def main():
        root = tk.Tk()
        root.title("Linear Regression Calculator")

        label_x = tk.Label(root, text="Enter x values (comma-separated):")
        label_x.pack()
        entry_x = tk.Entry(root)
        entry_x.pack()

        label_y = tk.Label(root, text="Enter y values (comma-separated):")
        label_y.pack()
        entry_y = tk.Entry(root)
        entry_y.pack()

        submit_button = tk.Button(root, text="Submit", command=lambda: submit_values(entry_x, entry_y))
        submit_button.pack()

        root.mainloop()

    if __name__ == "__main__":
        main()


def calc():
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

        operation_label = tk.Label(root, text="Choose Operation (1 to 5):")
        operation_label.grid(row=1, column=0, padx=5, pady=5)
        operation_entry = tk.Entry(root)
        operation_entry.grid(row=1, column=1, padx=5, pady=5)

        options_label = tk.Label(root, text="Options:")
        options_label.grid(row=2, column=0, padx=5, pady=5)
        options_text = tk.Text(root, height=5, width=50)
        options_text.insert(tk.END, "1. Derivative\n"
                                    "2. Double Derivative\n"
                                    "3. Indefinite Integral\n"
                                    "4. Definite Integral\n"
                                    "5. Limit")
        options_text.config(state=tk.DISABLED)
        options_text.grid(row=2, column=1, padx=5, pady=5)

        a_label = tk.Label(root, text="Enter max value:")
        a_label.grid(row=3, column=0, padx=5, pady=5)
        a_entry = tk.Entry(root)
        a_entry.grid(row=3, column=1, padx=5, pady=5)

        b_label = tk.Label(root, text="Enter min value:")
        b_label.grid(row=4, column=0, padx=5, pady=5)
        b_entry = tk.Entry(root)
        b_entry.grid(row=4, column=1, padx=5, pady=5)

        limit_label = tk.Label(root, text="Enter limit value:")
        limit_label.grid(row=5, column=0, padx=5, pady=5)
        limit_entry = tk.Entry(root)
        limit_entry.grid(row=5, column=1, padx=5, pady=5)

        calculate_button = tk.Button(root, text="Calculate",
                                     command=lambda: perform_operation(equation_entry, operation_entry, a_entry,
                                                                       b_entry,
                                                                       limit_entry, result_label))
        calculate_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        result_label = tk.Label(root, text="")
        result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        root.mainloop()

    def perform_operation(equation_entry, operation_entry, a_entry, b_entry, limit_entry, result_label):
        equation = equation_entry.get()
        operation = operation_entry.get()
        try:
            x = sp.Symbol('x')
            operation = int(operation)  # Convert operation to an integer

            if operation == 1:
                result = sp.diff(equation, x)
                result_label.config(text=f"Derivative: {result}")
            elif operation == 2:
                diff_eq = sp.diff(equation, x)
                result = sp.diff(diff_eq, x)
                result_label.config(text=f"Double Derivative: {result}")
            elif operation == 3:
                result = sp.integrate(equation, x)
                result_label.config(text=f"Indefinite Integral: {result}")
            elif operation == 4:
                a = float(a_entry.get())
                b = float(b_entry.get())
                result = sp.integrate(equation, (x, b, a))
                result_label.config(text=f"Definite Integral: {result}")
            elif operation == 5:
                m = float(limit_entry.get())
                limit = sp.limit(equation, x, m)
                result_label.config(text=f"Limit: {limit}")
            else:
                messagebox.showerror("Error", "Invalid Operation")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    main()


def mat():
    import tkinter as tk
    from tkinter import messagebox
    import numpy as np

    def create_widgets(window):
        operations_label = tk.Label(window, text="Choose matrix operation to perform:")
        operations_label.pack()

        operation_desc = ("1: Add Matrices\n"
                          "2: Multiply Matrix with a constant\n"
                          "3: Multiply Matrix with another Matrix\n"
                          "4: Transpose the Matrix\n"
                          "5: Find the Inverse of the Matrix\n"
                          "6: Find the Determinant of the Matrix")

        desc_frame = tk.Frame(window)
        desc_frame.pack()
        desc_label = tk.Label(desc_frame, text="Operation Descriptions:")
        desc_label.pack()
        desc_text = tk.Text(desc_frame, height=10, width=50)
        desc_text.insert(tk.END, operation_desc)
        desc_text.pack()

        operations_frame = tk.Frame(window)
        operations_frame.pack()

        operations_label = tk.Label(operations_frame, text="Enter operation number:")
        operations_label.pack(anchor="w")

        operations_entry = tk.Entry(operations_frame)
        operations_entry.pack(anchor="w")

        tk.Button(window, text="Perform Operation", command=lambda: perform_operation(operations_entry)).pack()

        matrix1_label = tk.Label(window, text="Enter Matrix 1 (each row separated by new line):")
        matrix1_label.pack()

        matrix1_entry = tk.Text(window, height=5, width=50)
        matrix1_entry.pack()

        matrix2_label = tk.Label(window, text="Enter Matrix 2 (each row separated by new line):")
        matrix2_label.pack()

        matrix2_entry = tk.Text(window, height=5, width=50)
        matrix2_entry.pack()

        constant_label = tk.Label(window, text="Enter Constant (for multiplication):")
        constant_label.pack()

        constant_entry = tk.Entry(window)
        constant_entry.pack()

        result_label = tk.Label(window, text="")
        result_label.pack()

        return matrix1_entry, matrix2_entry, constant_entry, result_label

    def perform_operation(operations_entry):
        operation = operations_entry.get()
        if operation == "1":
            perform_add_matrices()
        elif operation == "2":
            perform_multiply_constant()
        elif operation == "3":
            perform_multiply_matrices()
        elif operation == "4":
            perform_transpose()
        elif operation == "5":
            perform_inverse()
        elif operation == "6":
            perform_determinant()

    def accept_matrices(entry):
        try:
            matrix_input = entry.get('1.0', tk.END).strip().split('\n')
            matrix = []
            for row in matrix_input:
                row_elements = list(map(float, row.split()))
                matrix.append(row_elements)

            return np.array(matrix)

        except ValueError as e:
            messagebox.showerror("Error", "Error: " + str(e))

    def perform_add_matrices():
        matrix1 = accept_matrices(matrix1_entry)
        matrix2 = accept_matrices(matrix2_entry)
        if matrix1 is not None and matrix2 is not None:
            if matrix1.shape != matrix2.shape:
                result_label.config(text="Error: Matrices must have the same dimensions.")
            else:
                result = np.add(matrix1, matrix2)
                result_label.config(text="The sum of the two matrices is:\n" + str(result))

    def perform_multiply_constant():
        matrix = accept_matrices(matrix1_entry)
        constant = float(constant_entry.get())
        if matrix is not None:
            result = constant * matrix
            result_label.config(text="The result after multiplying with a constant:\n" + str(result))

    def perform_multiply_matrices():
        matrix1 = accept_matrices(matrix1_entry)
        matrix2 = accept_matrices(matrix2_entry)
        if matrix1 is not None and matrix2 is not None:
            if matrix1.shape[1] != matrix2.shape[0]:
                result_label.config(text="Error: Matrices' dimensions are incompatible for multiplication.")
            else:
                result = np.dot(matrix1, matrix2)
                result_label.config(text="The dot product is:\n" + str(result))

    def perform_transpose():
        matrix = accept_matrices(matrix1_entry)
        if matrix is not None:
            result = np.transpose(matrix)
            result_label.config(text="The transpose of the matrix is:\n" + str(result))

    def perform_inverse():
        matrix = accept_matrices(matrix1_entry)
        if matrix is not None:
            try:
                result = np.linalg.inv(matrix)
                result_label.config(text="The inverse of the matrix is:\n" + str(result))
            except np.linalg.LinAlgError as e:
                result_label.config(text="Error: The matrix is singular and cannot be inverted.")

    def perform_determinant():
        matrix = accept_matrices(matrix1_entry)
        if matrix is not None:
            result = np.linalg.det(matrix)
            result_label.config(text="The determinant of the matrix is:\n" + str(result))

    if __name__ == "__main__":
        window = tk.Tk()
        window.title("Matrix Calculator")
        window.geometry("600x600")  # Increase the window size

        matrix1_entry, matrix2_entry, constant_entry, result_label = create_widgets(window)

        window.mainloop()


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background='Black')
    gui.title('Simple Calculator')
    gui.geometry("270x150")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    button1 = Button(gui, text=' 1 ', fg='black', bg='white',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='white',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='white',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='white',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='white',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='white',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='white',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='white',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='white',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='white',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='white',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='white',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='white',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='white',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='white',
                   command=equal_press, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='white',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column=1)

    Decimal = Button(gui, text='.', fg='black', bg='white',
                     command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)

    regressor = Button(gui, text='Regression', fg='black', bg='white', command=reg, height=1, width=7)
    regressor.grid(row=6, column=1)

    cal = Button(gui, text='Calculus', fg='black', bg='white', command=calc, height=1, width=7)
    cal.grid(row=6, column=2)

    matrix = Button(gui, text='Matrix', fg='black', bg='white', command=mat, height=1, width=7)
    matrix.grid(row=6, column=3)
    gui.mainloop()
