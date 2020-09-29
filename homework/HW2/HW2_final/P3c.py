# Problem 3 Part c -- improved withdrawal function -- for Homework 2 of CS107
# Author: Max Li

def make_withdrawal(balance):
    '''This function takes an account balance and pass it to its inner function which makes the withdrawal.
    raise Value Error if the input is not allow (e.g. not a number)'''
    if not isinstance(balance, (float, int)):
        raise ValueError("balance should be a float or an integer") 
    
    def withdrawal(withdrawal_amount):
        '''This function takes an withdrawal amount and deduct it from the account balance in its outer function.
        raise Value Error if the input is not allow (e.g. not a number or a number larger than balance)'''
        nonlocal balance
        if not isinstance(withdrawal_amount, (float, int)):
            raise ValueError("withdrawal amount should be a float or an integer")    
        if withdrawal_amount > balance:
            raise ValueError("withdrawal amount should be no larger than balance")   
        balance = balance - withdrawal_amount
        return balance
    
    return withdrawal

init_balance = 500
withdrawal_amount = 400
new_withdrawal_amount = 100
wd = make_withdrawal(init_balance)

print(wd(withdrawal_amount))
print(wd(new_withdrawal_amount))