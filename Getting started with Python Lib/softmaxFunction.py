# Broadcasting and the softmax function
# A very important concept to understand in numpy is "broadcasting". 
# It is very useful for performing mathematical operations between arrays of different shapes.
# For the softmax function, you will be computing e^{z^{\left(i\right)}}e
# z(i)
#  for every training example i and for every feature j.

# Exercise: Implement a softmax function using numpy. You can think of softmax as a normalizing function used when your algorithm needs to classify two or more classes. You will learn more about softmax in the second course of this specialization.

# using the common math notation m x n: m is the number of rows and n is the number of columns.

import numpy as np
import math

def softmax(x):
    """Calculates the softmax for each row of the input x.

    Your code should work for a row vector and also for matrices of shape (m,n).

    Argument:
    x -- A numpy matrix of shape (m,n)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (m,n)
    """
    
    ### START CODE HERE ### (≈ 3 lines of code)
    # Apply exp() element-wise to x. Use np.exp(...).
    x_exp = np.exp(x)
    print("x_exp = " + str(x_exp))

    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).
    x_sum = np.sum(x_exp,axis=1,keepdims=True)
    print("x_sum = " + str(x_sum))
    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.
    s = x_exp/x_sum
    print("s = " + str(s))
    ### END CODE HERE ###
    
    return s

x = np.array([
    [9, 2, 5, 0, 0],
    [7, 5, 0, 0 ,0]])

print("softmax(x) = " + str(softmax(x)))


