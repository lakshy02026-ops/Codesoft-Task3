import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5)
        self.length_entry = tk.Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=5)
        self.length_entry.insert(0, "12")
        
        self.upper_var = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Uppercase", variable=self.upper_var).grid(row=1, column=0, columnspan=2, sticky="w", padx=10)
        
        self.lower_var = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Lowercase", variable=self.lower_var).grid(row=2, column=0, columnspan=2, sticky="w", padx=10)
        
        self.digits_var = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Digits", variable=self.digits_var).grid(row=3, column=0, columnspan=2, sticky="w", padx=10)
        
        self.symbols_var = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Symbols", variable=self.symbols_var).grid(row=4, column=0, columnspan=2, sticky="w", padx=10)
        
        tk.Button(root, text="Generate Password", command=self.generate_password).grid(row=5, column=0, columnspan=2, pady=10)
        
        self.password_display = tk.Entry(root, font=("Arial", 14), justify="center", width=30)
        self.password_display.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
    
    def generate_password(self):
        length = int(self.length_entry.get())
        chars = ""
        if self.upper_var.get():
            chars += string.ascii_uppercase
        if self.lower_var.get():
            chars += string.ascii_lowercase
        if self.digits_var.get():
            chars += string.digits
        if self.symbols_var.get():
            chars += string.punctuation
        
        if not chars:
            password = "Select at least one option"
        else:
            password = ''.join(random.choice(chars) for _ in range(length))
        
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()