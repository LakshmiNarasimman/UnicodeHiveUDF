'''
Created on 05-Oct-2017

@author: bigdata
'''
from tables.tests.create_backcompat_indexes import row
import timeit 
'''
import math
class ToStringConvert(object):
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=raw_input("Enter a string:\n")
    def toString(self):
        print self.s.upper()        
strObj=ToStringConvert()
strObj.getString()
strObj.toString()

'''
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print "unsorted liss:",my_list
my_list.sort(key=lambda e:e['key']['subkey'],reverse=False)
print "sorted list:",my_list



def to_flat(matrix):
    new_lis=[]
    for row in matrix:
        for x in row:
            new_lis.append(x)
    return new_lis        
matrix=[range(0,6),range(6,12),range(13,19)]
print matrix
print to_flat(matrix)
print [row for row in matrix]

print [x for row in matrix for x in row]
vowels = 'aeiou'
sentence="sadjkdjwdjwpjkpppioouc"
print ",".join([x for x in sentence if x not in vowels])

dic=dict()
list1=[1,2,3,4,5,6,7]
print map(lambda x:x+1,list1)

list2=['a','b','c','d','e','f','g']
def to_dict(keys,values):
    for i in range(len(keys)):
        dic[keys[i]]=values[i]
    return dic
print to_dict(list1, list2)  
def to_dict_short(keys,values):
    print {keys[i]:values[i] for i in range(len(keys))}  
to_dict_short(list1, list2)        
        
def square_map(arr):
    return map(lambda x: x**2, arr)

 
