import json
import logging
logging.basicConfig(
    filename="Account.log",
    level=logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)
type_of_account = ["saving account", "current account"]

class Account:
    id_counter = 0
    def __init__(self, name, balance, pin, account_type, account_id=None):
        self.name = name
        self._balance = balance
        self.__pin = pin
        self.account_type = account_type
        if account_id is None:
            Account.id_counter += 1
            self.account_id = Account.id_counter
        else:
            self.account_id = account_id
            Account.id_counter = max(Account.id_counter, account_id)


    def display_details(self):
        
        print(f"\nAccount Holder: {self.name}")
        print(f"Account ID: {self.account_id}")
        print(f"Account Type: {self.account_type}")

        print(f"\nBalance: ₹{self._balance}")


    def to_dict(self):
        return {
        "name": self.name,
        "balance": self._balance,
        "pin": self._Account__pin,
        "account_type": self.account_type,
        "account_id": self.account_id
         }
    @property
    def check_balance(self):
         return self._balance
    def deposit_fund(self, amount):
        if amount < 0:
            print("Invalid")
            return
        self._balance += amount

    def withdrawal(self, amount):
        if amount < 0:
            print("Invalid")
            return
        if amount > self._balance:
            print("Insufficient funds")
            return
        self._balance -= amount

    
    def pin_verify(self):
        print("\n====Pin===")
        pin_check = input("\nEnter current PIN: ")

        if self.__pin != pin_check:
            print("Incorrect PIN.")
            return False

        new_pin = input("Enter new 6 digit PIN: ")

        if len(new_pin) != 6 or not new_pin.isdigit():
            print("PIN must contain exactly 6 digits.")
            return False

        if new_pin == self.__pin:
            print("New PIN cannot be the same as the old PIN.")
            return False

        self.__pin = new_pin
        print("PIN successfully changed.")
        return True
        
    def pin_shoe(self):
        return self.__pin

try:
    with open("Account.json", "r") as file:
        data = json.load(file)
        project_legder = [Account(**account) for account in data]
except (FileNotFoundError, json.JSONDecodeError):
    project_legder = []

def json_account():
    with open("Account.json", "w") as file:
        json.dump([p.to_dict() for p in project_legder],
         file, indent=4)

class account_manage:
    def add_account(self):
        print("\n===Account Creation===")
        name_account = input("\nEnter name: ")
        if not name_account.strip():
            print("Invalid")
            logging.warning("Registration Failed.")
            return
        try:
            balance_account = int(input("Enter balance: "))
            if balance_account <= 0:
                print("Balance must be greater than 0.")
                logging.warning("Registration Failed.")
                return
        except ValueError:
            print("Invalid")
            logging.warning("Registration Failed.")
            return
        type_account = input("Enter the type of account(saving account/current account): ").lower()
        if not type_account.strip():
            print(f"The types of account available are: {type_of_account}")
            logging.warning("Registration Failed.")
            return
        if type_account not in type_of_account:
            print(f"The types of account available are: {type_of_account}")
            logging.warning("Registration Failed.")
            return

        try:
            pin_account = input("Enter a 6 digit pin: ")
            if len(pin_account) != 6 or not pin_account.isdigit():
                print("Enter a 6 digit pin.")
                logging.warning("Registration Failed.")
                return
            for pin in project_legder:
                if pin.pin_shoe() == pin_account:
                    print("This pin already exist.")
                    return

        except ValueError:
            print("Invalid")
            logging.warning("Registration Failed.")
            return
        
        account_creation = Account(name_account, balance_account, pin_account, type_account)
        project_legder.append(account_creation)
        json_account()
        print("\nAccount Created.")
        logging.info("Successfully register a new account")



    def remove_account(self):
        print("\n===Account Deletation===")
        try:
           removal_acc = int(input("\nEnter ID: "))
        except ValueError:
            print("ID contain digit.")
            return
        for id_removal_function in project_legder:
            if id_removal_function.account_id == removal_acc:
                project_legder.remove(id_removal_function)
                json_account()
                logging.info(f"Successfully deleted Account with ID:{removal_acc}")
                print("Account deleted.")
                break
        else:
            print("No account Found.")
            return
    
    def deposit_moneyin_account(self):
        print("\n====Deposit Fund====")
        try:
            first_id_check = int(input("\nEnter the ID: "))
        except ValueError:
            print("Invalid ID.")
            return

    # Find the correct account
        account = None

        for acc in project_legder:
            if acc.account_id == first_id_check:
                account = acc
                break

        if account is None:
            print("Account not found.")
            return

    # Verify the PIN of that particular account
        pin_deposit = input("Enter PIN: ")

        if account.pin_shoe() != pin_deposit:
            print("Incorrect PIN.")
            return

        try: 
            fund_raise = int(input("Enter the Funds: "))

            if fund_raise <= 0:
                print("Amount must be greater than 0.")
                return

            account.deposit_fund(fund_raise)
            json_account()

            logging.info(f"Successfully deposited ₹{fund_raise}.")
            print("Deposit successful!")

        except ValueError:
            print("Invalid amount.")
            return


    def withdrawal_money(self):
        print("\n====Withdraw Funds====")
        try:
           id_first = int(input("\nEnter ID"))
        except ValueError:
            print("Invalid")
            return
        account = None
        for acc in project_legder:
            if acc.account_id == id_first:
                account = acc
                break
        if account is None:
                print("No account found.")
                return

        pin_deposit = input("Enter pin: ")

        if account.pin_shoe() != pin_deposit:
            print("Invalid Pin.")
            return
        try:
            fund_deraiser = int(input("Enter funds: "))
            if fund_deraiser <= 0:
                print("Withdrawal funds must be greater than zero.")
                return

            if fund_deraiser > account.check_balance:
                print("Insufficent Funds.")
                return

            account.withdrawal(fund_deraiser)

            json_account()
            logging.info(f"Successfully Withdraw ₹{fund_deraiser}")
            print("Withdrawal successful")
        except ValueError:
            print("Invalid")
            return

    def display_account(self):
        try:
           multiple_user = int(input("Type '1' for individual acc and '2' for multiple acc: "))
        except ValueError:
            print("Invalid")
            return
        if multiple_user == 1:
            choose_acc = int(input("Enter ID: "))
            for id in project_legder:
                if id.account_id == choose_acc:
                    id.display_details()
                    logging.info(f"Check the details of account with id{choose_acc}")
                    break
            else:
                print("No account found.")
                return
        elif multiple_user == 2:
            print("\n=====Account Diplay===== ")
            for all in project_legder:
                all.display_details()

        

AccountManager = account_manage()
print("\n=====Project Legder=====")
while True:
    print("\n1. Create Account")
    print("2. Delete Account")
    print("3. Deposit Funds")
    print("4. Reset Pin")
    print("5. Withdraw Funds")
    print("6. Display Account")


    bank_user = input("\nChoose: ")
    if bank_user == "1":
        AccountManager.add_account()

    elif bank_user == "2":
        if not project_legder:
            print("No account register yet.")
        else:
            AccountManager.remove_account()

    elif bank_user == "3":
        if not project_legder:
            print("No account register yet.")
        else:
            AccountManager.deposit_moneyin_account()

    elif bank_user == "4":
        if not project_legder:
            print("No account register yet.")
        else:
            try:
               id_security = int(input("Enter ID: "))
            except ValueError:
                print("Invalid")
                continue
            for id_checker in project_legder:
                if id_checker.account_id == id_security:
                    if id_checker.pin_verify():
                        json_account()
                        logging.info(f"Successfully changed pin of ID{id_security}")
                    break
            else:
                print("Account not found")

    elif bank_user == "5":
        if not project_legder:
            print("No account register yet.")
        else:
            AccountManager.withdrawal_money()

    elif bank_user == "6":
        if not project_legder:
            print("No account register yet.")

        else:
            AccountManager.display_account()