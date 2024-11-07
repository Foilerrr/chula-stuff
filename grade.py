import tkinter as tk
from tkinter import messagebox

# Function to calculate the grade
def calculate_grade():
    try:
        # Get the numerical grade from the entry widget
        num_grade = float(entry.get())

        # Determine the letter grade based on the input
        if num_grade == 4:
            letter_grade = "A"
        elif num_grade == 3.5:
            letter_grade = "B+"
        elif num_grade == 3:
            letter_grade = "B"
        elif num_grade == 2.5:
            letter_grade = "C+"
        elif num_grade == 2:
            letter_grade = "C"
        elif num_grade == 1.5:
            letter_grade = "D+"
        elif num_grade == 1:
            letter_grade = "D"
        else:
            letter_grade = "Invalid grade"

        # Display the result
        result_label.config(text=f"Letter Grade: {letter_grade}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numerical grade.")

# Create the main window
root = tk.Tk()
root.title("Grade Calculator")

# Create and place widgets
label = tk.Label(root, text="Enter Numerical Grade:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

calc_button = tk.Button(root, text="Calculate", command=calculate_grade)
calc_button.pack(pady=10)

result_label = tk.Label(root, text="Letter Grade: ")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
