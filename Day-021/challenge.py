

class Bankaccounts:
    def __init__(self , account1 , account2):
        self.account1 = account1
        self.account2 = account2
    def __add__(self):
        return self.account1 + self.account2

account1 = int(input("enter balance in account1 : "))
account2 = int(input("enter balance in account2 : "))
acc1 = Bankaccounts(account1)
acc2 = Bankaccounts(account2)
print("acc1")
print("acc2")
print(acc1 + acc2)        