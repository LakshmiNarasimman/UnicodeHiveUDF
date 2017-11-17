'''
Created on 26-Oct-2017

@author: bigdata
'''

import os
import sys
print sys.executable
import subprocess

os.chdir("/home/bigdata/bigdata_noahdata/Alex_Py/Python_practice")
names= open('dq_unisex_names.csv','r').read()
name_list=names.split('\n')
first_five=name_list[:5]
nested_list=[]
for x in name_list:
    sp_list=x.split(',')
    nested_list.append(sp_list)
numerical_list=[]
for numeric in nested_list:
    if numeric != ['']:
        text_data=numeric[0]
        num_data=numeric[1]
        numerical_list.append(float(num_data))  
print numerical_list  
cat = subprocess.Popen(["hadoop", "fs", "-cat", "/user/bigdata/train.csv"], stdout=subprocess.PIPE)
for line in cat.stdout:
    print line 
    