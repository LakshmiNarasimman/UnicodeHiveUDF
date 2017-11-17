'''
Created on 06-Nov-2017

@author: bigdata
'''
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 50, 1000)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
y1 = 30*x + 1000
y2 = 50*x + 100

plt.plot(x, y1, c='orange')
plt.plot(x, y2, c='blue')

matrix_three = np.asarray([
    [1, -1/30, -1000/30],
    [0, 1, 2350]  
], dtype=np.float32)
matrix_three[0] += matrix_three[1]/30
print(matrix_three)
matrix_three[1]=matrix_three[1]*(20/30)
print(matrix_three)
