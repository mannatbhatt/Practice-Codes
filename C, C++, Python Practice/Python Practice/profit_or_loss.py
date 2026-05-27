class Account:
    def __init__(self, bal, acc):
        self.initial_balance = bal
        self.balance = bal
        self.acc = acc

    def debit(self, amount):
        self.balance -= amount
        return amount

    def credit(self, amount):
        self.balance += amount
        return amount

    def get_balance(self):
        return self.balance

    def profit_or_loss(self):
        if self.balance > self.initial_balance:
            print("Profit:", self.balance - self.initial_balance)

        elif self.balance < self.initial_balance:
            print("Loss:", self.initial_balance - self.balance)

        else:
            print("No Profit No Loss")


u1 = Account(150000, 42135)
u1.debit(2000)
u1.credit(1000)

u2 = Account(145000, 2313)
u2.debit(2000)
u2.credit(1800)
print("Current Balance: ",u1.get_balance())
u1.profit_or_loss()
print("Current Balance:", u2.get_balance())
u2.profit_or_loss()