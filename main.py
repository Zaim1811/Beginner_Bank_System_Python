class Atm():
    def __init__(self, account_name, account_number, balance=0):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def check_detail(self):
        print("Account Detail")
        print("Account Holder:" + self.account_name.title())
        print("Account number:" + self.account_number)
        print("Available balance: Rm%.2f" %self.balance)

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("The total balance is Rm%.2f" %self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount >= self.balance:
            print("Insufficient Balance")
            print("Please withdraw lesser amount")
            print("The current balance is Rm%.2f" %self.balance)
        else:
            self.balance = self.balance - self.amount
            print("The current balance is Rm%.2f" % self.balance)

    def check_balance(self):
        print("Balance is Rm%.2f" % self.balance)

    def menu(self):
        print("Menu:")
        print("1. Account Detail")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")

    def transaction(self):
        while True:
            self.menu()
            option = input("Enter number 1, 2, 3, or 4 to select the type of services:")
            if option == '1':
                Atm.check_detail(self)
                break
            elif option == '2':
                amount = float(input("Enter amount to deposit: Rm"))
                Atm.deposit(self, amount)
                break
            elif option == '3':
                amount = float(input("Enter amount to withdraw: Rm"))
                Atm.withdraw(self, amount)
                break
            elif option == '4':
                Atm.check_balance(self)
                break

            else:
                print("You can only enter no 1, 2, 3, or 4 only")

    def AskUserMorE(self):
        while True:
            print("Choose 'm' to menu or 'e' to exit below")
            repeat = input()
            if repeat not in ('e', 'm'):
                print("Choose 'm' or 'e' only'")
            else:
                return repeat

def log_name():
    while True:
        account_name = input("Enter your name:")
        nonspace = account_name.replace(' ', '')
        if nonspace.isalpha() == False:
            print('Please enter a alphabetical letter only')
        else:
            return account_name
def log_age():
    while True:
        account_number = input("Enter your id account number:")
        if not account_number.isdigit():
            print("Enter number only")
        else:
            return account_number

print("Welcome to the Bank")
atm = Atm(log_name(),log_age())
print("Congratulation! You has logged in succesfully")
while True:
    atm.transaction()
    final = atm.AskUserMorE()
    if final == 'e':
        print("Thank you for using our bank")
        break
