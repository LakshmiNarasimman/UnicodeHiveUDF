'''
Created on 31-Aug-2017

@author: bigdata
'''
from collections import Counter

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print dic1
dic_new={}
for d in (dic1,dic2,dic3):
    dic_new.update(d)
print dic_new  
usdic={1:"Narasimman",3:"Sridhar",2:"Malliga",5:"Sathya",4:"Vaijayanthi"}
print usdic.items()
for x,y in usdic.items():
    print "Key=",x, "Value=",y
    
def iskey_check(k):
        if k in usdic:
            print "key is already exist"
        else:
            print "key is not exists"    
iskey_check(2)
cal_dic={1:2,3:3,6:5,5:6}

for x in sorted(cal_dic.keys()):
    print x,cal_dic[x]

def remove_key(k):
    for x in cal_dic.keys():
        if x==k:
            del cal_dic[k]

my_dict = {'x':500, 'y':5874, 'z': 560}
my_dict1={'x':343,'y':532,'q':673}
max_call=max(my_dict.keys(),key=(lambda k:my_dict[k]))
min_call=min(my_dict.keys(),key=(lambda k:my_dict[k]))
print my_dict[max_call]
print my_dict[min_call]
print Counter(my_dict)+Counter(my_dict1)                       

   
   


