# Problem 1 -- Motivating Automatic Differentiation -- for Homework 4 of CS107
# Author: Max Li

import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f,h):
    """Returns the numerical approximation of the derivative of the input function f
    with stepsize h at x, which is given to the inner function.
    
        INPUTS
        =======
        f: symbolic expression of a function of a single variable
        h: float, stepsize of the approximation
           
        RETURNS
        ========
        f_prime: a function which takes as input a value of x 
        that computes the numerical approximation
        
        EXAMPLES
        =========
        >>> f_prime = numerical_diff(np.square, 0.1)
        >>> f_prime(3)
        6.1
        """
    def f_prime(x):
        derivative = (f(x+h)-f(x))/h
        return derivative
    
    return f_prime
    
        
        
if __name__ == '__main__':   
    x_range = np.linspace(0.2, 0.4, 100)
    h_list = [0.1,1e-7,1e-15]
    
    fp_FD_list = [np.zeros(len(x_range))] * 3
    real_fp = [1/x for x in x_range]

    for j in range(len(fp_FD_list)):
        
        fp_FD_list[j] = [numerical_diff(np.log, h_list[j])(x) for x in x_range]
    
    plt.xlabel('x')
    plt.ylabel("f ' (x)")        
    plt.plot(x_range, real_fp, color = 'yellow',linewidth = 3, label = 'Analytical derivative')
    plt.plot(x_range, fp_FD_list[0], color = 'red', linewidth = 1, label = 'h = 0.1')
    plt.plot(x_range, fp_FD_list[1], color = 'black', linewidth = 1, label = 'h = 1e-7')
    plt.plot(x_range, fp_FD_list[2], color = 'blue', linewidth = 1, label = 'h = 1e-15')
    plt.legend(loc = 'upper right')
    
    print("Answer to Q-a: \n", 
          "h = 1e-7 gives us the closest approximation to the true derivative.\n"
          "When h is too small, doing division by h will amplify floating point errors,",
          " making the approximate derivatives of x values close to each other the same, ",
          "which leads to inaccurate results.\n",
          "When h is too large, the approximation is simply inaccurate, getting far off the real derivatives.")
    print("Answer to Q-b: \n",
          "Automatic differentiation will allow us to evaluate derivatives to machine precision ",
          "while not being computationally costly, because it uses chain rule and ",
          "elementary operations to evaluate derivates in several steps.")
    
    plt.show()