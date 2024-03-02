# Exercise: Implement the numpy vectorized version of the L2 loss. There are several way of implementing the L2 loss but you may find the function np.dot() useful.
# As a reminder, if  x=[x1,x2,x3,...,xn]  then  np.dot(x,x) = ∑i=0 to n x^2i.
# L2 loss is defined as:
# L2(y^,y)=∑i=0 to n(y^i−yi)2L2(y^,y)=∑i=0 to n(y^i−yi)2

import numpy as np
import math

def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L2 loss function defined above
    """
    
    ### START CODE HERE ### (≈ 1 line of code)
    loss = np.dot(yhat - y, yhat - y)
    ### END CODE HERE ###
    
    return loss

yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L2 = " + str(L2(yhat,y)))
