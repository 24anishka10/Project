class BankAccount:
    def __init__(self, acc_num, name, pin, acc_type, balance):
        self.acc_num = int(acc_num)
        self.name = name
        self.pin = pin
        self.acc_type = acc_type
        self.balance = float(balance)

    def __str__(self):
        return f"{self.acc_num},{self.name},{self.pin},{self.acc_type},{self.balance}"
