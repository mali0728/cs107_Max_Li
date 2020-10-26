# Problem 3B_tests -- Tests for Bank.py -- for Homework 3 of CS107
# Author: Max Li
from Bank import BankAccount, BankUser, AccountType


def test_over_addAccount_1(): #this test function should throw an Exception or Error 
    user = BankUser("Jason")
    user.addAccount(AccountType.CHECKING)
    
    try:
        user.addAccount(AccountType.CHECKING) #this will cause an Exception or Error
    except Exception as e:
        print(e) #print the message for the Exeption

def test_over_addAccount_2(): #this test function should work
    user = BankUser("Jacob")
    user.addAccount(AccountType.CHECKING)
    
    try:
        user.addAccount(AccountType.SAVINGS) 
        print("Successfully added account!")
    except Exception as e:
        print(e) 
        
def test_over__str__(): #this test function should work
    user = BankUser("Jackson")
    user.addAccount(AccountType.CHECKING)
    user.deposit(AccountType.CHECKING, 10)
    user.addAccount(AccountType.SAVINGS) 
    user.deposit(AccountType.SAVINGS, 10)
    try:
        print(user)
    except Exception as e:
        print(e) #print the message for the Exeption    
        
        
def test_over_getBalance_(): #this test function should work
    user = BankUser("Javi")
    user.addAccount(AccountType.CHECKING)
    user.deposit(AccountType.CHECKING, 20)
    user.addAccount(AccountType.SAVINGS) 
    user.deposit(AccountType.SAVINGS, 1)
    try:
        print(user.getBalance(AccountType.CHECKING))
        print(user.getBalance(AccountType.SAVINGS))
    except Exception as e:
        print(e) #print the message for the Exeption   

def test_over_deposit_1(): #this test function should throw an Exception or Error 
    user = BankUser("Jack")
    user.addAccount(AccountType.SAVINGS)
    
    try:
        user.deposit(AccountType.SAVINGS, -10) #this will cause an Exception or Error
    except Exception as e:
        print(e) #print the message for the Exeption
        
def test_over_deposit_2(): #this test function should work
    user = BankUser("Jim")
    user.addAccount(AccountType.SAVINGS)
    
    try:
        new_balance = user.deposit(AccountType.SAVINGS, 10) 
        print("The new_balance is " + str(new_balance))
    except Exception as e:
        print(e) #print the message for the Exeption

def test_over_withdrawal_1(): #this test function should throw an Exception or Error 
    user = BankUser("John")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS, 10)
    try:
        user.withdraw(AccountType.SAVINGS, 1000) #this will cause an Exception or Error
    except Exception as e:
        print(e) #print the message for the Exeption
        
def test_over_withdrawal_2(): #this test function should work
    user = BankUser("Jeff")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS, 10)
    try:
        new_balance = user.withdraw(AccountType.SAVINGS, 1) 
        print("The new_balance is " + str(new_balance))
        
    except Exception as e:
        print(e) #print the message for the Exeption
        
        
def test_over_withdrawal_3(): #this test function should throw an Exception or Error 
    user = BankUser("Joe")
    user.addAccount(AccountType.CHECKING)
    try:
        user.withdraw(AccountType.CHECKING, -10) #this will cause an Exception or Error
    except Exception as e:
        print(e) #print the message for the Exeption


if __name__ == '__main__':
    print("test_over_addAccount_1:")        
    test_over_addAccount_1()
    print("\n")
    print("test_over_addAccount_2:")      
    test_over_addAccount_2()
    print("\n")
    print("test_over__str__:")      
    test_over__str__()
    print("\n")
    print("test_over_getBalance:")
    test_over_getBalance_()
    print("\n")
    print("test_over_deposit_1:")      
    test_over_deposit_1()
    print("\n")
    print("test_over_deposit_2:")      
    test_over_deposit_2()
    print("\n")
    print("test_over_withdrawal_1:")      
    test_over_withdrawal_1()
    print("\n")
    print("test_over_withdrawal_2:")      
    test_over_withdrawal_2()
    print("\n")
    print("test_over_withdrawal_3:")      
    test_over_withdrawal_3()