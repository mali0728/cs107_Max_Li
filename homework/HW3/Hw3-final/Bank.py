# Problem 3 -- Bank Account Revisited -- for Homework 3 of CS107
# Author: Max Li
from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():

    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

    def withdraw(self, amount):
        if not isinstance(amount, (float, int)):
            raise ValueError("Withdrawal amount should be a float or an integer")    
        if amount > self.balance:
            raise ValueError("Withdrawal amount should be no larger than balance")   
        if amount < 0:
            raise ValueError("Withdrawal amount should not be negative")   
        
        self.balance = self.balance - amount
        return self.balance        

    def deposit(self, amount):
        if not isinstance(amount, (float, int)):
            raise ValueError("Deposit amount should be a float or an integer")    
        if amount < 0:
            raise ValueError("Deposit amount should not be negative")   
        
        self.balance = self.balance + amount
        return self.balance                

    def __str__(self):
        return ("Account Owner: " + self.owner + "\n" + "Account Type: " +  self.accountType.name)

    def __len__(self):
        return self.balance
        
           
        
class BankUser():

    def __init__(self, owner):
        self.owner = owner
        self.saving_account = None
        self.checking_account = None

    def addAccount(self, accountType):
        
        if accountType == AccountType.SAVINGS or accountType == 1:
            if self.saving_account == None:
                self.saving_account = BankAccount(self.owner, AccountType.SAVINGS)              
            else:
                raise ValueError("Can only have one savings account")
            
        if accountType == AccountType.CHECKING or accountType == 2:
            if self.checking_account == None:
                self.checking_account = BankAccount(self.owner, AccountType.CHECKING)
                
            else:
                raise ValueError("Can only have one checking account")

    def getBalance(self, accountType):
        if accountType == AccountType.SAVINGS or accountType == 1:
            if self.saving_account != None:
                return self.saving_account.balance             
            else:
                raise ValueError("No savings account yet")
            
        if accountType == AccountType.CHECKING or accountType == 2:
            if self.checking_account != None:
                return self.checking_account.balance  
                
            else:
                raise ValueError("No checking account yet")        

    def deposit(self, accountType, amount):
        if accountType == AccountType.SAVINGS or accountType == 1:
            if self.saving_account != None:
                return self.saving_account.deposit(amount)             
            else:
                raise ValueError("No saving account yet")
            
        if accountType == AccountType.CHECKING or accountType == 2:
            if self.checking_account != None:
                return self.checking_account.deposit(amount)  
                
            else:
                raise ValueError("No checking account yet")                

    def withdraw(self, accountType, amount):
        if accountType == AccountType.SAVINGS or accountType == 1:
            if self.saving_account != None:
                return self.saving_account.withdraw(amount)           
            else:
                raise ValueError("No saving account yet")
            
        if accountType == AccountType.CHECKING or accountType == 2:
            if self.checking_account != None:
                return self.checking_account.withdraw(amount)       
                
            else:
                raise ValueError("No checking account yet")                

    def __str__(self):
        message = ""
        if self.saving_account != None:
            message += (str(self.saving_account) + "\n" + "Balance: " + str(self.getBalance(AccountType.SAVINGS)) + "\n")
            
            
        if self.checking_account != None:
            message += (str(self.checking_account) + "\n" + "Balance: " + str(self.getBalance(AccountType.CHECKING)))    
        return message
    
    
    
def ATMSession(bankUser):
    def Interface():
        while True:
            print("Enter Option: ")
            print("1)Exit")
            print("2)Create Account")
            print("3)Check Balance")
            print("4)Deposit")
            print("5)Withdraw")
            option = int(input())
            
            if option == 1:
                print("End of Session")
                exit(1)
                
            elif option == 2:
                print("Enter Option:")
                print("1)Checking")
                print("2)Savings")
                option_1 = int(input())
                
                if option_1 == 1:
                    try:
                        bankUser.addAccount(AccountType.CHECKING)
                        print("Successfully created CHECKING account.")
                        
                    except Exception as e:
                        print(e)
                        
                elif option_1 == 2:
                    try:
                        bankUser.addAccount(AccountType.SAVINGS)
                        print("Successfully created SAVINGS account.")
                        
                    except Exception as e:
                        print(e)   
                        
                else:
                    print("Invalid option. Please try again.")
                    
            elif option == 3:
                print("Enter Option:")
                print("1)Checking")
                print("2)Savings")
                option_1 = int(input())
                
                if option_1 == 1:
                    try:
                        balance = bankUser.getBalance(AccountType.CHECKING)
                        print("Your balance is: " + str(balance))
                        
                    except Exception as e:
                        print(e)
                        
                elif option_1 == 2:
                    try:
                        balance = bankUser.getBalance(AccountType.SAVINGS)
                        print("Your balance is: " + str(balance))
                        
                    except Exception as e:
                        print(e)   
                        
                else:
                    print("Invalid option. Please try again.")
                    
            elif option == 4:
                print("Enter Option:")
                print("1)Checking")
                print("2)Savings")
                option_1 = int(input())
                
                if option_1 == 1:
                    print("Enter Integer Amount, Cannot Be Negative: ")
                    option_2 = int(input())
                    try:
                        new_balance = bankUser.deposit(AccountType.CHECKING, option_2)
                        print("Deposit processed successfully! Your new balance is: " + str(new_balance))
                        
                    except Exception as e:
                        print(e)
                        
                elif option_1 == 2:
                    print("Enter Integer Amount, Cannot Be Negative: ")
                    option_2 = int(input())                    
                    try:
                        new_balance = bankUser.deposit(AccountType.SAVINGS, option_2)
                        print("Deposit processed successfully! Your new balance is: " + str(new_balance))                        
                        
                    except Exception as e:
                        print(e)   
                        
                else:
                    print("Invalid option. Please try again.")
                    
            elif option == 5:
                print("Enter Option:")
                print("1)Checking")
                print("2)Savings")
                option_1 = int(input())
                
                if option_1 == 1:
                    print("Enter Integer Amount, Cannot Be Negative: ")
                    option_2 = int(input())
                    try:
                        new_balance = bankUser.withdraw(AccountType.CHECKING, option_2)
                        print("Withdraw processed successfully! Your new balance is: " + str(new_balance))
                        
                    except Exception as e:
                        print(e)
                        
                elif option_1 == 2:
                    print("Enter Integer Amount, Cannot Be Negative: ")
                    option_2 = int(input())                    
                    try:
                        new_balance = bankUser.withdraw(AccountType.SAVINGS, option_2)
                        print("Withdraw processed successfully! Your new balance is: " + str(new_balance))                        
                        
                    except Exception as e:
                        print(e)   
                        
                else:
                    print("Invalid option. Please try again.")  
                    
                    
            else:
                print("Invalid option. Please try again.")  
        
        
    return Interface
        
        
inter = ATMSession(BankUser("Max"))
inter()