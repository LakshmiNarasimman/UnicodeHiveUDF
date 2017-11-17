'''
Created on 06-Oct-2017

@author: bigdata
'''
import numpy as np
import time
from timeit import Timer
vec_size=1000
def pure_py_ver():
    t1= time.time()
    X=range(vec_size)
    Y=range(vec_size)
    Z=[]
    for i in range(len(X)):
        Z.append(X[i]+Y[i])
        
    return (time.time()-t1)


def np_ver():
    t2=time.time()
    X=np.arange(vec_size)
    Y=np.arange(vec_size)
    Z=X+Y
    return time.time() - t2
A = np.array([ [3.4, 8.7, 9.9], 
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])
