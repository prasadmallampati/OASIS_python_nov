import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True, complex_rules=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    if complex_rules:
        # Ensure at least one character from each selected set
        if use_letters:
            characters += random.choice(string.ascii_letters)
        if use_numbers:
            characters += random.choice(string.digits)
        if use_symbols:
            characters += random.choice(string.punctuation)

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    length = length_var.get()
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    complex_rules = complex_rules_var.get()

    password = generate_password(length, use_letters, use_numbers, use_symbols, complex_rules)

    if password:
        result_label.config(text="Generated Password: " + password)
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

length_label = ttk.Label(main_frame, text="Password Length:")
length_label.grid(column=0, row=0, sticky=tk.W)

length_var = tk.IntVar(value=12)
length_entry = ttk.Entry(main_frame, textvariable=length_var)
length_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

letters_var = tk.BooleanVar(value=True)
letters_checkbox = ttk.Checkbutton(main_frame, text="Include Letters", variable=letters_var)
letters_checkbox.grid(column=0, row=1, sticky=tk.W)

numbers_var = tk.BooleanVar(value=True)
numbers_checkbox = ttk.Checkbutton(main_frame, text="Include Numbers", variable=numbers_var)
numbers_checkbox.grid(column=0, row=2, sticky=tk.W)

symbols_var = tk.BooleanVar(value=True)
symbols_checkbox = ttk.Checkbutton(main_frame, text="Include Symbols", variable=symbols_var)
symbols_checkbox.grid(column=0, row=3, sticky=tk.W)

complex_rules_var = tk.BooleanVar(value=True)
complex_rules_checkbox = ttk.Checkbutton(main_frame, text="Complex Rules", variable=complex_rules_var)
complex_rules_checkbox.grid(column=0, row=4, sticky=tk.W)

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_and_display_password)
generate_button.grid(column=0, row=5, columnspan=2)

result_label = ttk.Label(main_frame, text="")
result_label.grid(column=0, row=6, columnspan=2)

root.mainloop()
