import json
import os
from models.transaction import Transaction

class DataManager:
    def __init__(self, filename="data/transactions.json"):
        self.filename = filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    def save_transactions(self, transactions):
        data = [t.to_dict() for t in transactions]
        with open(self.filename, "w") as f:
            json.dump(data, f)
    
    def load_transactions(self):
     try:
        with open(self.filename, "r") as f:
            if f.read().strip() == "":  
                return []
            f.seek(0) 
            data = json.load(f)
            return [Transaction.from_dict(t) for t in data]
     except FileNotFoundError:
        # Create an empty file with an empty list if it doesn’t exist
        with open(self.filename, "w") as f:
            json.dump([], f)
        return []