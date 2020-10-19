# PP7 Exercise_2
# Collaborators: Max Li, ChunChao Tseng, Yujie Cai

import numpy as np

def my_pow(r):
    def forward(data_structure):
        
        return np.power(data_structure,r),r*np.power(data_structure,r - 1)

    return forward

    

if __name__ == "__main__":
    f = my_pow(4)
    result = f(3)
    print(result)

