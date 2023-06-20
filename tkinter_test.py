import tkinter as tk

# Create the main window
window = tk.Tk()

# Function to handle checkbox selection
def handle_checkbox():
    for checkbox in checkboxes:
        state = checkbox["variable"].get()
        print(f"Checkbox {checkbox['text']} selected" if state == 1 else f"Checkbox {checkbox['text']} deselected")

# Input options for checkboxes
options = ["Option 1", "Option 2", "Option 3"]

# List to store checkbox variables and widgets
checkboxes = []

# Create Checkbuttons dynamically
for option in options:
    checkbox_var = tk.IntVar()
    checkbox = tk.Checkbutton(window, text=option, variable=checkbox_var, command=handle_checkbox)
    checkbox.pack()
    checkboxes.append(checkbox)

# Start the event loop
window.mainloop()
