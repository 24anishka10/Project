import json

class Account:
    def __init__(self, account_number, name, pin_hash, balance=0.0, history=None):
        self.account_number = account_number
        self.name = name
        self.pin_hash = pin_hash
        self.balance = balance
        self.history = history if history else []

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "pin_hash": self.pin_hash,
            "balance": self.balance,
            "history": self.history
        }
