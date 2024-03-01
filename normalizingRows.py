#common technique we use in Machine Learning and Deep Learning is to normalize our data
# gradient descent converges faster after normalization
# normalization we mean changing x to (dividing each row vector of x by its norm).

#Exercise: Implement normalizeRows() to normalize the rows of a matrix. After applying this function to an input matrix x, each row of x should be a vector of unit length (meaning length 1).

import numpy as np
import math

def normalizeRows(x):

    """
    Implement a function that normalizes each row of the matrix x (to have unit length).
    
    Argument:
    x -- A numpy matrix of shape (n, m)
    
    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    """
    
    ### START CODE HERE ### (≈ 2 lines of code)
    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    x_norm = np.linalg.norm(x,axis = 1,keepdims=True)
    print("x_norm = " + str(x_norm))

    # Divide x by its norm.
    x = x/x_norm
    print("result x = " + str(x))
    ### END CODE HERE ###

    return x

x = np.array([
    [0, 3, 4],
    [1, 6, 4]])
print("Row vector x = " + str(x))
print("normalizeRows(x) = " + str(normalizeRows(x)))