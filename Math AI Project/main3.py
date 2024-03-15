import tkinter as tk
import numpy as np


class MatrixCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matrix Calculator")
        self.geometry("600x600")  # Increase the window size

        self.operation_var = tk.StringVar(value=" ")
        self.matrix1_entry = None
        self.matrix2_entry = None
        self.constant_entry = None
        self.result_label = None
        self.create_widgets()

    def create_widgets(self):
        operations_label = tk.Label(self, text="Choose matrix operation to perform:")
        operations_label.pack()

        operations_frame = tk.Frame(self)
        operations_frame.pack()

        operations = ["Add Matrices", "Multiply Matrix with a constant", "Multiply Matrix with another Matrix",
                      "Transpose the Matrix", "Find the Inverse of the Matrix", "Find the Determinant of the Matrix"]

        for i, operation in enumerate(operations, start=1):
            tk.Radiobutton(operations_frame, text=operation, variable=self.operation_var,
                           value=str(i)).pack(anchor="w")

        tk.Button(self, text="Perform Operation", command=self.perform_operation).pack()

        matrix1_label = tk.Label(self, text="Enter Matrix 1 (each row separated by new line):")
        matrix1_label.pack()

        self.matrix1_entry = tk.Text(self, height=5, width=50)
        self.matrix1_entry.pack()

        matrix2_label = tk.Label(self, text="Enter Matrix 2 (each row separated by new line):")
        matrix2_label.pack()

        self.matrix2_entry = tk.Text(self, height=5, width=50)
        self.matrix2_entry.pack()

        constant_label = tk.Label(self, text="Enter Constant (for multiplication):")
        constant_label.pack()

        self.constant_entry = tk.Entry(self)
        self.constant_entry.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def accept_matrices(self, entry):
        try:
            matrix_input = entry.get('1.0', tk.END).strip().split('\n')
            matrix = []
            for row in matrix_input:
                row_elements = list(map(float, row.split()))
                matrix.append(row_elements)

            return np.array(matrix)

        except ValueError as e:
            self.result_label.config(text="Error: " + str(e))

    def perform_operation(self):
        operation = self.operation_var.get()
        if operation == "1":
            self.perform_add_matrices()
        elif operation == "2":
            self.perform_multiply_constant()
        elif operation == "3":
            self.perform_multiply_matrices()
        elif operation == "4":
            self.perform_transpose()
        elif operation == "5":
            self.perform_inverse()
        elif operation == "6":
            self.perform_determinant()

    def perform_add_matrices(self):
        matrix1 = self.accept_matrices(self.matrix1_entry)
        matrix2 = self.accept_matrices(self.matrix2_entry)
        if matrix1 is not None and matrix2 is not None:
            if matrix1.shape != matrix2.shape:
                self.result_label.config(text="Error: Matrices must have the same dimensions.")
            else:
                result = np.add(matrix1, matrix2)
                self.result_label.config(text="The sum of the two matrices is:\n" + str(result))

    def perform_multiply_constant(self):
        matrix = self.accept_matrices(self.matrix1_entry)
        constant = float(self.constant_entry.get())
        if matrix is not None:
            result = constant * matrix
            self.result_label.config(text="The result after multiplying with a constant:\n" + str(result))

    def perform_multiply_matrices(self):
        matrix1 = self.accept_matrices(self.matrix1_entry)
        matrix2 = self.accept_matrices(self.matrix2_entry)
        if matrix1 is not None and matrix2 is not None:
            result = np.dot(matrix1, matrix2)
            self.result_label.config(text="The dot product is:\n" + str(result))

    def perform_transpose(self):
        matrix = self.accept_matrices(self.matrix1_entry)
        if matrix is not None:
            result = np.transpose(matrix)
            self.result_label.config(text="The transpose of the matrix is:\n" + str(result))

    def perform_inverse(self):
        matrix = self.accept_matrices(self.matrix1_entry)
        if matrix is not None:
            try:
                result = np.linalg.inv(matrix)
                self.result_label.config(text="The inverse of the matrix is:\n" + str(result))
            except np.linalg.LinAlgError as e:
                self.result_label.config(text="Error: The matrix is singular and cannot be inverted.")

    def perform_determinant(self):
        matrix = self.accept_matrices(self.matrix1_entry)
        if matrix is not None:
            result = np.linalg.det(matrix)
            self.result_label.config(text="The determinant of the matrix is:\n" + str(result))


if __name__ == "__main__":
    app = MatrixCalculator()
    app.mainloop()
