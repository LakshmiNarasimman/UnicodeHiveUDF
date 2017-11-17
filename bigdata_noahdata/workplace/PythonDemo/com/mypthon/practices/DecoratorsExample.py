'''
Created on 30-Aug-2017

@author: bigdata
'''


def foo(*args):
    for a in args:
        print a  
#foo(1,2,3,3,4)   

def foo1(**kargs):
    for b in kargs:
        print b
foo1(p=1,q=2,r=3,s=4,t=5)             
        
        