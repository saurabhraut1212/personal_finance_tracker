import tkinter as tk
from tkinter import ttk
from gui.transaction_frame import TransactionInputFrame
from gui.transaction_list import TransactionListFrame
from gui.summary_frame import SummaryFrame
from utils.data_manager import DataManager

class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("800x600")
        
        # Data management
        self.data_manager = DataManager()
        self.transactions = self.data_manager.load_transactions()
        
        # Main container
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Transaction input
        self.input_frame = TransactionInputFrame(main_frame, self.on_add_transaction)
        self.input_frame.grid(row=0, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # Transaction list
        self.list_frame = TransactionListFrame(main_frame)
        self.list_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Summary
        self.summary_frame = SummaryFrame(main_frame)
        self.summary_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # Initial refresh
        self.refresh_ui()
    
    def on_add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.data_manager.save_transactions(self.transactions)
        self.refresh_ui()
    
    def refresh_ui(self):
        self.list_frame.refresh_transactions(self.transactions)
        self.summary_frame.update_total(self.transactions)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()