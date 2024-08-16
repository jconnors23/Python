# account class - create, deposit, withdraw 
import datetime 
import time

class Account():
    def __init__(self, name="", balance=0, transactions={}):
        self.name = name
        self.balance = balance
        self.transactions = transactions
    
    def set_name(self, name):
        self.name = name

    def get_current_date_time(self):
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_date

    def set_balance(self, starting_amount):
        self.balance += starting_amount
        self.update_transactions("account_opening", starting_amount, self.get_current_date_time())
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        self.update_transactions("deposit", amount, self.get_current_date_time())

    def withdraw(self, amount):
        self.balance -= amount
        self.update_transactions("withdraw", amount, self.get_current_date_time())

    def update_transactions(self, transaction_type, amount, time):
        self.transactions[time]={transaction_type: amount} 

    def get_transaction_history(self):
        return self.transactions

danny = Account()
danny.set_name("danny")
danny.set_balance(1000)
time.sleep(5)
danny.deposit(500)
print(danny.get_transaction_history())
#print(danny.get_balance())
# danny.withdraw(750)
# danny.get_balance()




    
    