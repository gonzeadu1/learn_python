# # Object Oriented Programming Challenge
# # For this challenge, create a bank account class that has two attributes:
# # owner
# # balance
# # and two methods:
#
# # deposit
# # withdraw
# # As an added requirement, withdrawals may not exceed the available balance.
#
# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Hi, {self.owner}. You added {amount} to your account. Your new balance is {self.balance}")
#         return self.balance
#
#     def __str__(self):
#         return f"The balance is {self.balance} and the owner of the account is {self.owner}"
#
#     def withdraw(self, amount, minimum_deposit):
#         if amount <= self.balance >= minimum_deposit:
#             # self.balance = - amount ==>This is wrong!
#             self.balance -= amount
#             print(f"You withdrew {amount}. Your current balance is {self.balance}")
#         else:
#             print("You have exceeded your maximum withdrawal. Add more money into your account")
#
#         return self.balance
#
#
# account = Account("Gideon", 1000)
# print(account.__str__())
# # print(account.deposit(500))
# print(account.withdraw(100, 50))



class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


account = Account("Gideon", 10000)
print(account.__str__())
# print(account.deposit(500))
print(account.withdraw(10000))