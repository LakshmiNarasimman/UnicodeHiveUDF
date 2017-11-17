'''
Created on 09-Oct-2017

@author: bigdata
'''
import numpy as np
import pandas as pd

ser=pd.Series([12,23,3,232])
print ser.tolist()
df= pd.DataFrame({"X":[12,23,3,23,33],"y":[1,23,34,65,75],"z":[23,5,78,9,97]})
print df
print df['X'].tolist()
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
l = [12.23, 13.32, 100, 36.32]
print("Original List:",l)
a = np.array(l,np.int)
print("One-dimensional numpy array: ",a)
b=np.asfarray(np.arange(2,11).reshape(3,3))
x=np.ones((3,3))
x=np.pad(x, pad_width=1, mode='constant',constant_values=0)
print x
Y = np.ones((3,3))
print("Checkerboard pattern:")
y = np.zeros((8,8),dtype=int)
y[1::2,::2]=1
y[::2,1::2]=1
print y