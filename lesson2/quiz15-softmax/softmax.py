import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    s_L = []
    
    for i in range(len(L)):
        softmax_formula = np.exp(L[i]) / sum(np.exp(L))
        s_L.append(softmax_formula)

    return s_L
