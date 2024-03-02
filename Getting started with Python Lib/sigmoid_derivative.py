#Implement the function sigmoid_grad() to compute the gradient of the sigmoid function with respect to its input x
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

def sigmoid_derivative(y):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    
    ### START CODE HERE ### (≈ 2 lines of code)
    s = sigmoid(y)
    ds = s*(1-s)
    ### END CODE HERE ###
    
    return ds

print (" sigmoid_derivative([1,2,3]) = " + str(sigmoid_derivative(np.array([1,2,3]))))