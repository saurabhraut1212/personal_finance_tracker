import tkinter as tk
from tkinter import ttk

class TransactionListFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Transactions", padding="5")
        
        # Treeview for transactions
        self.tree = ttk.Treeview(self, columns=("Date", "Amount", "Category", "Description"), show="headings")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Description", text="Description")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
    
    def refresh_transactions(self, transactions):
        # Clear tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add transactions to tree
        for transaction in transactions:
            self.tree.insert("", "end", values=(
                transaction.date,
                f"${transaction.amount:.2f}",
                transaction.category,
                transaction.description
            ))