# Problem 3 Part b -- another withdrawal function -- for Homework 2 of CS107
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
        balance = balance - withdrawal_amount
        return balance
    
    return withdrawal

init_balance = 500
withdrawal_amount = 400
new_withdrawal_amount = 100
wd = make_withdrawal(init_balance)

explanation = "The functions returned an UnboudLocalError \n because the variable 'balance' in the withdrawal() function is used before it is assigned a value and is what we wanted to return at the end of withdrawal(). \n Python would disregard the 'balance' from make_withdrawal(balance) in this case.\n To pass the variable 'balance' from make_withdrawal(balance), we need to declare it as a nonlocal variable."

print(explanation)
print(wd(withdrawal_amount))
print(wd(new_withdrawal_amount))