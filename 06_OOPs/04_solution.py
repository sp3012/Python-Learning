# Encapsulation

# Define a class BankAccount with attributes account_number, account_holder, and balance.
# Make the balance attribute private.
# Provide methods to deposit money, withdraw money, and check the balance.
# Create an instance of BankAccount and demonstrate depositing and withdrawing money.

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
        
    def deposit_money (self, deposit):
        if deposit > 0:
            self.__balance += deposit 
            return f"Final balance is {self.__balance}"
        else:
            return "Deposit should be greater then 0"
    
    def withdraw_money (self, withdraw_amount):
        if withdraw_amount > 0:
            if withdraw_amount <= self.__balance:
                self.__balance -= withdraw_amount
                return f"After withdrawing {withdraw_amount}, your final balance is {self.__balance}"
            
            else:
                return "Insufficient fund!"
        
        else:
            return "Withdraw amount should be reater then 0"

    def balance_check(self):
        return self.__balance
    
my_bank_account = BankAccount(1234567890, "shubham", 10000)

print(my_bank_account.deposit_money(0))
print(my_bank_account.withdraw_money(1111111))
# print(my_bank_account.__balance)