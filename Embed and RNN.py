"""
Here, I am leraning how the tf implements 
RNN, Dense, and Embedding layers and how to chain them for NLP tasks
"""
import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
from tensorflow.python.keras.layers.recurrent_v2 import GRU

x1 = np.array([0, 1, 1])
x2 = np.array([[0,1,1],[1,2,0]])
embed = keras.layers.Embedding(4,5)
gru1 = keras.layers.GRU(15, return_sequences=True, return_state=True, )
dense1 = keras.layers.Dense(26)
dense2 = keras.layers.Dense(26)

z1 = embed(x1) # works even for one sample (T)
z2 = embed(x2) # as well as multiple samples (N, T)

try:
    b = gru1(z1)
except ValueError:
    print("Should fail because GRu only accepts (N, T, D) as input, not (T, D) for one smaple")
a = gru1(z2) # works for 3dim input

# GRU output will be
# 3dim -> if return_sequences is true
# 2dim -> if only returning the last hidden state
# the last time step's output should be equiv to the last hiden state (default return of RNNs)
test1 = (a[0][:, -1, :] - a[1] < 0.001)
print(test1)

# so dense works on BOTH 3dim and 2dim input
# which is good bc it can accept 3dim output form RNN layers with return_sequences
# its like there are dim1 * dim2 samples (N = 2 *3 = 6), but the original structure of the input stays the same 
# so kinda like (6, 15) -> (6, 26) but structurally stays the same so (2, 3, 15) -> (2, 3, 26)
# this represents an OUTPUT for each of the 3 times steps for each of the 2 samples
o1 = dense1(a[0])
o2 = dense1(a[1])

# since the last sequence is equivalent ot the returned state (pre-Dense layer), 
# the follow (post-Dense layer) should be true
test2 = o1[:, -1, :] - o2 < 0.001
print(test2)

print("debug")