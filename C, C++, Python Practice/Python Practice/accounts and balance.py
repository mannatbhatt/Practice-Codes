class Account:
    def __init__(self, bal, acc):
        self.initial_balance = bal
        self.balance = bal
        self.acc = acc

    def debit(self, amount):
        self.balance -= amount
        print(amount, "debited successfully")

    def credit(self, amount):
        self.balance += amount
        print(amount, "credited successfully")

    def get_balance(self):
        return self.balance

    def profit_or_loss(self):
        if self.balance > self.initial_balance:
            print("Profit:", self.balance - self.initial_balance)

        elif self.balance < self.initial_balance:
            print("Loss:", self.initial_balance - self.balance)

        else:
            print("No Profit No Loss")


accounts = {}

while True:

    choice = int(input("\nEnter 1 to continue or 0 to stop: "))

    if choice == 1:

        acc = int(input("Enter account number: "))

        # CHECK IF ACCOUNT ALREADY EXISTS
        if acc in accounts:
            user = accounts[acc]
            print("Account found")
            print("Current Balance:", user.get_balance())

        else:
            bal = int(input("Enter opening balance: "))
            user = Account(bal, acc)

            accounts[acc] = user
            print("New account created")

        ch = input("Do you want to debit or credit? ").lower()

        amount = int(input("Enter amount: "))

        if ch == "debit":
            user.debit(amount)

        elif ch == "credit":
            user.credit(amount)

        else:
            print("Invalid choice")

        print("Updated Balance:", user.get_balance())

    else:
        print("Program stopped")
        break