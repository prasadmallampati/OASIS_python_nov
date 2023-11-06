import tkinter as tk
from tkinter import ttk

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def on_calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError as e:
        result_label.config(text=f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place widgets
weight_label = ttk.Label(root, text="Enter Weight (kg):")
weight_label.pack()

weight_entry = ttk.Entry(root)
weight_entry.pack()

height_label = ttk.Label(root, text="Enter Height (m):")
height_label.pack()

height_entry = ttk.Entry(root)
height_entry.pack()

calculate_button = ttk.Button(root, text="Calculate BMI", command=on_calculate)
calculate_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
