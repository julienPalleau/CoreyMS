"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9478326#search
Object Oriented Programming Challenge
"""


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        print("")
        self.balance += dep_amt
        print(f"Deposit Accepted\nYour deposit is: ${dep_amt}, your new balance is: ${self.balance}")

    def withdraw(self, wd_amt):
        print("")
        if self.balance - wd_amt >= 0:
            print(f"Withdrawal Accepted\nYour new amount after the withdraw is: ${self.balance - wd_amt}")
        else:
            print(f"Withdrawal of ${wd_amt} is Rejected\nFunds unavailable !")

    def __str__(self):
        return f"Account owner:   {self.owner}\nAccount balance: ${self.balance}"


acct1 = Account('Julien', 100)
print(acct1)

acct1.deposit(50)
acct1.withdraw(500)
