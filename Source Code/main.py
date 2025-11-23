import validators
from bank_logic import BankController

def main():
    controller = BankController()
    
    print("=== BANK MANAGEMENT SYSTEM ===")
    
    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            anum = input("Enter Account Number: ")
            if not validators.validate_account_num(anum):
                print("Invalid Account Number.")
                continue
                
            name = input("Enter Name: ")
            if not validators.validate_name(name):
                print("Invalid Name.")
                continue
                
            print(controller.create_account(anum, name))

        elif choice == '2':
            anum = input("Enter Account Number: ")
            amt_str = input("Enter Deposit Amount: ")
            amount = validators.validate_positive_amount(amt_str)
            
            if amount:
                print(controller.process_transaction(anum, "DEPOSIT", amount))
            else:
                print("Invalid amount.")

        elif choice == '3':
            anum = input("Enter Account Number: ")
            amt_str = input("Enter Withdraw Amount: ")
            amount = validators.validate_positive_amount(amt_str)
            
            if amount:
                print(controller.process_transaction(anum, "WITHDRAW", amount))
            else:
                print("Invalid amount.")

        elif choice == '4':
            anum = input("Enter Account Number: ")
            print(controller.get_balance(anum))

        elif choice == '5':
            print("Exiting system...")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
