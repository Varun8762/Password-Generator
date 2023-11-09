import tkinter as tk
import random
import string

class RandomPasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        
        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack(pady=10)
        
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.password_var, state="readonly")
        self.password_entry.pack(pady=5, padx=10)
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password , bg="green")
        self.generate_button.pack(pady=5)
        
        root.geometry("300x300")
        root.configure(bg="black")
        
    def generate_password(self):
        password_length = 8
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        self.password_var.set(generated_password)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = RandomPasswordGenerator(root)
    root.mainloop()
