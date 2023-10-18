class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def depos(self, deposit):
        self.balance += deposit
        print(f"vous deposez ${deposit}")
        print("Deposit Accepted")
        return f"nouveau solde {self.balance}\n"

    def withdraw(self, withdraw):
        if (withdraw < self.balance):
            print(f"Vous retirez ${withdraw}")
            self.balance -= withdraw
            print("Withdraw Accepted")
        else:
            print("Withdraw Refused")
        return f"nouveau solde ${self.balance}\n"

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}\n"


acct1 = Account('Julien', 100)
print(acct1)
print(acct1.withdraw(50))
print(acct1.depos(100))
print(acct1)
