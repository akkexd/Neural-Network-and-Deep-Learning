
# Vectorization is the art of getting rid of explicit for-loops in code.
# In deep learning, you deal with very large datasets and hence, you need to make your computation as fast as possible.
# Vectorization allows you to efficiently compute on large datasets without using explicit for-loops.
# In Python, vectorization is efficiently implemented using NumPy, which provides an easy and flexible interface to optimize code.
#  np.dot() performs a matrix-matrix or matrix-vector multiplication. 
# This is different from np.multiply() and the * operator (which is equivalent to .* in
# Matlab/Octave), which performs an element-wise multiplication.
# np.dot() performs a matrix-matrix or matrix-vector multiplication.
# This is different from np.multiply() and the * operator (which is equivalent to .* in Matlab/Octave), which performs an element-wise multiplication.
# np.dot() performs a matrix-matrix or matrix-vector multiplication.


import time
import numpy as np
import math

x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]

### VECTORIZED DOT PRODUCT OF VECTORS ###
tic = time.process_time()
dot = np.dot(x1,x2)
toc = time.process_time()
print ("dot = " + str(dot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### VECTORIZED OUTER PRODUCT ###
tic = time.process_time()
outer = np.outer(x1,x2)
toc = time.process_time()
print ("outer = " + str(outer) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### VECTORIZED ELEMENTWISE MULTIPLICATION ###
tic = time.process_time()
mul = np.multiply(x1,x2)
toc = time.process_time()
print ("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")

### VECTORIZED GENERAL DOT PRODUCT ###
W = np.random.rand(3,len(x1)) # Random 3*len(x1) numpy array
tic = time.process_time()
dot = np.dot(W,x1)
toc = time.process_time()
print ("gdot = " + str(dot) + "\n ----- Computation time = " + str(1000*(toc - tic)) + "ms")