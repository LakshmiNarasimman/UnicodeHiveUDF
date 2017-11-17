'''
Created on 29-Aug-2017

@author: bigdata
'''
import os
os.chdir("/home/bigdata/bigdata_noahdata/mGage-Phase-3-POC/Python_Script_byDavid") 
print os.getcwd()
f=open("Sample.txt","w+")
f.write("Hello I am writting into a file..")    
