import tkinter as tk
import random

# Function to guess the number
def guess_number():
    lower_bound = int(entry_lower.get())
    upper_bound = int(entry_upper.get())

    if lower_bound >= upper_bound:
        lbl_result.config(text="Lower bound must be less than upper bound.")
        return

    guessed_number = random.randint(lower_bound, upper_bound)
    lbl_result.config(text=f"I guess your number is: {guessed_number}")

# Create the main window
window = tk.Tk()
window.title("Mind Reader")

# Create input widgets
lbl_instruction = tk.Label(window, text="Think of a number within a range:")
lbl_instruction.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

lbl_range = tk.Label(window, text="Range:")
lbl_range.grid(row=1, column=0, padx=5, pady=5)

entry_lower = tk.Entry(window, width=5)
entry_lower.grid(row=1, column=1, padx=5, pady=5)

lbl_to = tk.Label(window, text="to")
lbl_to.grid(row=1, column=2, padx=5, pady=5)

entry_upper = tk.Entry(window, width=5)
entry_upper.grid(row=1, column=3, padx=5, pady=5)

btn_guess = tk.Button(window, text="Guess", command=guess_number)
btn_guess.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

lbl_result = tk.Label(window, text="")
lbl_result.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()
