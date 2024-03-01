#Implement the sigmoid function using numpy.
import numpy as np
import math

def sigmoid(x):
    """
    Compute the sigmoid of x
    
    Arguments:
    x -- A scalar or numpy array of any size
    
    Return:
    s -- sigmoid(x)
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    s = 1/(np.exp(-x)+1)
    ### END CODE HERE ###
    
    return s

print(sigmoid(np.array([1, 2, 3]))) # result is (sigmoid(1), sigmoid(2), sigmoid(3))