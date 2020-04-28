class Bank:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def Deposit(self,amount):
        self.balance += amount

    def Withdraw(self,amount):
        if self.balance > amount
        self.balance -= amount

amruth = Bank('Amruth', 0)

print(amruth.balance)
amruth.Deposit(1000)
print(amruth.balance)
amruth.Withdraw(200)
print(amruth.balance)