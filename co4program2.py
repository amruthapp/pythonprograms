class Bank:
    def __init__(self,acc_no,name,type,balance):
        self.acc_no=acc_no
        self.name=name
        self.type=type
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("amount deposited successfully ")
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance ")
            return self.balance
        else:
            self.balance=self.balance-amount
            print("amount withdrawn successfully")
            return self.balance
bank__=Bank(5460000674,"AKHILA T","SAVINGS",5000)
dep_amount=float(input("enter the amount to be deposited :"))
print("account balance : ",bank__.deposit(dep_amount))
with_amount=float(input("enter the amount to be withdrawn : "))
print("account balance : ",bank__.withdraw(with_amount))


