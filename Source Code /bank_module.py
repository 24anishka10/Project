import json
import os
import random
from datetime import datetime

DATA_FILE = "data/accounts.json"

class BankAccount:
    def __init__(self, name, pin, acc_type, balance=0, acc_num=None, history=None):
        self.name = name
        self.pin = pin
        self.acc_type = acc_type
        self.balance = balance
        # Generate random 6-digit account number if not provided
        self.acc_num = acc_num if acc_num else random.randint(100000, 999999)
        self.history = history if history else []

    def deposit(self, amount):
        if amount <= 0:
            return False, "Amount must be positive."
        
        self.balance += amount
        self._log_transaction("Deposit", amount)
        return True, f"Successfully deposited ${amount}. New Balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Amount must be positive."
        if amount > self.balance:
            return False, "Insufficient funds."
        
        self.balance -= amount
        self._log_transaction("Withdrawal", amount)
        return True, f"Successfully withdrew ${amount}. New Balance: ${self.balance}"

    def _log_transaction(self, type, amount):
        """Private method to log transaction history"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append({
            "type": type,
            "amount": amount,
            "date": timestamp,
            "balance_after": self.balance
        })

    def to_dict(self):
        """Convert object to dictionary for JSON saving"""
        return {
            "acc_num": self.acc_num,
            "name": self.name,
            "pin": self.pin,
            "acc_type": self.acc_type,
            "balance": self.balance,
            "history": self.history
        }

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self._load_data()

    def _load_data(self):
        """Load data from JSON file on startup"""
        if not os.path.exists("data"):
            os.makedirs("data")
        
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as file:
                    data = json.load(file)
                    for acc_id, info in data.items():
                        self.accounts[int(acc_id)] = BankAccount(
                            info['name'], info['pin'], info['acc_type'], 
                            info['balance'], info['acc_num'], info['history']
                        )
            except (json.JSONDecodeError, ValueError):
                print("Warning: Data file corrupted or empty. Starting fresh.")

    def save_data(self):
        """Save all accounts to JSON file"""
        data = {acc_id: acc.to_dict() for acc_id, acc in self.accounts.items()}
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def create_account(self, name, pin, acc_type):
        new_acc = BankAccount(name, pin, acc_type)
        # Ensure unique account number
        while new_acc.acc_num in self.accounts:
            new_acc.acc_num = random.randint(100000, 999999)
            
        self.accounts[new_acc.acc_num] = new_acc
        self.save_data()
        return new_acc.acc_num

    def authenticate(self, acc_num, pin):
        if acc_num in self.accounts:
            if self.accounts[acc_num].pin == pin:
                return self.accounts[acc_num]
        return None
