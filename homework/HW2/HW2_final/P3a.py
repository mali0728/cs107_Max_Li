# Problem 3 Part a -- simple withdrawal function -- for Homework 2 of CS107
# Author: Max Li

def make_withdrawal(balance):
    '''This function takes an account balance and pass it to its inner function which makes the withdrawal.
    raise Value Error if the input is not allow (e.g. not a number)'''
    if not isinstance(balance, (float, int)):
        raise ValueError("balance should be a float or an integer") 
    
    def withdrawal(withdrawal_amount):
        '''This function takes an withdrawal amount and deduct it from the account balance in its outer function.
        raise Value Error if the input is not allow (e.g. not a number or a number larger than balance)'''
        if not isinstance(withdrawal_amount, (float, int)):
            raise ValueError("withdrawal amount should be a float or an integer")    
        if withdrawal_amount > balance:
            raise ValueError("withdrawal amount should be no larger than balance")          
        return balance - withdrawal_amount
    
    return withdrawal

init_balance = 500
withdrawal_amount = 400
new_withdrawal_amount = 100
wd = make_withdrawal(init_balance)

explanation = "The functions did not behave as expected bacause in wd(new_withdrawal_amount), wd is a whole new make_withdrawal which has input init_balance and does not have any memory of what is return from wd(withdrawal_amount)."

print(explanation)
print(wd(withdrawal_amount))
print(wd(new_withdrawal_amount))