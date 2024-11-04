import tkinter as tk
from tkinter import ttk
from models.transaction import Transaction

class TransactionInputFrame(ttk.LabelFrame):
    def __init__(self, parent, on_add_transaction):
        super().__init__(parent, text="Add Transaction", padding="5")
        self.on_add_transaction = on_add_transaction
        
        # Amount
        ttk.Label(self, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_var = tk.StringVar()
        self.amount_entry = ttk.Entry(self, textvariable=self.amount_var)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Category
        ttk.Label(self, text="Category:").grid(row=0, column=2, padx=5, pady=5)
        self.categories = ["Income", "Food", "Transport", "Utilities", "Entertainment", "Other"]
        self.category_var = tk.StringVar()
        category_combo = ttk.Combobox(self, textvariable=self.category_var, values=self.categories)
        category_combo.grid(row=0, column=3, padx=5, pady=5)
        category_combo.set("Other")
        
        # Description
        ttk.Label(self, text="Description:").grid(row=0, column=4, padx=5, pady=5)
        self.desc_var = tk.StringVar()
        self.desc_entry = ttk.Entry(self, textvariable=self.desc_var)
        self.desc_entry.grid(row=0, column=5, padx=5, pady=5)
        
        # Add button
        add_btn = ttk.Button(self, text="Add Transaction", command=self.add_transaction)
        add_btn.grid(row=0, column=6, padx=5, pady=5)
    
    def add_transaction(self):
        try:
            amount = float(self.amount_var.get())
            category = self.category_var.get()
            description = self.desc_var.get()
            
            transaction = Transaction(amount, category, description)
            self.on_add_transaction(transaction)
            
            # Clear inputs
            self.amount_var.set("")
            self.desc_var.set("")
            self.category_var.set("Other")
            
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid amount")