import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class LinearRegressionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Linear Regression Calculator")

        self.label_x = tk.Label(master, text="Enter x values (comma-separated):")
        self.label_x.pack()
        self.entry_x = tk.Entry(master)
        self.entry_x.pack()

        self.label_y = tk.Label(master, text="Enter y values (comma-separated):")
        self.label_y.pack()
        self.entry_y = tk.Entry(master)
        self.entry_y.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_values)
        self.submit_button.pack()

    def submit_values(self):
        x_input = self.entry_x.get()
        y_input = self.entry_y.get()

        try:
            x_values = np.array([float(val) for val in x_input.split(",")])
            y_values = np.array([float(val) for val in y_input.split(",")])

            if len(x_values) != len(y_values):
                raise ValueError("Number of x and y values must be equal")

            confirm = messagebox.askyesno("Confirmation",
                                          "Are these the correct values?\n\nX: {}\nY: {}".format(x_values, y_values))
            if confirm:
                self.calculate_linear_regression(x_values, y_values)
            else:
                self.entry_x.delete(0, tk.END)
                self.entry_y.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def calculate_linear_regression(self, x_values, y_values):
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
    app = LinearRegressionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
