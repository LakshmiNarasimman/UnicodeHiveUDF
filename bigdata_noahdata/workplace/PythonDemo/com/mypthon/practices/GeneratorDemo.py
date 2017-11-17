'''
Created on 19-Oct-2017

@author: bigdata
'''
n=10
def gen_item(n):
    for i in range(n):
        yield i
        
gen=gen_item(n)       
for x in range(n):
    print gen.next()
    
        