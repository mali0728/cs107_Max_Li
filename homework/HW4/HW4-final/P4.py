# Problem 4 -- A Toy AD Implementaion -- for Homework 4 of CS107
# Author: Max Li

class AutoDiffToy():

    def __init__(self, val, der=1):
        self.val = val
        self.der = der

    def __add__(self, other):
        
        try:
            new_val = self.val + other.val
            new_der = self.der + other.der                  
                    
        except AttributeError:
            new_val = self.val + other
            new_der = self.der 
            
        return AutoDiffToy(new_val, new_der)
        
    def __radd__(self, other):     
        return self.__add__(other)
        
    def __mul__(self, other):
        try:
            new_val = self.val * other.val
            new_der = self.val * other.der + other.val * self.der
            
        except AttributeError:
            new_val = self.val * other
            new_der = self.der * other     
            
        return AutoDiffToy(new_val, new_der)
               
    def __rmul__(self, other):
        return self.__mul__(other)
        
    
    
if __name__ == '__main__':
    a = 2.0 # Value to evaluate at
    x = AutoDiffToy(a)
    
    alpha = 2.0
    beta = 3.0
    f1 = alpha * x + beta
    f2 = x * alpha + beta
    f3 = beta + alpha * x
    f4 = beta + x * alpha
    
    print(f1.val, f1.der)
    print(f2.val, f2.der)
    print(f3.val, f3.der)
    print(f4.val, f4.der)
    
    a = 9.0 # Value to evaluate at
    b = 3.0
    x = AutoDiffToy(a)
    
    alpha = 2.0
    beta = AutoDiffToy(b)
    f1 = alpha * x + beta
    f2 = x * alpha + beta
    f3 = beta + alpha * x
    f4 = beta + x * alpha
    
    print(f1.val, f1.der)
    print(f2.val, f2.der)
    print(f3.val, f3.der)
    print(f4.val, f4.der)    
    
    
    