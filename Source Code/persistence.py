from account import BankAccount
from transaction import Transaction

USER_FILE = "users.txt"
TRANS_FILE = "transactions.txt"

def init_file(filename):
    """Creates file if it doesn't exist using try-except (No OS module)"""
    try:
        f = open(filename, "r")
        f.close()
    except FileNotFoundError:
        f = open(filename, "w")
        f.close()

def load_accounts():
    """Reads users.txt and returns a dict of BankAccount objects"""
    init_file(USER_FILE)
    accounts = {}
    with open(USER_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 5:
                acc = BankAccount(parts[0], parts[1], parts[2], parts[3], parts[4])
                accounts[acc.acc_num] = acc
    return accounts

def save_accounts(accounts_dict):
    """Overwrites users.txt with current data"""
    with open(USER_FILE, "w") as file:
        for acc in accounts_dict.values():
            file.write(str(acc) + "\n")

def log_transaction(trans_obj):
    """Appends a Transaction object to transactions.txt"""
    init_file(TRANS_FILE)
    with open(TRANS_FILE, "a") as file:
        file.write(str(trans_obj) + "\n")

def load_transactions(acc_num):
    """Returns list of transactions for a specific account"""
    init_file(TRANS_FILE)
    history = []
    with open(TRANS_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                # Filter by account number matches
                if int(parts[0]) == acc_num:
                    t = Transaction(parts[0], parts[1], parts[2], parts[3])
                    history.append(t)
    return history
