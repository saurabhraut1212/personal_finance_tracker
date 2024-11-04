from datetime import datetime

class Transaction:
    def __init__(self, amount: float, category: str, description: str):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.amount = amount
        self.category = category
        self.description = description
    
    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }
    
    @staticmethod
    def from_dict(data):
        transaction = Transaction(
            amount=data["amount"],
            category=data["category"],
            description=data["description"]
        )
        transaction.date = data["date"]
        return transaction