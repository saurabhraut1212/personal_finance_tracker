import tkinter as tk
from tkinter import ttk

class SummaryFrame(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Summary", padding="5")
        
        self.total_var = tk.StringVar(value="Total Balance: $0.00")
        ttk.Label(self, textvariable=self.total_var).grid(row=0, column=0, padx=5, pady=5)
    
    def update_total(self, transactions):
        total = sum(t.amount if t.category == "Income" else -t.amount for t in transactions)
        self.total_var.set(f"Total Balance: ${total:.2f}")